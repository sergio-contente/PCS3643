from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
import datetime
from django.contrib import messages

from FlightApp.forms import LoginForm

# Create your views here.


def ListaVoos(request):
    return render(request, "ListaVoos.html")


def GerarRelatorios(request):
    return render(request, "GerarRelatorios.html")


def CadastrarVoo(request):
    return render(request, "CadastrarVoo.html")


def AtualizarVoo(request):
    return render(request, "AtualizarVoo.html")


def MonitorarVoo(request):
    return render(request, "MonitorarVoo.html")


def Login(request):
    admin_cred = {'username': 'admin', 'password': 'admin'}
    operador = {'username': 'operador', 'password': 'operador'}
    funcionario = {'username': 'funcionario', 'password': 'funcionario'}
    global tentativas
    tentativas = 0
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        if (tentativas == 2):
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
                messages.warning(request, f"Login inválido. Número de tentativas restantes: {tentativas%3}")
                return HttpResponseRedirect('/')
            # ...
            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        return render(request, "Login.html", {"form": form})
