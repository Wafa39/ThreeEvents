from django.db import models

class Events(models.Model):
 categoryname = models.CharField(max_length = 50)
 pakagedetails = models.CharField(max_length = 50)
 price = models.FloatField(default = 0.0)
