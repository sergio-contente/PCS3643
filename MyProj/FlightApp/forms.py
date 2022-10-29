from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegisterFlightForm(forms.Form):
    flightCode = forms.CharField()
    departureTime = forms.DateTimeField()
    arrivalTime = forms.DateTimeField()
    route = forms.ChoiceField()

    class Meta:
        # model = User
        fields = ('username', 'password')
