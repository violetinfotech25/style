from django import forms
from .models import CourseApplication

class CourseApplicationForm(forms.ModelForm):
    class Meta:
        model = CourseApplication
        fields = '__all__'
