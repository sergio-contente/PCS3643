from django.db import models
import uuid
from FlightApp.utils import *

# Create your models here.


class HorarioReal(models.Model):
    id_real = models.UUIDField(primary_key=True, default=uuid.uuid4)
    partida_real = models.DateTimeField(null=True, default=None)
    chegada_real = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = "horarios_reais"


class Rota(models.Model):
    id_rota = models.UUIDField(primary_key=True, default=uuid.uuid4)
    aeroporto_destino = models.CharField(max_length=3, null=False)
    aeroporto_saida = models.CharField(max_length=3, null=False)

    class Meta:
        db_table = "rotas"


class Status(models.Model):
    id_status = models.UUIDField(primary_key=True, default=uuid.uuid4)
    status_voo = models.CharField(max_length=20, null=False, default=flightStatus[0][1])

    class Meta:
        db_table = "status"


class HorarioPrevisto(models.Model):
    id_previsao = models.UUIDField(primary_key=True, default=uuid.uuid4)
    partida_prevista = models.DateTimeField(null=False)
    chegada_prevista = models.DateTimeField(null=False)

    class Meta:
        db_table = "horarios_previstos"


class Voo(models.Model):
    codigo_voo = models.CharField(primary_key=True, max_length=20)
    companhia_aerea = models.CharField(max_length=10, null=False)
    estado = models.ForeignKey(Status, on_delete=models.CASCADE)
    rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
    previsao = models.ForeignKey(HorarioPrevisto, on_delete=models.CASCADE)
    real = models.ForeignKey(HorarioReal, on_delete=models.CASCADE)

    class Meta:
        db_table = "voos"


class Relatorio(models.Model):
    id_relatorio = models.UUIDField(primary_key=True)
    codigo_voo = models.ForeignKey(Voo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, null=False)
    tempo_real_atraso = models.DateTimeField(null=False)
    data_geracao = models.DateTimeField(null=False)

    class Meta:
        db_table = "relatorios"


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=20, null=False)
    password = models.CharField(max_length=100, null=False)
    isLocked = models.BooleanField(default=False)
    counter = models.IntegerField(default=3)
    profession = models.CharField(
        choices=roles, max_length=20, null=False, default=roles[3]
    )

    class Meta:
        db_table = "users"
