"""
URL configuration for ClubManagement project.

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
from home import views
urlpatterns = [
    path("", views.index,name='index'),
    path("login", views.signin,name='signin'),
    path("logout", views.signout,name='signout'),
    path("contact", views.contact,name='contact'),
    path("about", views.about,name='about'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("clubmembers",views.clubmembers,name='clubmembers'),
    path("addmembers",views.addmembers,name='addmembers'),
    path("eventslist",views.eventslist,name='eventslist'),
    path("addevents",views.addevents,name='addevents'),
    path("clubtimeline",views.clubtimeline,name='clubtimeline'),
    path("requestOd",views.requestOnDuty,name='requestOd'),
    path("approval",views.approve,name='approval'),
    path('approval/<int:request_id>/', views.approve, name='approval'),
    path('approvalstatus/<int:request_id>/', views.approvalStatus, name='approvalstatus'),
    path('approvalstatus', views.approvalStatus, name='approvalstatus'),
    path("changepassword", views.changePassword,name='changepassword'),
    path("profile", views.profile,name='profile'),
    path("addclub", views.addUser,name='adduser'),
]
