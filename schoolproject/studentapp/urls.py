from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
    path('add', views.add_student, name="add_student"),
    path("list", views.student_list, name='student_list'),
    path('student/<str:slug>/', views.view_student, name='view_student'),
    path('edit/<str:slug>/', views.edit_student, name='edit_student'),
    path('delete/<str:slug>/', views.delete_student, name='delete_student'),

  

]+  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)