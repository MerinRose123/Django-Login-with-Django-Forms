from django import forms
from .models import userlogin
from django.shortcuts import render


class ContactForm(forms.Form):
    firstname = forms.CharField(required=False, max_length=50)
    lastname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    mail = forms.EmailField(label='Your email', max_length=50)
    phonenumber = forms.IntegerField()
    address = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput())
    password_again = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class HomeForm(forms.Form):
    username = forms.CharField(max_length=50)
    firstname = forms.CharField(required=False, max_length=50)
    lastname = forms.CharField(required=False, max_length=50)
    address = forms.CharField(required=False, max_length=50)
    phonenumber = forms.IntegerField(required=False)