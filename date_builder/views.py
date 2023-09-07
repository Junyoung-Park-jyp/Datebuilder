from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'single_pages/index.html')
  

def site(request):
  return HttpResponse("위치 검색 페이지 url")

def food(request):
  return HttpResponse("식당 선택 페이지 url")

def cafe(request):
  return HttpResponse("카페 선택 페이지 url")

def play(request):
  return HttpResponse("근처 놀거리 선택 페이지 url")

