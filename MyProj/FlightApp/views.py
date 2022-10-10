from django.shortcuts import render

# Create your views here.
def main_flight(request):
	return render(request, "main_flight.html")
