from django.shortcuts import render

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
	return render(request, "Login.html")