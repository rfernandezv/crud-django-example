from django.db import models
from django.utils import timezone

# Create your models here.
class Postres(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20)
    stock = models.CharField(max_length=100)
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
         db_table = 'postres' # Le doy de nombre 'postres' a nuestra tabla en la Base de Datos
