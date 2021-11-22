from django import forms
from . import models

class BasicDetailsForm (forms.ModelForm):
    # class to store all the model form fields from models.py
    class Meta:
        model = models.BasicDetails
        fields = ["nombre", "sexo", "ingreso_anual", "telefono", "ocupacion"]


class PresentLocationForm (forms.ModelForm):
    class Meta:
        model = models.PresentLocation
        fields = ["Pais", "Estado", "Ciudad", "Calle", "Codigo_postal"]

class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = models.MoneyTransfer
        fields = [
            "nombre_de_usuario",
            "no_cuenta_que_recibira_la_transferencia", 
            "monto_a_transferir"
        ]

class MoneyLoan (forms.ModelForm):
    class Meta:
        model = models.MoneyLoan
        fields = [
            "nombre_usuario",
            "no_cuenta",
            "monto_prestamo"
        ]



class online (forms.ModelForm):
    class Meta:
        model = models.online
        fields = [
            "nombre_usuario",
            "no_cuenta",
            "monto_retirar"
        ]

