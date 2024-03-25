from django.urls import path 
from django.contrib.auth import views as auth_views 
from .views import task, detail, create_task, update_task, delete_task, register

app_name = 'todo'
urlpatterns = [
    path('', task, name="task"),
    path('task/<int:pk>', detail, name='detail'),
    #add
    path('task/create', create_task, name='create-task'),
    #update
    path('task/<int:pk>/update', update_task, name='update-task'),
    #delete
    path('task/<int:pk>/delete', delete_task, name='delete-task'),
    # register
    path('register/', register, name="register"),
    #login
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    #logout
    path('logout/', auth_views.LogoutView.as_view(template_name='todo/logout.html'), name='logout'),
]
