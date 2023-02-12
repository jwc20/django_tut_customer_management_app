from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/dashboard.html')


def product(request):
    return HttpResponse("Product Page")


def customer(request):
    return HttpResponse("Customer Page")
