from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/create/', views.student_create, name='student_create'),
    path('grade/<int:pk>/edit/', views.grade_edit, name='grade_form'),
]