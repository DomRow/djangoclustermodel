from __future__ import unicode_literals

from django.db import models

class Film(models.Model):
	id=models.IntegerField(primary_key=True)
	title=models.CharField(max_length=10)
	image=models.CharField(max_length=10)
	genre=models.CharField(max_length=10)
	image=models.CharField(max_length=10)



