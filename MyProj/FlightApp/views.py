from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from FlightApp.forms import *
from FlightApp.models import *
from FlightApp.utils import airports
from FlightApp.forms import LoginForm


# Create your views here.


def ListaVoos(request):
    if request.method == "GET":
        flights = Voo.objects.all()

        return render(request, "ListaVoos.html", {"flights": flights, "currFlight": ""})
    elif request.method == "POST":
        print("test")


def deleteFlight(request, codigo):
    flight = Voo.objects.get(codigo_voo=codigo)
    flight.delete()
    return HttpResponseRedirect("/ListaVoos/")


def generateDailyReport(request, day: str):
    print("><><>", day)
    flights = Voo.objects.filter(
        previsao=HorarioPrevisto.objects.filter(partida_prevista=day)
    )
    return render(request, "GerarRelatorios.html", {"flights": flights})


def generateSingleReport(request, code: str):
    flight = Voo.objects.get(codigo_voo=code)
    return render(request, "GerarRelatorios.html", {"flights": flight})


def CadastrarVoo(request):
    if request.method == "POST":
        form = RegisterFlightForm(request.POST)
        if form.is_valid():
            newFlightInfo = form.cleaned_data
            Voo.objects.create(
                codigo_voo=newFlightInfo["flightCode"],
                companhia_aerea=newFlightInfo["airline"],
                estado=Status.objects.create(),
                rota=Rota.objects.create(
                    aeroporto_destino=newFlightInfo["destinationAirport"],
                    aeroporto_saida=newFlightInfo["departureAirport"],
                ),
                previsao=HorarioPrevisto.objects.create(
                    partida_prevista=newFlightInfo["departureTime"],
                    chegada_prevista=newFlightInfo["arrivalTime"],
                ),
                real=HorarioReal.objects.create(),
            )
            messages.success(request, "Voo cadastrado com sucesso!")
            return HttpResponseRedirect("/CadastrarVoo/")
    else:
        form = RegisterFlightForm()
        return render(request, "CadastrarVoo.html", {"form": form})
        return HttpResponseRedirect("/ListaVoos/")


def AtualizarVoo(request, code: str):
    flight: Voo = Voo.objects.get(codigo_voo=code)
    if request.method == "POST":
        form = updateFlightForm(request.POST)
        if form.is_valid():
            print("hier")
            flight.companhia_aerea = form.cleaned_data["airline"]
            flight.estado.status_voo = flightStatus[
                int(form.cleaned_data["status"]) - 1
            ][1]
            flight.estado.save()
            flight.rota.aeroporto_saida = airports[
                int(form.cleaned_data["departureAirport"]) - 1
            ][1]
            flight.rota.aeroporto_destino = airports[
                int(form.cleaned_data["destinationAirport"]) - 1
            ][1]
            flight.rota.save()
            flight.previsao.partida_prevista = form.cleaned_data["estDepartureTime"]
            flight.previsao.chegada_prevista = form.cleaned_data["estArrivalTime"]
            flight.previsao.save()
            flight.real.partida_real = form.cleaned_data["realDepartureTime"]
            flight.real.chegada_real = form.cleaned_data["realArrivalTime"]
            flight.real.save()
            flight.save()
            return HttpResponseRedirect("/MonitorarVoo/" + flight.codigo_voo)
        else:
            print("NOT HIERRRRRR")
        #     messages.warning(
        #         request, f"Login inválido. Número de tentativas restantes: {3 - tentativas}")
        #     return HttpResponseRedirect('/MonitorarVoo/'+flight.codigo_voo)
    else:
        form = updateFlightForm(
            initial={
                "status": flight.estado.status_voo,
                "airline": flight.companhia_aerea,
                "departureAirport": flight.rota.aeroporto_saida,
                "destinationAirport": flight.rota.aeroporto_destino,
                "estDepartureTime": flight.previsao.partida_prevista,
                "estArrivalTime": flight.previsao.chegada_prevista,
                "realDepartureTime": flight.real.partida_real,
                "realArrivalTime": flight.real.chegada_real,
            }
        )
        return render(request, "AtualizarVoo.html", {"form": form, "flight": flight})


def MonitorarVoo(request, code):
    flight = Voo.objects.get(codigo_voo=code)
    return render(request, "MonitorarVoo.html", {"flight": flight})


def Login(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["username"]).exists():
                currUser = User.objects.get(username=form.cleaned_data["username"])
            else:
                messages.error(
                    request,
                    "Combinação usuário senha incorreta.",
                )
                return HttpResponseRedirect("/")

            if currUser.counter == 1:
                messages.error(
                    request,
                    "Número de tentativas ultrapassado. Acesso bloqueado. Contate um administrador.",
                )
                return HttpResponseRedirect("/")
            # process the data in form.cleaned_data as required
            if form.cleaned_data["password"] == currUser.password:
                currUser.counter = 3
                currUser.save()
                return HttpResponseRedirect("/ListaVoos/")
            else:
                currUser.counter -= 1
                currUser.save()
                messages.warning(
                    request,
                    f"Login inválido. Número de tentativas restantes: {currUser.counter}",
                )
                return HttpResponseRedirect("/")
            # ...
            # redirect to a new URL:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        return render(request, "Login.html", {"form": form})
