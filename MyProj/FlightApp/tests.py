from django.test import TestCase
import datetime
from FlightApp.models import *

# Create your tests here.
class StatusTest(TestCase):
	"""
	Testa o CRUD de Estado do Voo
	"""
	@classmethod
	def setUpTestData(cls):
		Status.objects.create(id_status= 1, status_voo = 'Programado')

	def test_read(self):
		status_1 = Status.objects.get(id_status= 1)
		self.assertEqual(status_1.id_status,1)
		self.assertEqual(status_1.status_voo, 'Programado')

	def test_update(self):
		Status.objects.filter(id_status= 1).update(status_voo='Taxiando')
		status_2 = Status.objects.get(id_status= 1)
		self.assertEqual(status_2.id_status, 1)
		self.assertEqual(status_2.status_voo, 'Taxiando')
	
	def test_delete(self):
		Status.objects.filter(id_status= 1).delete()
		self.assertEqual(Status.objects.count(), 0)

class HorarioPrevistoTest(TestCase):
	"""
	Testa o CRUD de Horario Previsto
	"""
	@classmethod
  #CRUD TEST
	def setUpTestData(cls):
		HorarioPrevisto.objects.create(
			id_previsao=1, 
			partida_prevista = datetime.datetime(2022, 10, 10, 22, 30, 10, tzinfo=datetime.timezone.utc), 
			chegada_prevista = datetime.datetime(2022, 10, 11, 22, 30, 10, tzinfo=datetime.timezone.utc)
			)

	def test_read(self):
		previsao = HorarioPrevisto.objects.get(id_previsao = 1)
		self.assertEqual(previsao.id_previsao, 1)
		self.assertEqual(previsao.partida_prevista, datetime.datetime(2022, 10, 10, 22, 30, 10, tzinfo=datetime.timezone.utc))
		self.assertEqual(previsao.chegada_prevista, datetime.datetime(2022, 10, 11, 22, 30, 10, tzinfo=datetime.timezone.utc))
	
	def test_update(self):
		HorarioPrevisto.objects.filter(id_previsao=1).update(partida_prevista =
		datetime.datetime(2022, 10, 10, 22, 40, 20,  tzinfo=datetime.timezone.utc))
		previsao_2 = HorarioPrevisto.objects.get(id_previsao = 1)
		self.assertEqual(previsao_2.id_previsao, 1)
		self.assertEqual(previsao_2.partida_prevista, datetime.datetime(2022, 10, 10, 22, 40, 20,  tzinfo=datetime.timezone.utc))
		self.assertEqual(previsao_2.chegada_prevista, datetime.datetime(2022, 10, 11, 22, 30, 10, tzinfo=datetime.timezone.utc))
	
	def test_delete(self):
		HorarioPrevisto.objects.filter(id_previsao=1).delete()
		self.assertEqual(HorarioPrevisto.objects.count(), 0)

class HorarioRealTest(TestCase):
	"""
	Testa o CRUD de Horario Real
	"""
	@classmethod
  #CRUD TEST
	def setUpTestData(cls):
		HorarioReal.objects.create(
			id_real=1, 
			partida_real = datetime.datetime(2022, 10, 10, 22, 40, 20, tzinfo=datetime.timezone.utc), 
			chegada_real = datetime.datetime(2022, 10, 11, 22, 35, 10, tzinfo=datetime.timezone.utc)
			)

	def test_read(self):
		previsao = HorarioReal.objects.get(id_real = 1)
		self.assertEqual(previsao.id_real, 1)
		self.assertEqual(previsao.partida_real, datetime.datetime(2022, 10, 10, 22, 40, 20,  tzinfo=datetime.timezone.utc))
		self.assertEqual(previsao.chegada_real, datetime.datetime(2022, 10, 11, 22, 35, 10, tzinfo=datetime.timezone.utc))
	
	def test_update(self):
		HorarioReal.objects.filter(id_real=1).update(partida_real =
		datetime.datetime(2022, 10, 10, 22, 45, 10))
		previsao_2 = HorarioReal.objects.get(id_real = 1)
		self.assertEqual(previsao_2.id_real, 1)
		self.assertEqual(previsao_2.partida_real, datetime.datetime(2022, 10, 10, 22, 45, 10, tzinfo=datetime.timezone.utc))
		self.assertEqual(previsao_2.chegada_real, datetime.datetime(2022, 10, 11, 22, 35, 10, tzinfo=datetime.timezone.utc))
	
	def test_delete(self):
		HorarioReal.objects.filter(id_real=1).delete()
		self.assertEqual(HorarioReal.objects.count(), 0)
	
class RotaTest(TestCase):
	"""
	Testa o CRUD de Rota
	"""
	@classmethod
	#CRUD TEST
	def setUpTestData(cls):
		Rota.objects.create(id_rota = 1,
			aeroporto_destino = 'GRU',
			aeroporto_saida = 'JFK',
		)

	def test_read(self):
		rota_1 = Rota.objects.get(id_rota = 1)
		self.assertEqual(rota_1.id_rota, 1)
		self.assertEqual(rota_1.aeroporto_destino, 'GRU')
		self.assertEqual(rota_1.aeroporto_saida, 'JFK')

	def test_update(self):
		Rota.objects.filter(id_rota = 1).update(aeroporto_destino = 'MCO')
		rota_2 = Rota.objects.get(id_rota = 1)
		self.assertEqual(rota_2.id_rota, 1)
		self.assertEqual(rota_2.aeroporto_destino, 'MCO')
		self.assertEqual(rota_2.aeroporto_saida, 'JFK')

	def test_delete(self):
		Rota.objects.filter(id_rota = 1).delete()
		self.assertEqual(Rota.objects.count(), 0)

class TestVoo(TestCase):
	"""
	Tests for the Voo model.
	"""
	@classmethod
	#CRUD TEST
	def setUpTestData(cls):
		estado_voo = Status.objects.create(id_status = 10, status_voo = 'Programado')
		rota_voo = Rota.objects.create(id_rota = 13, aeroporto_destino = 'JFK', aeroporto_saida = 'GRU')
		previsao_voo = HorarioPrevisto.objects.create(id_previsao = 13,
			partida_prevista = datetime.datetime(2022, 10, 10, 22, 30, 10, tzinfo=datetime.timezone.utc),
			chegada_prevista = datetime.datetime(2022, 10, 11, 22, 30, 10, tzinfo=datetime.timezone.utc)
			)
		real_voo = HorarioReal.objects.create(id_real = 13,
			partida_real = datetime.datetime(2022, 10, 10, 22, 40, 20, tzinfo=datetime.timezone.utc), 
			chegada_real = datetime.datetime(2022, 10, 11, 22, 35, 10, tzinfo=datetime.timezone.utc)
		)
		Voo.objects.create(codigo_voo = 'TAM0001',
		companhia_aerea = "TAM",
		estado = estado_voo,
		rota = rota_voo,
		previsao = previsao_voo,
		real = real_voo)

	def test_read(self):
		voo_1 = Voo.objects.get(codigo_voo = 'TAM0001')
		self.assertEqual(voo_1.codigo_voo, 'TAM0001')
		self.assertEqual(voo_1.companhia_aerea, 'TAM')
	
	#TO-DO: Update
	# def test_update(self):
	# 	voo_1 = Voo.objects.filter(codigo_voo = 'TAM0001').update(companhia_aerea = 'GOL')
	# 	self.assertEqual(voo_1.companhia_aerea, "GOL")
	
	def test_delete(self):
		Voo.objects.filter(codigo_voo = 'TAM0001').delete()
		self.assertEqual(Voo.objects.count(), 0)




