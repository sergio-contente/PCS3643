import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from FlightApp.forms import *
from FlightApp.models import *
from FlightApp.utils import airports
from FlightApp.forms import LoginForm
import json


# Create your views here.


def ListaVoosChegadas(request):
    role = request.COOKIES.get("user")
    if role is None:
        return HttpResponseRedirect("/")
    if request.method == "GET":
        flights = Voo.objects.all()

        if role == "pilot":
            role = "Piloto"
        elif role == "manager":
            role = "Gerente"
        elif role == "employee":
            role = "Funcionário"
        elif role == "operator":
            role = "Operador"

        print(flights)

        return render(
            request, "ListaVoos-Chegadas.html", {"flights": flights, "role": role}
        )


def ListaVoos(request):
    role = request.COOKIES.get("user")
    if role is None:
        return HttpResponseRedirect("/")
    if request.method == "GET":
        flights = Voo.objects.all()

        if role == "pilot":
            role = "Piloto"
        elif role == "manager":
            role = "Gerente"
        elif role == "employee":
            role = "Funcionário"
        elif role == "operator":
            role = "Operador"

        print(flights)

        return render(request, "ListaVoos.html", {"flights": flights, "role": role})


def deleteFlight(request, codigo):
    flight = Voo.objects.get(codigo_voo=codigo)
    flight.delete()
    return HttpResponseRedirect("/ListaVoos/")


def generateDailyReport(request, day: str):
    print("><><>", day)
    allFlights = Voo.objects.all()
    flights = []
    for flight in allFlights:
        if flight.previsao.partida_prevista.strftime("%Y-%m-%d") == day:
            flights.append(flight)

    return render(request, "GerarRelatorios.html", {"flights": flights})


def generateSingleReport(request, code: str):
    flight = Voo.objects.get(codigo_voo=code)
    return render(request, "GerarRelatorios.html", {"flights": flight})


