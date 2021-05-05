from django.db import models


# Create your models here.
class Detail(models.Model):
	user = models.CharField(max_length=50)
	time = models.DateTimeField(auto_now=True)
	# age = models.IntegerField()
	age = models.CharField(max_length=50)
	gen = models.CharField(max_length=50) 
	# wei = models.IntegerField()
	# hei = models.IntegerField()
	# bp = models.IntegerField()
	# sug = models.IntegerField()
	# tem = models.IntegerField()
	# hae = models.IntegerField()
	# bmi = models.DecimalField(max_digits=4, decimal_places=1)
	# dia = models.DecimalField(max_digits=4, decimal_places=1)
	# typ = models.DecimalField(max_digits=4, decimal_places=1)
	# hea = models.DecimalField(max_digits=4, decimal_places=1)
	# ane = models.DecimalField(max_digits=4, decimal_places=1)
	# den = models.DecimalField(max_digits=4, decimal_places=1)
	wei = models.CharField(max_length=50)
	hei = models.CharField(max_length=50)
	bp = models.CharField(max_length=50)
	sug = models.CharField(max_length=50)
	tem = models.CharField(max_length=50)
	hae = models.CharField(max_length=50)
	bmi = models.CharField(max_length=50)
	dia = models.CharField(max_length=50)
	typ = models.CharField(max_length=50)
	hea = models.CharField(max_length=50)
	ane = models.CharField(max_length=50)
	den = models.CharField(max_length=50)

	def __str__(self):
		return self.user

	def __str__(self):
		return self.user