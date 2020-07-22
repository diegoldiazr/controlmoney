from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):    
    gastomensual = models.BigIntegerField()
    empresa = models.TextField()
    memo = models.TextField()
    nombre = models.TextField()

    # datos de auditoria
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_modificacion = models.DateTimeField(
            blank=True, null=True)

    def guardar(self):
        self.fecha_modificacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre