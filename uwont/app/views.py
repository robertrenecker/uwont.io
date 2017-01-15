from django.shortcuts import render
from django.http import HttpResponse
from app.models import User


def index(request):
    li = []
    user = User(firstname="Robert", lastname="KYS")
    user.save()
    for u in User.objects():
        li.append()
        print (u.firstname, u.lastname)
    return HttpResponse("Hello, World!")

def lol(request):
    print ("in lol")
    return HttpResponse("ROB KYS")
