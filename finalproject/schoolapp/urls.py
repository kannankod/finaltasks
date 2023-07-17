
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('formland/', views.formland, name='formland'),
    path('forms/', views.forms, name='forms'),
    path('department/<str:dept>/', views.department_wikipedia, name='department_wikipedia'),
    path('get_courses/', views.get_courses, name='get_courses'),
]