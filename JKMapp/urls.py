from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('index/', views.index, name="index"),
    path('students/', views.student_list, name='student_list'),
    path('register/', views.register, name='register'),
    path('update_personal_details/', views.update_personal_details, name="update_personal_details"),
    path("personal_details/", views.personal_details, name="personal_details"),
    path('login/', views.custom_login, name='login'),
]
