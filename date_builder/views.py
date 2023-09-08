from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'single_pages/landing.html')


def site(request):
    return HttpResponse("위치 검색 페이지 url")

def main(request):
    return render(request, 'single_pages/base.html')

