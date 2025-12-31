from django.urls import path
from . import views

urlpatterns = [
    path('', views.scholarship_list, name='scholarship_list'),
    path('recommend/<int:student_id>/', views.recommend_scholarship, name='recommend_scholarship'),
]
