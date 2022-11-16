from django import forms
from FlightApp.utils import airports


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegisterFlightForm(forms.Form):
    flightCode = forms.CharField(label="Código de Voo")
    airline = forms.CharField(label="Linha Aérea")
    departureAirport = forms.ChoiceField(
        choices=airports, label="Aeroporto de Saída")
    destinationAirport = forms.ChoiceField(
        choices=airports, label="Aeroporto de Partida")
    departureTime = forms.DateTimeField(label="Partida Prevista")
    arrivalTime = forms.DateTimeField(label="Chegada Prevista")

    # class Meta:
    #     # model = User
    #     fields = ('código', 'password', 'password',
    #               'password', 'password', 'password')
