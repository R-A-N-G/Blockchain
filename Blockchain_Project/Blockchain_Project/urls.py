"""Blockchain_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Blockchain_App import views
from Blockchain_App.views import test , full_chain, new_transcations, mine, register_node, P_2_P, consensus, login, chain, dec_chain

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test, name="test"),
    path('chain/', views.chain, name="chain"),
    path('dec_chain/', views.dec_chain, name="dec_chain"),
    path('fullchain/', views.full_chain, name="full_chain"),
    path('node/register', views.register_node, name="register_node"),
    path('transaction/new', views.new_transcations, name="new_transcations"),
    path('mine/', views.mine, name="mine"),
    path('nodes/resolve', views.consensus, name="consensus"),
    path('p2p/', views.P_2_P, name="p2p"),
    
]
login()
