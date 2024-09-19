from django.urls import reverse
from .forms import SignupForm,UserForm,ProfileForm
from .models import Profile
from django.contrib import messages
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,("You have been signup successfully ✅"))
            return redirect('/accounts/profile')
    else:
        form=SignupForm()
    context={
        'form': form,
    }
    messages.success(request,(" Opration field 😢"))
    return render(request,'registration/signup.html',context)

# def register_user(request):
#     if request.method =='POST':
#         form= RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             user=authenticate(username=username,password=password)
#             login(request ,user)
#             messages.success(request,("You have been registered successfully"))
#             return redirect('home')            
#     else:
#         form=RegisterUserForm()
#     context={
#         'form': form
#     }
#     return render(request,'authentication/register_user.html',context)
def pro(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'navbar.html',{'pro':profile})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform=UserForm(request.POST ,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES ,instance=profile)          
        if userform.is_valid and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            messages.success(request,("Your profile has been updated ✅"))
            return redirect(reverse('account:profile'))
            # return redirect(reverse('accounts/profile'))
    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=profile)

    context={
            'profile':profile,
            'userform':userform,
            'profileform':profileform,
            }    
    return render(request,'accounts/profile_edit.html',context)


