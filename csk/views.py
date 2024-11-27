from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('captain of csk ruthuraj')
def vicecaptain(request):
    return HttpResponse('<h1>vicecaptain of csk ruthuraj</h1>')