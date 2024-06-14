from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return f"{self.marca} - {self.modelo} ({self.año})"

