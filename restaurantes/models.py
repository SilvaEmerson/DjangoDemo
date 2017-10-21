from django.db import models
from django.utils import timezone

# Create your models here.

class Restaurant(models.Model):
	"""docstring for Restaurant"""
	owner = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	adress = models.CharField(max_length=200)
	speciality = models.CharField(max_length=200)
	fund_date = models.DateField(
		blank=True, null=True)

	def __str__(self):
		return self.name