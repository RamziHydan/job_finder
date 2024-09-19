from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job,Comment,Category
from django.core.paginator import Paginator
from .form import ApplyForm,JobForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .filters import JobFilter
from . models import Apply
from django.views.generic import CreateView
from django.views.generic import ListView

from django.utils.translation import get_language,activate,gettext
from django.utils.translation import gettext_lazy as _
from django.db.models import Count

def translate(language):
    cur_lang=get_language()
    try:
        activate(language)
    finally:
        activate(cur_lang)



def index(request):
    categories=Category.objects.all()
    context={
        'categories':categories,
    }
    return render(request,'index.html',context)

def admin_approval(request):
    trans=translate(language='ar')
    if request.user.is_authenticated:
        job_list = Job.objects.filter(owner=request.user)

        if request.method == 'POST':
            id_list = request.POST.getlist('boxes')
            job_list.filter(pk__in=id_list).update(available=True)
            job_list.exclude(pk__in=id_list).update(available=False)

            messages.success(request, _('Approval has been approved successfully 👍'))
            return redirect('admin-approval')
        else:

            context = {
                'job_list': job_list,
                'trans':trans,
            }
            return render(request, 'job/dashboard.html', context)
    else:
        messages.success(request,_('You need to be logged in to access this page.')) 
        return redirect('/login')

     
from taggit.models import Tag
from django.shortcuts import get_object_or_404
from django.db.models import Q

def job_list(request, tag_slug=None):
    trans = translate(language='ar')
    job_list = Job.objects.filter(available=True)
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        job_list = job_list.filter(tags__in=[tag])

    # Get unique tags
    all_tags = Tag.objects.all()  # Get all tags
    unique_tags = set(all_tags)  # Convert to set for easier manipulation

    if tag:
        unique_tags.discard(tag)  # Remove the selected tag from unique_tags

    # Get the search query from the request GET parameters
    search_query = request.GET.get('search')
    if search_query:
        job_list = job_list.filter(Q(title_ar__icontains=search_query) | Q(title_en__icontains=search_query))

    p = Paginator(job_list, 3)
    page = request.GET.get('page')
    job_list = p.get_page(page)
    nums = " " * job_list.paginator.num_pages

    context = {
        'job_list': job_list,
        'nums': nums,
        'trans': trans,
        'tag': tag,
        'unique_tags': unique_tags,
    }

    return render(request, 'job/job_listing.html', context)





from django.contrib.auth.decorators import login_required

@login_required

def job_details(request, slug):
    job_details = Job.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(job=job_details, active=True)
    apply = None
    comment_form = CommentForm()
    form = ApplyForm()

    if request.method == "POST":
        if request.POST.get('action') == 'apply_job':
            if job_details.owner == request.user:
                messages.error(request, _('You cannot apply for your own job.'))
            else:
                form = ApplyForm(request.POST, request.FILES)
                if form.is_valid():
                    apply_instance = form.save(commit=False)
                    apply_instance.Applier = request.user
                    apply_instance.job = job_details
                    apply_instance.save()
                    messages.success(request, _('Applying operation has been done successfully 👍'))
                    return redirect(reverse('job-details', args=[job_details.slug]))
                else:
                    form = ApplyForm()
        elif request.POST.get('action') == 'leave_comment':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                leave_comment = comment_form.save(commit=False)
                leave_comment.name = request.user
                leave_comment.job = job_details
                leave_comment.save()
                return redirect(reverse('job-details', args=[job_details.slug]))
            else:
                comment_form = CommentForm()
    else:
        initial_data = {'Applier': request.user}
        form = ApplyForm(initial=initial_data)
        apply = Apply.objects.filter(job=job_details, Applier=request.user).first()

    job_tags_ids = job_details.tags.values_list('id', flat=True)
    similar_jobs = Job.objects.filter(tags__in=job_tags_ids)\
                              .exclude(id=job_details.id)\
                              .annotate(same_tags=Count('tags'))\
                              .order_by('-same_tags', '-published_at')[:4]

    context = {
        'job_details': job_details,
        'form': form,
        'apply': apply,
        'comment_form': comment_form,
        'comments': comments,
        'similar_jobs': similar_jobs,
    }

    return render(request, 'job/job_details.html', context)






@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            form = JobForm()
            messages.success(request, _('Your job has been added successfully'))
            return redirect(reverse('job-list'))
        else:
            messages.error(request, _('There was an error saving the job. Please try again.'))
    else:
        form = JobForm()

    context = {
        'form': form,
    }
    return render(request, 'job/add_job.html', context)

