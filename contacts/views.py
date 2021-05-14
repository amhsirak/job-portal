from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        
        contact = Contact(name=name, company=company, email=email, phone=phone, message=message, user_id=user_id )

        contact.save()

        messages.success(request, 'Your request has been submitted, we will get back to you soon!')
        return redirect('index')

