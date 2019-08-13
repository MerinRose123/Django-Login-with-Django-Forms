from django.shortcuts import render, redirect, render_to_response
from django.shortcuts import HttpResponse
from django.template import loader
from .models import userlogin
from django.contrib import messages
from .forms import ContactForm
from .forms import LoginForm
from .forms import HomeForm
# Create your views here.

def editrender(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
    else:
        form = HomeForm()
    return render(request, 'userlogin/editpage.html', {'form': form})
def edit(request):
    print("Control here")
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phonenumber = request.POST.get('phonenumber')
        address = request.POST.get('address')
        #password = request.POST.get("password")
        if userlogin.objects.filter(username=username).exists():
            emp = userlogin.objects.get(username=username)
            emp.lastname = lastname
            emp.phonenumber = phonenumber
            emp.address = address
            emp.firstname = firstname
            emp.save()
            data = userlogin.objects.all()
            return render(request, 'userlogin/home.html', {'userlogin': data})
            return response
        else:
            return HttpResponse('username doesnot exist')
    else:
        response = redirect('../login/')
        return response


def loginview(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get("password")
            if userlogin.objects.filter(username=username, password=password).exists():
                data = userlogin.objects.all()

                return render(request, 'userlogin/home.html', {'userlogin': data})
            else:
                return HttpResponse('username or password are not correct')
            #return render(request, 'userlogin/home.html', stu, {'form': form})
            #response = redirect('../homecreate/')
            #return response
    else:
        return render(request, 'userlogin/login.html')

def login(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = LoginForm(request.POST)
    else:
        # GET, generate blank form
        form = LoginForm()
    return render(request, 'userlogin/login.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
    else:
        # GET, generate blank form
        form = ContactForm()
    return render(request, 'userlogin/formnew.html', {'form': form})


def register(request):
    if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            mail = request.POST.get('mail')
            address = request.POST.get('address')
            phonenumber = request.POST.get('phonenumber')
            password = request.POST.get("password")
            password2 = request.POST.get("password_again")

            if password == password2:
                if userlogin.objects.filter(username=username).exists():
                    print("username taken")
                    return HttpResponse('username already exists')
                else:
                    q = userlogin(firstname=firstname, lastname=lastname, username=username, mail=mail, address=address, phonenumber=phonenumber, password=password)
                    q.save()
                    response = redirect('../login/')
                    return response
            else:
                #messages.info(request,'password not same')
                return HttpResponse('passwords are not same')
    else:
        return render(request, 'userlogin/formnew.html', {'form': form})
