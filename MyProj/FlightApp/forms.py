from django import forms

airports = (
    ("1", "RIO"),
    ("2", "GRU"),
    ("3", "AMAZONIA"),
    ("4", "CHINA")
)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegisterFlightForm(forms.Form):
    flightCode = forms.CharField()
    airline = forms.CharField()
    state = "estacionado"
    route = forms.ChoiceField(choices=airports)
    departureTime = forms.DateTimeField()
    arrivalTime = forms.DateTimeField()

    class Meta:
        # model = User
        fields = ('código', 'password', 'password', 'password', 'password', 'password')
