from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail,EmailMessage

# Create your views here.
def SendEmail(request):

    if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       mobileno = request.POST.get('mobileno')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       ctx = {
           'name' : name,
           'email' : email,
           'mobileno' : mobileno,
           'subject' : subject,
           'message' : message
       }

       message = render_to_string('myapp/mail.html', ctx)
       
       send_mail('Contact Form Enquiry',
        message,
        settings.EMAIL_HOST_USER,
        ['gopalsrinivas.b@gmail.com'],
        fail_silently=False, html_message=message)

    return render(request,'myapp/sendEmail.html')

