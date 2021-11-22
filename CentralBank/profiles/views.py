from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from profiles.models import Status 
import random

def randomGen():
    # return a 6 digit random number
    return int(random.uniform(100000, 999999))

def index(request):
    try:
        curr_user = Status.objects.get(user_name=request.user) # getting details of current user
    except:
        # if no details exist (new user), create new details
        curr_user = Status()
        curr_user.account_number = randomGen() # random account number for every new user
        curr_user.balance = 0
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "profiles/profile.html", {"curr_user": curr_user})

def money_transfer(request):
    if request.method == "POST":
        form = forms.MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()
        
            curr_user = models.MoneyTransfer.objects.get(nombre_de_usuario=request.user)
            dest_user_acc_num = curr_user.no_cuenta_que_recibira_la_transferencia

            temp = curr_user # NOTE:  
            
            dest_user = models.Status.objects.get(account_number=dest_user_acc_num) 
            transfer_amount = curr_user.monto_a_transferir  
            curr_user = models.Status.objects.get(user_name=request.user)  

            # Now transfer the money!
            curr_user.balance = curr_user.balance - transfer_amount
            dest_user.balance = dest_user.balance + transfer_amount

             
            curr_user.save()
            dest_user.save()

            temp.delete()  

        return redirect("profiles/profile.html")
    else:
        form = forms.MoneyTransferForm()
    return render(request, "profiles/money_transfer.html", {"form": form})

def loan_app(request):
    if request.method == "POST":
        form = forms.MoneyLoan(request.POST)
        if form.is_valid():
            form.save()
        
            curr_user = models.MoneyLoan.objects.get(nombre_usuario=request.user)
            dest_user_acc_num = curr_user.no_cuenta

            temp = curr_user # NOTE: 

            dest_user = models.Status.objects.get(account_number=dest_user_acc_num)  
            loan_amount = curr_user.monto_prestamo
            curr_user = models.Status.objects.get(user_name=request.user)  

            # Now transfer the money!
            dest_user.balance = dest_user.balance + loan_amount
            curr_user.save()
            dest_user.save()
            temp.delete()  
        return redirect("profiles/profile.html")
    else:
        form = forms.MoneyLoan()
    return render(request, "profiles/loans.html", {"form": form})

def ewallet(request):
    return render(request, "profiles/eWallet.html")

def online_pay(request):
    if request.method == "POST":
        form = forms.online(request.POST)
        if form.is_valid():
            form.save()
        
            curr_user = models.online.objects.get(nombre_usuario=request.user)
            dest_user_acc_num = curr_user.no_cuenta

            temp = curr_user # NOTE:  
            
            dest_user = models.Status.objects.get(account_number=dest_user_acc_num)  
            transfer_amount = curr_user.monto_a_retirar
            curr_user = models.Status.objects.get(user_name=request.user)  

            # Now transfer the money!
            curr_user.balance = curr_user.balance - transfer_amount
            dest_user = dest_user
           

             
            curr_user.save()
            temp.delete()  

        return redirect("profiles/profile.html")
    else:
        form = forms.online()
    return render(request, "profiles/online_payment.html", {"form": form})

def settings(request):
    return render(request, "profiles/settings.html")

def edit_details(request):
    if request.method == "POST":
        # POST actions for BasicDetailsForms
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form = forms.BasicDetailsForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.BasicDetailsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()

        # POST actions for PresentLocationForm
        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form = forms.PresentLocationForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.PresentLocationForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()     
        
        # POST actions for Password change
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

        return redirect("profiles/edit_details.html")
    
    else: # GET actions
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form1 = forms.BasicDetailsForm(instance=curr_user) # basic details
        except:
            form1 = forms.BasicDetailsForm()
        
        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form2 = forms.PresentLocationForm(instance=curr_user) # location
        except:
            form2 = forms.PresentLocationForm()

        # change password
        form3 = PasswordChangeForm(request.user)

        dici = {"form1": form1, "form2": form2, "form3": form3}
        return render(request, "profiles/edit_details.html", dici)

def delete_account(request):
    return render(request, "profiles/delete_account.html")


