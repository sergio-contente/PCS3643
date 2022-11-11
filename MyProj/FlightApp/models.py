from django.db import models
ESTADOS_VOO = [
	"ESTACIONADO",
	"ATERRISSANDO",
]

# Create your models here.
class HorarioReal(models.Model):
	id_real = models.IntegerField(primary_key=True)
	partida_real = models.DateTimeField(null=True)
	chegada_real = models.DateTimeField(null=True)
	class Meta:
		db_table = 'horarios_reais'

class Rota(models.Model):
	id_rota = models.IntegerField(primary_key=True)
	aeroporto_destino = models.CharField(max_length=3, null=False)
	aeroporto_saida = models.CharField(max_length=3, null=False)
	class Meta:
			db_table = 'rotas'

class Status(models.Model):
	id_status = models.IntegerField(primary_key=True)
	status_voo = models.CharField(max_length=20, null=False)
	class Meta:
  		db_table ='status'

class HorarioPrevisto(models.Model):
	id_previsao = models.IntegerField(primary_key=True)
	partida_prevista = models.DateTimeField(null=False)
	chegada_prevista = models.DateTimeField(null=False)
	class Meta:
			db_table ='horarios_previstos'

class Voo(models.Model):
	codigo_voo = models.CharField(primary_key=True, max_length=20)
	companhia_aerea = models.CharField(max_length=10, null=False)
	estado = models.ForeignKey(Status, on_delete=models.CASCADE)
	rota = models.ForeignKey(Rota, on_delete=models.CASCADE)
	previsao = models.ForeignKey(HorarioPrevisto, on_delete=models.CASCADE)
	real = models.ForeignKey(HorarioReal, on_delete=models.CASCADE)
	class Meta:
		db_table = 'voos'

class Relatorio(models.Model):
	id_relatorio = models.IntegerField(primary_key=True)
	codigo_voo = models.ForeignKey(Voo, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=20, null=False)
	tempo_real_atraso = models.DateTimeField(null=False)
	data_geracao = models.DateTimeField(null=False)
	class Meta:
		db_table ='relatorios'
