from django.db import models
from datetime import datetime

# Create your models here.
class Vote(models.Model):
    TURMA = (
        ('M1A','M1A'),
        ('M1B','M1B'),
        ('M2A','M2A'),
        ('M2B','M2B')
    )

    FLOWERSCHOICES = (
        ('Tulipa','Tulipa'),
        ('Rosa','Rosa'),
        ('Flores do Campo','Flores do Campo'),
    )
    currentDate = models.DateTimeField(default=datetime.now())
    nome = models.CharField(max_length=200, default="SEM NOME")
    turma = models.CharField(max_length=4, choices=TURMA)
    flor = models.CharField(max_length=30, choices=FLOWERSCHOICES)