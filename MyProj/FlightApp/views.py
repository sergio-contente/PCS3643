from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from FlightApp.forms import *
import datetime
from FlightApp.models import *
from django.contrib import messages

from FlightApp.forms import LoginForm

# Create your views here.
global tentativas
tentativas = 0

def ListaVoos(request):
    return render(request, "ListaVoos.html")


def GerarRelatorios(request):
    return render(request, "GerarRelatorios.html")


def CadastrarVoo(request):
    if request.method == 'POST':
        form = RegisterFlightForm(request.POST)
        voo_base = {"flightCode": "", "state": "", "route": "", "departureTime": "", "arrivalTime": ""}
        if form.is_valid():
            credentials = form.cleaned_data
            messages.success(request, "Voo cadastrado com sucesso!")
            Voo.objects.create(codigo_voo = form.cleaned_data["flightCode"], 
                companhia_aerea = form.cleaned_data["airline"], estado=form.cleaned_data["state"], 
                rota=form.cleaned_data["route"], previsao=form.cleaned_data["departureTime"], real=form.cleaned_data["arrivalTime"])
            return HttpResponseRedirect('/CadastrarVoo/')
            #salvar no DB
            #mostrar msg de sucesso
    else:
        form = RegisterFlightForm()
        return render(request, "CadastrarVoo.html", {"form": form})


def AtualizarVoo(request):
    return render(request, "AtualizarVoo.html")


def MonitorarVoo(request):
    return render(request, "MonitorarVoo.html")


def Login(request):
    admin_cred = {'username': 'admin', 'password': 'admin'}
    operador = {'username': 'operador', 'password': 'operador'}
    funcionario = {'username': 'funcionario', 'password': 'funcionario'}
    global tentativas
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        if (tentativas == 3):
              messages.error(request, "Número de tentativas ultrapassado. Acesso bloqueado.")
              return HttpResponseRedirect('/')
            # check whether it's valid:
        elif form.is_valid():
            # process the data in form.cleaned_data as required
            credentials = form.cleaned_data
            if credentials == admin_cred or credentials == operador or credentials == funcionario:
                tentativas = 0
                return HttpResponseRedirect('/ListaVoos/')
            else:
                tentativas = tentativas + 1
                messages.warning(request, f"Login inválido. Número de tentativas restantes: {3 - tentativas}")
                return HttpResponseRedirect('/')
            # ...
            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        return render(request, "Login.html", {"form": form})
