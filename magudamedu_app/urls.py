from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # maps root URL of the app to `home` view
    path('gallery/', views.gallery, name='gallery'),
    path('course/', views.course, name='course'),
    path('hea-dna-846/', views.course1, name='course1'),
    path('hae-dhnm-847/', views.course2, name='course2'),
    path('contact/', views.contact, name='contact'),
    path('apply/', views.apply, name='apply'),
]
