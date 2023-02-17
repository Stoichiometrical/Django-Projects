from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters =list('abcdefghijklmnopqrstuv')
    thepassword=''
    length=int(request.GET.get('length'))
    if request.GET.get('numbers'):
       characters.extend(list('1234567890'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRS'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    for x in range(length):
        thepassword+=random.choice(characters)



    return render(request, 'generator/password.html',{'password': thepassword})