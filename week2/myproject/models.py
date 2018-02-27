from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
	Firstname
	lastname
	telephone
	date of birth
	credit amount
	profiles image
	Memo 500 characters
'''

class Person(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	telephone=models.CharField(max_length=15)
	dob=models.DateField(blank=True,null=True)
	credit_amount=models.DecimalField(max_digits=15, decimal_places=2)
	memo=models.CharField(max_length=500)

	#null = true no*

# class User(models.model):
# 	uname
# 	name
# 	password
# 	email

class Car(models.Model):
	name =models.CharField(max_length=100)
	detail=models.CharField(max_length=100)
	price=models.DecimalField(max_digits=15, decimal_places=2)
	image=models.ImageField(upload_to='images')
	def __str__(self):
		return u"Brand : %s - Year : %s - Fee : %d Bath"%(self.name, self.detail , self.price)

class Rent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	car = models.ForeignKey(Car, on_delete=models.CASCADE)
	start_datetime = models.DateTimeField(null=True)
	stop_datetime= models.DateTimeField(null=True)
	fee= models.DecimalField(max_digits=15, decimal_places=2,null=True)
