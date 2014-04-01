from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def depotapp_test(request):
    return HttpResponse('Welcome to depotapp!')