from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from FlightApp.forms import *
from FlightApp.models import *
from FlightApp.utils import airports
from FlightApp.forms import LoginForm

# Create your views here.
global tentativas
tentativas = 0


def ListaVoos(request):
    if request.method == "GET":
        flights = Voo.objects.all()
        for flight in flights:
            fixFlightAirportInfo(flight)

        return render(request, "ListaVoos.html", {'flights': flights, 'currFlight': ""})


def fixFlightAirportInfo(flight: Voo):
    flight.rota.aeroporto_destino = airports[int(
        flight.rota.aeroporto_destino) - 1][1]
    flight.rota.aeroporto_saida = airports[int(
        flight.rota.aeroporto_saida) - 1][1]


def deleteFlight(request, codigo):
    flight = Voo.objects.get(codigo_voo=codigo)
    flight.delete()
    return HttpResponseRedirect("/ListaVoos/")


def GerarRelatorios(request):
    return render(request, "GerarRelatorios.html")


def CadastrarVoo(request):
    if request.method == 'POST':
        form = RegisterFlightForm(request.POST)
        if form.is_valid():
            newFlightInfo = form.cleaned_data
            Voo.objects.create(codigo_voo=newFlightInfo["flightCode"],
                               companhia_aerea=newFlightInfo["airline"],
                               estado=Status.objects.create(),
                               rota=Rota.objects.create(
                aeroporto_destino=newFlightInfo["destinationAirport"], aeroporto_saida=newFlightInfo["departureAirport"]),
                previsao=HorarioPrevisto.objects.create(
                                   partida_prevista=newFlightInfo["departureTime"],
                                   chegada_prevista=newFlightInfo["arrivalTime"]),
                real=HorarioReal.objects.create()
            )
            messages.success(request, "Voo cadastrado com sucesso!")
            return HttpResponseRedirect('/CadastrarVoo/')
    else:
        form = RegisterFlightForm()
        return render(request, "CadastrarVoo.html", {"form": form})
        return HttpResponseRedirect('/ListaVoos/')


def AtualizarVoo(request):
    return render(request, "AtualizarVoo.html")


def MonitorarVoo(request, code):
    flight = Voo.objects.get(codigo_voo=code)
    fixFlightAirportInfo(flight)
    return render(request, "MonitorarVoo.html", {"flight": flight})


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
            messages.error(
                request, "Número de tentativas ultrapassado. Acesso bloqueado.")
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
                messages.warning(
                    request, f"Login inválido. Número de tentativas restantes: {3 - tentativas}")
                return HttpResponseRedirect('/')
            # ...
            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        return render(request, "Login.html", {"form": form})
