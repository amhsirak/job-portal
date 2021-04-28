from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from .choices import location_choices, contract_choices
from .models import Job 
from django.http import HttpResponse

def index(request):
    jobs = Job.objects.order_by('-job_date').filter(is_published = True) # Fetching data from db

    paginator = Paginator(jobs,3) # Show 3 listings per page
    page_number = request.GET.get('page')
    paged_jobs = paginator.get_page(page_number)

    context = {
        'jobs': paged_jobs
    }
    return render (request , 'jobs/jobs.html', context)


def job(request,job_id):
     #If user searches for an invalid listing , display a 404 error page

    job = get_object_or_404(Job , pk=job_id)

    context = {
        'job': job
    }

    return render (request , 'jobs/job.html',context)

def search(request):
    job_list = Job.objects.order_by('-job_date')


    if 'role' in request.GET:
        role = request.GET['role']
        if role:
            job_list = job_list.filter(role__icontains = role)


    if 'location' in request.GET:
        location = request.GET['location']
        if location:
           job_list = job_list.filter(location__iexact = location)
     

    if 'contract' in request.GET:
        contract = request.GET['contract']
        if contract:
            job_list = job_list.filter(contract__iexact = contract)


    context = {
        'location_choices': location_choices,
        'contract_choices': contract_choices,
        'jobs': job_list,
        'values': request.GET # preserving form inputs 

    }
    return render (request , 'jobs/search.html',context)

    
def applyjob(request,job_id):
    job = get_object_or_404(Job , pk=job_id)

    context = {
        'job': job
    }
    return render(request,'jobs/applyjob.html',context)