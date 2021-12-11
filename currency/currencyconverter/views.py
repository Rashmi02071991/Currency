from django.contrib.auth import models


# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Bank
from .models import Transaction
# from .models import CurrencyForm
from currencyconverter import forms
from django.db.models import F
import requests
import json



# Create your views here.
def index1(request):
    return HttpResponse('test')

def index(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'dashboard.html')

def login(request):
    return render(request,'login.html')

def loginAction(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            messages.success(request,"you are sucessfully Login")
            return redirect(dashboard)

        else:
            messages.error(request, "invalid username and password")
            return redirect(dashboard)
    else:
        return HttpResponse("bad request")


def logoutAction(request):
        logout(request)
        messages.success(request,"you are sucessfully Logout")
        return redirect(dashboard)

def signup(request):
    return render(request,'signup.html')

def signupaction(request):
    if request.method == 'POST':
            username = request.POST['uname']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            obj=User.objects.create_user(username,email,password)
            obj.first_name =fname
            obj.last_name =lname
            obj.save()
            messages.success(request,"Successfully Create your Account")
            return render(request,"dashboard.html")
    else:
             return HttpResponse("not login please again signup")

def convert(request):
    ''' convert the given amount to target country amount'''
    
    # calling API using requests lib
    api_request = requests.get("http://data.fixer.io/api/latest?access_key=40eac7a32ba84e0369830d99248246b7")
    currency_dict = json.loads(api_request.text)

    currency_rates_dict = currency_dict['rates']
    list_of_country_currency_code = [x for x in currency_rates_dict.keys()]
    tuple_of_country_codes = [tuple([x,x]) for x in list_of_country_currency_code]
    
    # initialize form with country currency code
    currency_form =forms.CurrencyForm(tuple_of_country_codes,request.POST or None)

    converted_currency = ""
    if request.method == "POST":
        # check sanitation
        if currency_form.is_valid():

            # values from the html input fields
            source_currency_code = currency_form.cleaned_data['source_currency_code']
            target_currency_code = currency_form.cleaned_data['target_currency_code']
            input_currency_value = currency_form.cleaned_data['source_currency_value']

            # get live amount of selected country 
            from_country_base_value = currency_rates_dict[source_currency_code]
            to_country_base_value = currency_rates_dict[target_currency_code]
            
            # logic to calculate the converted_currency
            converted_currency = (to_country_base_value / from_country_base_value) * float(input_currency_value)

            return render(request, 'currencyconvert.html', {'currency_form':currency_form, 'converted_currency':converted_currency})

    # form initialization
    context = {
        'currency_form': currency_form,
        'converted_currency':converted_currency
    }
    return render(request, 'currencyconvert.html', context)             


def viewcustomer(request,account):
    bank=Bank.objects.filter(customer_account_no=account)
    param = {'bank':bank}
    return render(request,'customerview.html', param)


def transfer(request):
    return render(request,'transfer.html')

def showtransferresult(request):
    account=request.POST.get("ac",default=0)
    amt=float(request.POST.get("amount"))
    acc=request.POST.get("account")
    date=request.POST.get("date")
    bank=Bank.objects.get(customer_account_no=account)
    amt1= bank.amount
    if amt <= amt1:
        Bank.objects.filter(customer_account_no=account).update(amount=F('amount') - amt)
        trans = Transaction(account_no=account, amount=amt, tdate=date, satus='withdraw')
        trans.save()
        print("transfer sucessfully")
    else:
        print("insufficient balance")
    return render(request,'showtransferresult.html')


   