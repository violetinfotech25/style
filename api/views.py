from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import CourseApplicationForm

def apply_for_course(request):
    if request.method == 'POST':
        form = CourseApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()

            # Prepare the email content
            subject = f"New Course Application from {application.name}"
            message = (
                f"Name: {application.name}\n"
                f"Email: {application.email}\n"
                f"Address: {application.address}\n"
                f"Contact: {application.contact}\n"
                f"Course: {application.course}\n"
                f"Message:\n{application.message}\n"
            )

            # Create the email message
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=None,  # Will use DEFAULT_FROM_EMAIL
                to=["magudamedu@gmail.com"],
            )

            # Attach uploaded files if available
            if application.marksheet:
                email.attach_file(application.marksheet.path)

            if application.aadhar:
                email.attach_file(application.aadhar.path)

            # Send the email
            email.send()

            return render(request, 'thank_you.html')  # Render success page
    else:
        form = CourseApplicationForm()

    return render(request, 'apply_form.html', {'form': form})
