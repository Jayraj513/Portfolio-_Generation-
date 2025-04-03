from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # User registration form
    path('success/', views.success, name='success'),  # Success page after form submission
    path('', views.form, name='form'),  # Homepage (optional)
]
