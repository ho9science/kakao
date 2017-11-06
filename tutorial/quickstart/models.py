from django.db import models


class Klog(models.Model):
	id = models.IntegerField(primary_key=True)
	query = models.CharField(max_length=767)
	reply = models.CharField(max_length=767)
	qdate = models.DateField(auto_now=True)


class Kknouns(models.Model):
	class Meta:
		db_table='kknouns'
	id=models.IntegerField(primary_key=True)
	indexing=models.CharField(max_length=200)
	answer=models.CharField(max_length=767)

