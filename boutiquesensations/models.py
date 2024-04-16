from django.db import models

# Create your models here.
from django.db import models

class AccessoryType(models.Model):
    name = models.CharField(max_length=200,verbose_name='Nombre del tipo de accesorio',unique=True)

    def __str__(self):
        return self.name

class Accessory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del accesorio')
    description = models.TextField(verbose_name='Descripción')
    price = models.IntegerField(verbose_name='Precio')
    image = models.ImageField(upload_to='boutiquesensations/',verbose_name='Imagen')
    type = models.ForeignKey(AccessoryType, on_delete=models.CASCADE,verbose_name='Tipo de accesorio')

    def __str__(self):
        return self.name

class Coupon(models.Model):
    code = models.CharField(max_length=50, verbose_name='Código del cupón')
    discount = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Descuento')

    def __str__(self):
        return self.name
