from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Becario(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nombre')
    phone = models.IntegerField(default=0, verbose_name='Teléfono')
    mail = models.CharField(max_length=128, verbose_name='Correo')

    class Meta:
        db_table ='becarios'

class Estudio(models.Model):
    Discipline = models.CharField(max_length=128, verbose_name='Disciplina')
    Grade = models.CharField(max_length=128, verbose_name='Grado')
    Country = models.CharField(max_length=128, verbose_name='País')
    University = models.CharField(max_length=128, verbose_name='University')

    class Meta:
        db_table ='estudios'

class Beca(models.Model):
    Becario = models.ForeignKey(Becario, on_delete=models.CASCADE, null=True, verbose_name='Becario')
    First_date = models.DateField(verbose_name='Fecha de inicio')
    End_date = models.DateField(verbose_name='Fecha final')
    Status = models.CharField(max_length=128, verbose_name='Estado de la beca')
    Create_date = models.DateTimeField(auto_now_add=True,verbose_name='Fecha creación')

    class Meta:
        db_table = 'becas'



    


