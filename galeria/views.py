from django.shortcuts import render
from django.http import HttpResponse

def index(Request):
    return HttpResponse('<h1>Alura Space</h1>')
