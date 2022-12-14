from django import forms
from django.forms import ModelForm, TextInput, PasswordInput
from django.core.validators import RegexValidator
from FlightApp.utils import *
from FlightApp.models import User

flightCodeValidator = RegexValidator(
    r"^[A-Z]{3}\d{4}$", "Formato do código de voo incorreto"
)


# class AbstractUser(forms.Form):
#     username = forms.CharField(required=True, label=False)
#     password = forms.CharField(required=True, label=False)


class RegisterFlightForm(forms.Form):
    flightCode = forms.CharField(
        label="Código de Voo",
        validators=[flightCodeValidator],
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Código de Voo",
            }
        ),
    )
    airline = forms.ChoiceField(
        label="Linha Aérea",
        choices=airlines,
        widget=forms.Select(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Linha Aérea",
            }
        ),
    )
    departureAirport = forms.ChoiceField(
        choices=airports,
        label="Aeroporto de Saída",
        widget=forms.Select(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Aeroporto de Saída",
            }
        ),
    )
    destinationAirport = forms.ChoiceField(
        choices=airports,
        label="Aeroporto de Partida",
        widget=forms.Select(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Aeroporto de Partida",
            }
        ),
    )
    departureTime = forms.DateTimeField(
        label="Partida Prevista",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Partida Prevista",
            }
        ),
    )
    arrivalTime = forms.DateTimeField(
        label="Chegada Prevista",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Chegada Prevista",
            }
        ),
    )


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
    airline = forms.CharField(
        label="Linha Aérea",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Linha Aérea",
            }
        ),
    )
    departureAirport = forms.ChoiceField(
        choices=airports,
        label="Aeroporto de Saída",
        widget=forms.Select(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Aerorporto de Partida",
            }
        ),
    )
    
    destinationAirport = forms.ChoiceField(
        choices=airports,
        label="Aeroporto de Partida",
         widget=forms.Select(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Aeroporto de Destino",
            }
        ),
    )

    estDepartureTime = forms.DateTimeField(
        label="Partida Prevista",
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example4",
                "placeholder": "Chegada Real",
            }
        ),
    )
    estArrivalTime = forms.DateTimeField(
        label="Chegada Prevista",
        widget=forms.DateTimeInput(attrs={
            "class": "form-control form-control-lg",
            "id": "form3example4",
            "placeholder": "Chegada Real",
        }
        ),
    )


class pilotForm(forms.Form):
    realDepartureTime = forms.DateTimeField(
        required=False,
        label=False,
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Partida Real",
            }
        ),
    )
    realArrivalTime = forms.DateTimeField(
        required=False,
        label=False,
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example4",
                "placeholder": "Chegada Real",
            }
        ),
    )


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


# class UserForm(forms.ModelForm):
#     password = forms.CharField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ["password"]


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example3",
                "placeholder": "Usuário",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "form3example4",
                "placeholder": "Senha",
            }
        )
    )
