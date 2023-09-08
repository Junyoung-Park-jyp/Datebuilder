from django.shortcuts import render

# Create your views here.
def searchbar(request):
    return render(request, 'single_pages/searchbar.html')

# def base(request):
#     return render(request, 'single_pages/base.html')