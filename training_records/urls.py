from django.urls import path
from . import views


app_name = 'training_records'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
]