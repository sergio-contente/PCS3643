from django.test import TestCase
import datetime
from FlightApp.models import *

# Create your tests here.
class StatusTest(TestCase):
	"""
	Testa o CRUD de Estado do Voo
	"""
	@classmethod
	def createTest(cls):
		Status.objects.create(id_voo = 1, status_voo = 'Programado')

	def readTest(self):
		status_1 = Status.objects.get(id_voo = 1)
		self.assertEqual(status_1.id,1)
		self.assertEqual(status_1.status_voo, 'Programado')

	def updateTest(self):
		Status.objects.filter(id_voo = 1).update(status_voo='Taxiando')
		status_2 = Status.objects.get(id_voo = 1)
		self.assertEqual(status_2.id, 1)
		self.assertEqual(status_2.status_voo, 'Taxiando')
	
	def deleteTest(self):
		Status.objects.filter(id_voo = 1).delete()
		self.assertEqual(Status.objects.count(), 0)

class HorarioPrevistoTest(TestCase):
	"""
	Testa o CRUD de Horario Previsto
	"""
	@classmethod
  #CRUD TEST
	def createTest(cls):
		HorarioPrevisto.objects.create(
			id_previsao=1, 
			partida_prevista = datetime(2022, 10, 10, 50, 22, datetime.tzinfo().timezone.utc), 
			chegada_prevista = datetime(2022, 10, 11, 50, 22, datetime.tzinfo().timezone.utc)
			)

	def readTest(self):
		previsao = HorarioPrevisto.objects.get(id_previsao = 1)
		self.assertEqual(previsao.id_previsao, 1)
		self.assertEqual(previsao.partida_prevista, datetime(2022, 10, 10, 50, 22, datetime.tzinfo().timezone.utc))
		self.assertEqual(previsao.chegada_prevista, datetime(2022, 10, 11, 50, 22, datetime.tzinfo().timezone.utc))
	
	def updateTest(self):
		HorarioPrevisto.objects.filter(id_previsao=1).update(partida_prevista =
		datetime(2022, 10, 10, 59, 22, datetime.tzinfo().timezone.utc))
		previsao_2 = HorarioPrevisto.objects.get(id_previsao = 1)
		self.assertEqual(previsao_2.id_previsao, 1)
		self.assertEqual(previsao_2.partida_prevista, datetime(2022, 10, 10, 59, 22, datetime.tzinfo().timezone.utc))
		self.assertEqual(previsao_2.chegada_prevista, datetime(2022, 10, 11, 50, 22, datetime.tzinfo().timezone.utc))
	
	def deleteTest(self):
		HorarioPrevisto.objects.filter(id_previsao=1).delete()
		self.assertEqual(HorarioPrevisto.objects.count(), 0)


