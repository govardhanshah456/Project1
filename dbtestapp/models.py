from django.db import models

# Create your models here.

class Customer(models.Model):
	name=models.CharField(max_length=100)
	address=models.TextField()
	cust_id=models.AutoField(primary_key=True)
	email=models.CharField(max_length=50)
	mobile=models.IntegerField()

class Seller(models.Model):
	seller_name=models.CharField(max_length=100)
	seller_address=models.TextField()
	seller_id=models.AutoField(primary_key=True)
	seller_email=models.CharField(max_length=50)
	seller_mobile=models.IntegerField()

class Product(models.Model):
	prod_name=models.CharField(max_length=100)
	prod_brand=models.CharField(max_length=30,primary_key=True)
	prod_availability=models.BooleanField()
	prod_category=models.CharField(max_length=50)
	prod_price=models.IntegerField()

