from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre completo")
    cedula = models.CharField(max_length=20, unique=True, verbose_name="Cédula")
    fecha_nacimiento = models.CharField(max_length=10, verbose_name="Fecha de nacimiento")
    ultimos_digitos_tarjeta = models.CharField(max_length=4, verbose_name="Últimos 4 dígitos de la tarjeta")
    saldo = models.CharField(max_length=20, verbose_name="Saldo")
    
    def __str__(self):
        return f"{self.nombre} - {self.cedula}"
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
