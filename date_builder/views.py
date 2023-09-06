from django.http import HttpResponse

def index(request):
  return HttpResponse("Test 성공!")

def site(request):
  return HttpResponse("위치 검색 페이지 url")

def food(request):
  return HttpResponse("식당 선택 페이지 url")

def cafe(request):
  return HttpResponse("카페 선택 페이지 url")

def play(request):
  return HttpResponse("근처 놀거리 선택 페이지 url")

