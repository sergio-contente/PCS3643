from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime

from django import forms
from django.forms import DateTimeInput

CHOICES= [
    ('1', 'Relatório de um vôo'),
    ('2', 'Relatórios de um dia'),
    ]

class MyDateInput(forms.widgets.DateInput):
    input_type = 'date'


class RelatorioForms(forms.Form):

    choice= forms.CharField(label='Escolha o tipo de relatório a ser gerado', widget=forms.Select(choices=CHOICES))
    codigo_voo = forms.CharField(widget=MyDateInput())
    final_date = forms.DateField(widget=MyDateInput())

    def reset_date(self):
        initial_date = self.data['initial_date']
        final_date = self.data['final_date']

        # Check if a date is in the allowed range (+4 weeks from today).

        if initial_date > datetime.date.today():
            raise ValidationError(_('Data inicial maior que a atual!'))

        if final_date > datetime.date.today():
            raise ValidationError(_('Data final maior que a atual!'))

        if initial_date >= final_date:
            raise ValidationError(_('Data inicial maior que a fina!'))

        # Remember to always return the cleaned data.
        return 0


ROTAS= [
    ('1', 'Rota 1'),
    ('2', 'Rota 2'),
    ('3', 'Rota 3'),
    ('4', 'Rota 4'),
    ]
# template (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)

class CreateVoo(forms.Form):
    numero_do_voo_de_partida = forms.CharField(max_length = 200)
    numero_do_voo_de_chegada = forms.CharField(max_length = 200)
    companhia_aerea = forms.CharField(max_length = 200)
    rota= forms.CharField(label='Rota do voo:', widget=forms.Select(choices=ROTAS))
    local_de_partida = forms.CharField(max_length = 200)
    local_de_destino = forms.CharField(max_length = 200)
    previsao_de_partida = forms.CharField(max_length = 200)
    previsao_de_chegada = forms.CharField(max_length = 200)

class UpdateVoo(forms.Form):
    id_num_partida = forms.CharField(max_length = 200)
    id_num_chegada = forms.CharField(max_length = 200)
    companhia_aerea = forms.CharField(max_length = 200)
    rota= forms.CharField(label='Rota do voo:', widget=forms.Select(choices=ROTAS))
    local_de_partida = forms.CharField(max_length = 200)
    local_de_destino = forms.CharField(max_length = 200)
    previsao_de_partida = forms.CharField(max_length = 200)
    previsao_de_chegada = forms.CharField(max_length = 200)

class testForm(forms.Form):
    dummyText = forms.CharField(help_text="Enter text")
