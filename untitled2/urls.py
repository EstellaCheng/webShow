"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from untitled2 import views
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('first', views.judge, name="judge"),
    path('getex', views.getex, name="getex"),
    path('send', views.send, name="send"),
    path('entity', views.entity, name="entity"),
    path('getchou', views.getchou, name="getchou"),
    path('sendchou', views.sendchou, name="sendchou"),
    path('concept', views.concept, name="concept"),
    path('getconcept', views.getconcept, name="getconcept"),
    path('sendconcept1', views.sendconcept1, name="sendconcept1"),
    path('sendconcept2', views.sendconcept2, name="sendconcept2"),
    path('sendconcept3', views.sendconcept3, name="sendconcept3")
]

