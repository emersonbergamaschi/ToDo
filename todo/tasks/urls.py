from django.urls import path
from . import views


urlpatterns = [
    path('helloworld/', views.helloword),
    path('', views.tasklist, name='task-list'),
    path('task/<int:id>', views.taskview, name='task-view'),
    path('yourname/<str:name>', views.yourname, name='your-name')
]
