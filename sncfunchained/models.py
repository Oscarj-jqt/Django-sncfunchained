from django.db import models

# Create your models here.

class Sncfunchained(models.Model) :
    trainID = models.AutoField(primary_key=True)
    ville = models.CharField(max_length = 50)
    heure_depart = models.TimeField(max_length = 50)
    heure_arrivee = models.TimeField(max_length = 50)
