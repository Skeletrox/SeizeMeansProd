from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the default HTTP response for the player app.")
