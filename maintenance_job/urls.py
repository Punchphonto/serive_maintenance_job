"""
URL configuration for maintenance_job project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job_maintenance import views
from job_maintenance.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobrequest_create', JobrequestCreateView.as_view(), name='jobrequest-create'),
    path('jobrequest_update/<int:pk>', JobrequestUpdateView.as_view(), name='jobrequest-update'),
    path('jobrequest/', JobrequestListView.as_view(), name='jobrequest-list'),
    path('jobrequest/<int:pk>', JobrequestRetrieveView.as_view(), name='jobrequest-detail'),
    path('get_job_stats/', GetJpobStatusListView.as_view(), name='jostatus-detail'),
    path('get_place/', GetPlaceListView.as_view()),
    path('get_person/', RsponsiblePersonListView.as_view()),
]
