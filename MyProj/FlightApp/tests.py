from django.test import TestCase
import datetime
from FlightApp.models import *

# Create your tests here.
class StatusTest(TestCase):
	@classmethod
	#CRUD TEST
	def createTest(cls):
		Status.objects.create(id=1, status_voo = 'Programado')

	def readTest(self):
		status_1 = Status.objects.get(id=1)
		self.assertEqual(status_1.id,1)
		self.assertEqual(status_1.status_voo, 'Programado')

	def updateTest(self):
		status_1 = Status.objects.get(id=1)
		Status.objects.filter(id=1).update(status_voo='Taxiando')
		status_2 = Status.objects.get(id=1)
		self.assertEqual(status_2.id, 1)
		self.assertEqual(status_2.status_voo, 'Taxiando')
	
	def deleteTest(self):
		Status.objects.filter(id=1).delete()
		self.assertEqual(Status.objects.count(), 0)
