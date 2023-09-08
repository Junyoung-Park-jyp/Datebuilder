from django.urls import path
from . import views

urlpatterns = [
    path('food/', views.food),
    path('cafe/', views.cafe),
    path('place/', views.place),
    path('review/', views.review),
    path('date_course/', views.date_course),
]