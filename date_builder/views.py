from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'single_pages/landing.html')


def main(request):
    return render(request, 'single_pages/base.html')

def login(request):
    return render(request, 'common/login.html')

def introduce(request):
    return render(request, 'introduce.html')