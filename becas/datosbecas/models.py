from django.db import models

# Create your models here.

class Becario(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nombre')
    phone = models.IntegerField(default=0, verbose_name='Teléfono')
    mail = models.CharField(max_length=128, verbose_name='Correo')

    class Meta:
        db_table ='becarios'


