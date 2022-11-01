from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render

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
    print(">>")
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if form.cleaned_data == {'username': 'admin', 'password': 'admin'}:
                return HttpResponseRedirect('/ListaVoos/')
            else:
                return HttpResponseRedirect('/')
            # ...
            # redirect to a new URL:
            return render(request, "ListaVoos.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
        return render(request, "Login.html", {"form": form})
