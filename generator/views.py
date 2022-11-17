from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, "generator/home.html")

def password(request):
    characters = list("qwertyuiopasdfghjklzxcvbnm")


    if request.GET.get('uppercase'):
        characters.extend(list("QWERTYUIOPASDFGHJKLZXCVBNM"))

    if request.GET.get('specical'):
        characters.extend(list("<>.//?][]-+!@#$%^$^&"))

    if request.GET.get('numbers'):
        characters.extend(list("123456789"))

    length = int(  request.GET.get("length"),12 )

    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, "generator/password.html", {"password": thepassword})


def myself(request):
    return render(request, "generator/myself.html")
