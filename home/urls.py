from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('add/', views.student_add, name='student_add'), 
]