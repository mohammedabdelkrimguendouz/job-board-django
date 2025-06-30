from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

from .form import ApplicationForm, JobForm
from .models import Category, Job


def job_list(request):
    job_list = Job.objects.all()


    filter = JobFilter(request.GET,queryset=job_list)
    job_list = filter.qs

    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)





    return render(request, 'job/jobs.html', {'jobs': page_obj , 'filter':filter})



def job_details(request,slug):

    job = Job.objects.get(slug = slug)


    if(request.method == 'POST'):
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)  # <-- لا تحفظ مباشرة
            application.job = job  # <-- ربط الوظيفة
            application.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = ApplicationForm()

    return render(request, 'job/job_details.html', {'job': job,'form':form})

@login_required
def add_job(request):
    if(request.method == 'POST'):
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.owner = request.user
            job.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()
    return render(request, 'job/add_job.html',{'form':form})