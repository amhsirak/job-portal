from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Application

def application(request):
    if request.method == 'POST':
        job_id = request.POST['job_id']
        job = request.POST['job']
        creator = request.POST['creator']
        creator_id = request.POST['creator_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        resume = request.FILES['resume']
        user_id = request.POST['user_id']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Application.objects.all().filter(job_id=job_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already applied for this job')
                return redirect('/jobs/'+job_id)    

        apply = Application(job=job, job_id=job_id,creator=creator,creator_id=creator_id, name=name, email=email, phone=phone,resume=resume, user_id=user_id)

        apply.save()


        messages.success(request, 'Your application has been submitted')
        return redirect('/jobs/'+ job_id)
