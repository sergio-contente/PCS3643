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