def CadastrarVoo(request):
    user = request.COOKIES.get("user")
    if user is None:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = RegisterFlightForm(request.POST)
        if form.is_valid():
            newFlightInfo = form.cleaned_data
            try:
                date_checker = datetime.datetime.strptime(
                    str(newFlightInfo["departureTime"]), "%Y-%m-%d %H:%M" + ":00+00:00"
                )
            except:
                messages.error(
                    request,
                    "Formato de data de partida incorreto. O formato correto é: YY-MM-DD HH:MM",
                )
                return HttpResponseRedirect("/CadastrarVoo/")
            else:
                try:
                    date_checker = datetime.datetime.strptime(
                        str(newFlightInfo["arrivalTime"]),
                        "%Y-%m-%d %H:%M" + ":00+00:00",
                    )
                except:
                    messages.error(
                        request,
                        "Formato de data de chegada incorreto. O formato correto é: YY-MM-DD HH:MM",
                    )
                    return HttpResponseRedirect("/CadastrarVoo/")
                else:
                    try:
                        time_partida = newFlightInfo["departureTime"]
                        time_chegada = newFlightInfo["arrivalTime"]
                        if time_partida >= time_chegada:
                            raise TypeError(
                                "Horario de partida é maior ou igual que o de chegada."
                            )
                    except:
                        messages.error(
                            request,
                            "Horario de partida é maior ou igual que o de chegada.",
                        )
                        return HttpResponseRedirect("/CadastrarVoo/")
                    else:
                        try:
                            if (
                                newFlightInfo["destinationAirport"]
                                == newFlightInfo["departureAirport"]
                            ):
                                raise TypeError(
                                    "Aeroporto de saída é o mesmo que o de destino"
                                )
                        except:
                            messages.error(
                                request,
                                "Aeroporto de saída é o mesmo que o de destino",
                            )
                            return HttpResponseRedirect("/CadastrarVoo/")
                        else:
                            Voo.objects.create(
                                codigo_voo=newFlightInfo["flightCode"],
                                companhia_aerea=newFlightInfo["airline"],
                                estado=Status.objects.create(),
                                rota=Rota.objects.create(
                                    aeroporto_destino=airports[
                                        int(newFlightInfo["destinationAirport"]) - 1
                                    ][1],
                                    aeroporto_saida=airports[
                                        int(newFlightInfo["departureAirport"]) - 1
                                    ][1],
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
            newFlightInfo = form.cleaned_data
            print(str(newFlightInfo["departureTime"]))
            try:
                date_checker = datetime.datetime.strptime(
                    str(newFlightInfo["departureTime"]), "%Y-%m-%d %H:%M" + ":00+00:00"
                )
            except:
                messages.error(
                    request,
                    "Formato de data de partida incorreto",
                )
            else:
                # newFlightInfo = form.cleaned_data
                print(form.errors.as_data())
                messages.error(
                    request,
                    "Formato de data(s) incorreto)(s)",
                )
            return HttpResponseRedirect("/CadastrarVoo/")
    else:
        form = RegisterFlightForm()
        return render(request, "CadastrarVoo.html", {"form": form})


def AtualizarVoo(request, code: str, role):
    user: User = request.COOKIES.get("user")
    if user is None:
        return HttpResponseRedirect("/")

    flight: Voo = Voo.objects.get(codigo_voo=code)
    if request.method == "POST":

        form = operatorForm(request.POST)

        if form.is_valid():
            newFlightInfo = form.cleaned_data
            print("===========================")
            print(newFlightInfo)
            if role == "operator":
                try:
                    date_checker = datetime.datetime.strptime(
                        str(newFlightInfo["estDepartureTime"]),
                        "%Y-%m-%d %H:%M" + ":00+00:00",
                    )
                except:
                    messages.error(
                        request,
                        "Formato de data de partida incorreto. O formato correto é: YY-MM-DD HH:MM",
                    )
                    return HttpResponseRedirect(
                        "/AtualizarVoo/" + flight.codigo_voo + "/" + role
                    )
                else:
                    try:
                        date_checker = datetime.datetime.strptime(
                            str(newFlightInfo["estArrivalTime"]),
                            "%Y-%m-%d %H:%M" + ":00+00:00",
                        )
                    except:
                        messages.error(
                            request,
                            "Formato de data de chegada incorreto. O formato correto é: YY-MM-DD HH:MM",
                        )
                        return HttpResponseRedirect(
                            "/AtualizarVoo/" + flight.codigo_voo + "/" + role
                        )
                    else:
                        try:
                            time_partida = newFlightInfo["estDepartureTime"]
                            time_chegada = newFlightInfo["estArrivalTime"]
                            if time_partida >= time_chegada:
                                raise TypeError(
                                    "Horario de partida é maior ou igual que o de chegada."
                                )
                        except:
                            messages.error(
                                request,
                                "Horario de partida é maior ou igual que o de chegada.",
                            )
                            return HttpResponseRedirect(
                                "/AtualizarVoo/" + flight.codigo_voo + "/" + role
                            )
                        else:
                            try:
                                if (
                                    newFlightInfo["destinationAirport"]
                                    == newFlightInfo["departureAirport"]
                                ):
                                    raise TypeError(
                                        "Aeroporto de saída é o mesmo que o de destino"
                                    )
                            except:
                                messages.error(
                                    request,
                                    "Aeroporto de saída é o mesmo que o de destino",
                                )
                                return HttpResponseRedirect(
                                    "/AtualizarVoo/" + flight.codigo_voo + "/" + role
                                )
                            else:
                                flight.companhia_aerea = form.cleaned_data["airline"]
                                flight.rota.aeroporto_saida = airports[
                                    int(form.cleaned_data["departureAirport"]) - 1
                                ][1]
                                flight.rota.aeroporto_destino = airports[
                                    int(form.cleaned_data["destinationAirport"]) - 1
                                ][1]
                                flight.rota.save()
                                flight.previsao.partida_prevista = form.cleaned_data[
                                    "estDepartureTime"
                                ]
                                flight.previsao.chegada_prevista = form.cleaned_data[
                                    "estArrivalTime"
                                ]
                                flight.previsao.save()
                                flight.save()

                            return HttpResponseRedirect(
                                "/AtualizarVoo/" + flight.codigo_voo + "/" + role
                            )
    else:
        form = operatorForm(
            initial={
                "realDepartureTime": flight.real.partida_real,
                "realArrivalTime": flight.real.chegada_real,
            }
        )

        return render(
            request, "AtualizarVoo.html", {"form": form, "flight": flight, "user": user}
        )


def MonitorarVoo(request, code):
    role = request.COOKIES.get("user")
    if role is None:
        return HttpResponseRedirect("/")
    flight = Voo.objects.get(codigo_voo=code)
    status = flight.estado.status_voo
    if request.method == "POST":
        form = pilotForm(request.POST)
        if form.is_valid():
            newFlightInfo = form.cleaned_data
            try:
                date_checker = datetime.datetime.strptime(
                    str(newFlightInfo["realDepartureTime"]),
                    "%Y-%m-%d %H:%M" + ":00+00:00",
                )
            except:
                messages.error(
                    request,
                    "Formato de data de partida incorreto. O formato correto é: YY-MM-DD HH:MM",
                )
                return HttpResponseRedirect("/MonitorarVoo/" + flight.codigo_voo)
            else:
                try:
                    date_checker = datetime.datetime.strptime(
                        str(newFlightInfo["realArrivalTime"]),
                        "%Y-%m-%d %H:%M" + ":00+00:00",
                    )
                except:
                    messages.error(
                        request,
                        "Formato de data de chegada incorreto. O formato correto é: YY-MM-DD HH:MM",
                    )
                    return HttpResponseRedirect("/MonitorarVoo/" + flight.codigo_voo)
                else:
                    try:
                        time_partida = newFlightInfo["realDepartureTime"]
                        time_chegada = newFlightInfo["realArrivalTime"]
                        if time_partida >= time_chegada:
                            raise TypeError(
                                "Horario de partida é maior ou igual que o de chegada."
                            )

                    except:
                        messages.error(
                            request,
                            "Horario de partida é maior ou igual que o de chegada.",
                        )
                        return HttpResponseRedirect(
                            "/MonitorarVoo/" + flight.codigo_voo
                        )
                    else:
                        flight.real.partida_real = form.cleaned_data[
                            "realDepartureTime"
                        ]
                        flight.real.chegada_real = form.cleaned_data["realArrivalTime"]
                        flight.real.save()
                        print(flight.real.chegada_real - flight.real.chegada_real)
                        flight.erro = (
                            flight.real.chegada_real - flight.real.partida_real
                        ).seconds
                        flight.save()
                        return HttpResponseRedirect(
                            "/MonitorarVoo/" + flight.codigo_voo
                        )

    else:
        form = pilotForm()
        allowedPilot = ["PROGRAMADO", "EM VOO", "ATERRISSADO", "TAXIANDO", "AUTORIZADO"]
        allowedEmployee = ["EMBARCANDO", "PRONTO"]
        return render(
            request,
            "MonitorarVoo.html",
            {
                "flight": flight,
                "role": role,
                "status": status,
                "form": form,
                "allowedPilot": allowedPilot,
                "allowedEmployee": allowedEmployee,
            },
        )


def Login(request):
    user = request.COOKIES.get("user")
    if user is not None:
        return HttpResponseRedirect("/ListaVoos")
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        print("here")
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        print("surely, form")
        print(form)
        print(form.cleaned_data)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            print("opa")
            if User.objects.filter(username=form.cleaned_data["username"]).exists():
                currUser = User.objects.get(username=form.cleaned_data["username"])
            else:
                messages.error(
                    request,
                    "Combinação usuário senha incorreta.",
                )
                return HttpResponseRedirect("/")
            print("gere2")
            if currUser.profession in roles[4][1]:
                messages.error(
                    request,
                    "Usuário não autorizado",
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
                response = HttpResponseRedirect("/ListaVoos/")
                response.set_cookie("user", currUser.profession)
                return response
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


def Logout(request):
    response = HttpResponseRedirect("/")
    response.delete_cookie("user")
    return response


def updateStatus(request, code, status, role):
    flight = Voo.objects.get(codigo_voo=code)
    currIdx: int
    for idx in range(0, len(flightStatus)):
        if status == flightStatus[idx][1]:
            currIdx = idx
    newIdx = currIdx + 1
    flight.estado.status_voo = flightStatus[newIdx][1]
    flight.estado.save()
    return HttpResponseRedirect("/MonitorarVoo/" + code)
    # return render(
    #     request,
    #     "MonitorarVoo.html",
    #     {"flight": flight, "role": role, "status": status},
    # )


def cancelFlight(request, code):
    flight = Voo.objects.get(codigo_voo=code)
    flight.estado.status_voo = "CANCELADO"
    flight.estado.save()
    return HttpResponseRedirect("/MonitorarVoo/" + code)
