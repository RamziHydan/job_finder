from django.shortcuts import render
from .models import Info
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact_view(request):
    MyInfo=Info.objects.first()
    if request.method=="POST":
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['message']
        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )
        messages.success(request, 'Email has been send successfully')

        # messages.success(request,('Your email has been submitted successfully'))
    context={
        'infos': MyInfo
    }
    return render(request,'contact/contact.html',context)