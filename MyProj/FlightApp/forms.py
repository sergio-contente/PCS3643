from django import forms
from django.core.validators import RegexValidator
from FlightApp.utils import *
from FlightApp.models import User

flightCodeValidator = RegexValidator(
    r"^[A-Z]{3}\d{4}$", "Formato do código de voo incorreto"
)


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(label="senha", required=True)


class RegisterFlightForm(forms.Form):
    flightCode = forms.CharField(
        label="Código de Voo", validators=[flightCodeValidator]
    )
    airline = forms.ChoiceField(label="Linha Aérea", choices=airlines)
    departureAirport = forms.ChoiceField(choices=airports, label="Aeroporto de Saída")
    destinationAirport = forms.ChoiceField(
        choices=airports, label="Aeroporto de Partida"
    )
    departureTime = forms.DateTimeField(label="Partida Prevista")
    arrivalTime = forms.DateTimeField(label="Chegada Prevista")


class generalForm(forms.Form):
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


class operatorForm(forms.Form):
    airline = forms.CharField(label="Linha Aérea")
    departureAirport = forms.ChoiceField(choices=airports, label="Aeroporto de Saída")
    destinationAirport = forms.ChoiceField(
        choices=airports, label="Aeroporto de Partida"
    )
    estDepartureTime = forms.DateTimeField(label="Partida Prevista")
    estArrivalTime = forms.DateTimeField(label="Chegada Prevista")


class pilotForm(forms.Form):
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
