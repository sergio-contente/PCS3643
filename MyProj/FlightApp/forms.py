from django import forms
from FlightApp.utils import *
from FlightApp.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(label="senha", required=True)


class RegisterFlightForm(forms.Form):
    flightCode = forms.CharField(label="Código de Voo")
    airline = forms.CharField(label="Linha Aérea")
    departureAirport = forms.ChoiceField(choices=airports, label="Aeroporto de Saída")
    destinationAirport = forms.ChoiceField(
        choices=airports, label="Aeroporto de Partida"
    )
    departureTime = forms.DateTimeField(label="Partida Prevista")
    arrivalTime = forms.DateTimeField(label="Chegada Prevista")


class updateFlightForm(forms.Form):
    status = forms.ChoiceField(choices=flightStatus)
    airline = forms.CharField(label="Linha Aérea")
    departureAirport = forms.ChoiceField(choices=airports, label="Aeroporto de Saída")
    destinationAirport = forms.ChoiceField(
        choices=airports, label="Aeroporto de Partida"
    )
    estDepartureTime = forms.DateTimeField(label="Partida Prevista")
    estArrivalTime = forms.DateTimeField(label="Chegada Prevista")
    realDepartureTime = forms.DateTimeField(label="Partida Real", required=False)
    realArrivalTime = forms.DateTimeField(label="Chegada Real", required=False)


class DailyReportDateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=["%d/%m/%Y %H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker1",
            }
        ),
    )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["password"]
