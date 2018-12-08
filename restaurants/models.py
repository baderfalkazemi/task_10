from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logos', null=True, blank=True)

    def __str__(self):
    	return self.name

class Item(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=3)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

	def __str__(self):
		return self.name