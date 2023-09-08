from django.urls import path
from . import views

urlpatterns = [
    path('searchbar/', views.searchbar),
    # path('base/', views.base),
]