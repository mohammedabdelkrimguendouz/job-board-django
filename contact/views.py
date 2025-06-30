from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from project import settings

def send_mssage(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if subject and email and message:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
        return redirect('contact:contact')
    return render(request, 'contact/contact.html')
