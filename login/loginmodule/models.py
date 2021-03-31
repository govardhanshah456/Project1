from django.db import models
from django.contrib.auth.models import User
class shopper(models.Model):
    Fname=models.CharField(max_length=100)
    Userfk=models.ForeignKey(User,on_delete=models.CASCADE)
