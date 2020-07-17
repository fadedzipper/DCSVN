from django.db import models

# Create your models here.

class Net(models.Model):

    net_name = models.CharField(max_length=50)