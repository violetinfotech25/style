from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import CourseApplicationForm


def home(request):
    return render(request, 'main/index.html')  # This will look for a template named home.html

def gallery(request):
    return render(request, 'main/gallery.html')

def course(request):
    return render(request, 'main/course.html')

def course1(request):
    return render(request, 'main/hae-dna-846.html')

def course2(request):
    return render(request, 'main/hae-dhnm-847.html')

def contact(request):
    return render(request, 'main/contact.html')

def apply(request):
    if request.method == 'POST':
        form = CourseApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()

            # Email setup
            subject = f"New Course Application from {application.name}"
            message = (
                f"Name: {application.name}\n"
                f"Email: {application.email}\n"
                f"Address: {application.address}\n"
                f"Contact: {application.contact}\n"
                f"Course: {application.course}\n"
                f"Message:\n{application.message}\n"
            )

            try:
                email = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=["jossubi1429@gmail.com"],
                )

                if application.marksheet:
                    email.attach_file(application.marksheet.path)
                if application.aadhar:
                    email.attach_file(application.aadhar.path)

                email.send()
                messages.success(request, "✅ Application submitted successfully!")
            except Exception as e:
                messages.warning(request, "⚠️ Application saved, but email failed to send.")
                print("Email sending error:", e)
        else:
            print("Form is not valid:")
            print(form.errors)  # DEBUG THIS

    return render(request, 'main/apply.html', {'form': CourseApplicationForm()})