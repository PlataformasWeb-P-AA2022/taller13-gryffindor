from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Edificio(models.Model):
    tipo_edificio = (
    ('(Residencial)','residencial'),
    ('(Comercial)','comercial')
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices = tipo_edificio)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

    def obtener_costo_departametos(self):
        valor = [d.costo_dep for d in self.departamentos.all()]
        valor = sum(valor)
        return valor

    def obtener_cant_cuartos(self):
        valor = [d.num_cuartos for d in self.departamentos.all()]
        valor = sum(valor)
        return valor

class Departamento(models.Model):
    nombre_prop = models.CharField(max_length=100)
    costo_dep = models.DecimalField(max_digits=100, decimal_places=2)
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %s %d" % (self.nombre_prop, 
                self.costo_dep, 
                self.num_cuartos)
