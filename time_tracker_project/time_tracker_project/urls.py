"""
URL configuration for time_tracker_project project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from time_tracker_app.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),

    # User authentication
    path('register/', UserRegister.as_view(), name='register'),
	path('login/', UserLogin.as_view(), name='login'),
	path('logout/', UserLogout.as_view(), name='logout'),
	path('user/', UserView.as_view(), name='user'),

    # Get all projects or create a new project
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),

    # Get, update, or delete a specific project
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),

    # Get all time entries for a specific user or create a new time entry
    path('time-entries/', TimeEntryListAPIView.as_view(), name='time-entry-list'),

    # Get, update, or delete a specific time entry
    path('time-entries/<int:pk>/', TimeEntryDetailAPIView.as_view(), name='time-entry-detail'),
    
    # Get all task descriptions or create a new task description
    path('task-descriptions/', TaskDescriptionListAPIView.as_view(), name='task-description-list'),

    # Get, update, or delete a specific task description
    path('task-descriptions/<int:pk>/', TaskDescriptionDetailAPIView.as_view(), name='task-description-detail')
]
