from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<int:task_id>', views.detail, name='detail'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('delete/<int:task_id>', views.delete, name='delete'),
]
