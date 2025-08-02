from django.urls import path
from .views import apply_for_course

urlpatterns = [
    path('apply/', apply_for_course, name='apply_for_course'),
]
