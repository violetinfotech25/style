from django.db import models

class CourseApplication(models.Model):
    COURSE_CHOICES = [
        ('medical', 'HAE-DNA-846, HAE-DNA-847'),
        ('engineering', 'HAE-DHNM-846, HAE-DHNM-847'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    message = models.TextField()
    marksheet = models.FileField(upload_to='uploads/marksheets/', blank=True, null=True)
    aadhar = models.FileField(upload_to='uploads/aadhar/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

