from django.db import models

# Create your models here.


class Company(models.Model):
    nit = models.CharField(primary_key=True, max_length=9)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    description = models.CharField(max_length=500)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.name, self.address, self.phone, self.description)
