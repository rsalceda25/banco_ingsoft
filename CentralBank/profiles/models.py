from django.db import models
import datetime

class BasicDetails (models.Model):
    nombre = models.CharField(max_length = 50, default = None)
    sexo = models.CharField(max_length = 1, default = None)
    ingreso_anual = models.IntegerField(default = 0)
    telefono = models.IntegerField(default = 0)
    ocupacion = models.CharField(max_length = 50, default = None)


class PresentLocation (models.Model):
    # (Country, State, City, Street, Pincode) 
    Pais = models.CharField(max_length = 50, default = "Mexico")
    Estado = models.CharField(max_length = 50)
    Ciudad = models.CharField(max_length = 50)
    Calle = models.CharField(max_length = 50)
    Codigo_postal = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)

class Status (models.Model):
    account_number = models.IntegerField()
    balance = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)

class MoneyTransfer(models.Model):
    nombre_de_usuario = models.CharField(max_length = 150, default = None)
    no_cuenta_que_recibira_la_transferencia = models.IntegerField()
    monto_a_transferir = models.IntegerField()

class MoneyLoan(models.Model):
    nombre_usuario = models.CharField(max_length = 150, default = None)
    no_cuenta = models.IntegerField()
    monto_prestamo = models.IntegerField()

class online (models.Model):
    nombre_usuario = models.CharField(max_length = 150, default = None)
    no_cuenta = models.IntegerField()
    monto_retirar = models.IntegerField()





