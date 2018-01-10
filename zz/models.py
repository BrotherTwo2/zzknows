from django.db import models

# Create your models here.
class Raw(models.Model):
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=200)
	local_uri = models.CharField(max_length=200)

class Fresh(models.Model):
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=200)
	oss = models.CharField(max_length=100)

class Mature(models.Model):
	title = models.CharField(max_length=100)
	orignal = models.CharField(max_length=100)
	processed = models.CharField(max_length=100)