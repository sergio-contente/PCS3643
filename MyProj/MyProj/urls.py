"""MyProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from FlightApp import views

app_name = "flightApp"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ListaVoos/", views.ListaVoos),
    path("ListaVoos/Chegadas", views.ListaVoosChegadas),
    path("ListaVoos/delete/<str:codigo>", views.deleteFlight, name="deleteFlight"),
    path("CadastrarVoo/", views.CadastrarVoo),
    path("AtualizarVoo/<str:code>/<str:role>", views.AtualizarVoo),
    path("GerarRelatorioVoo/<str:code>", views.generateSingleReport),
    path("GerarRelatorioDia/<str:day>", views.generateDailyReport),
    path("MonitorarVoo/<str:code>", views.MonitorarVoo, name="manageFlight"),
    path("", views.Login, name="Login"),
    path("Login/", views.Login),
    path("Logout/", views.Logout),
    path(
        "MonitorarVoo/<str:code>/UpdateStatus/<str:status>/<str:role>",
        views.updateStatus,
    ),
    path(
        "MonitorarVoo/<str:code>/cancel/",
        views.cancelFlight,
    ),
]
