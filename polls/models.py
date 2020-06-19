from django.db import models

# Create your models here.
class Output(models.Model):
	price = models.FloatField(max_length=200,blank=True, null=True)
	asin = models.CharField(max_length=200,blank=True, null=True)
	rank = models.IntegerField(blank=True, null=True)
	link = models.CharField(max_length=200,blank=True, null=True)
	date = models.CharField(max_length=200, blank=True, null=True)
	List = models.CharField(max_length=200, blank=True, null=True)
	brand = models.CharField(max_length=200, blank=True, null=True)
	cpu = models.CharField(max_length=200, blank=True, null=True)
	screen = models.CharField(max_length=200, blank=True, null=True)
	ram = models.CharField(max_length=200, blank=True, null=True)
	Type = models.CharField(max_length=200, blank=True, null=True)
	model = models.CharField(max_length=200, blank=True, null=True)
	os = models.CharField(max_length=200, blank=True, null=True)
	DVD = models.CharField(max_length=200, blank=True, null=True)
	keyboard = models.CharField(max_length=200, blank=True, null=True)
	security = models.CharField(max_length=200, blank=True, null=True)
	vc = models.CharField(max_length=200, blank=True, null=True)
	upc = models.CharField(max_length=200, blank=True, null=True)
	sku = models.CharField(max_length=200, blank=True, null=True)
	office = models.CharField(max_length=200, blank=True, null=True)