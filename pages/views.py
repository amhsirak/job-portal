from django.shortcuts import render
from django.http import HttpResponse
from jobs.choices import contract_choices, location_choices
from jobs.models import Job

def index(request):
    jobs = Job.objects.order_by('-job_date').filter(is_published=True)[:3]

    context = {
        'jobs': jobs,
        'location_choices': location_choices,
        'contract_choices':  contract_choices
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')