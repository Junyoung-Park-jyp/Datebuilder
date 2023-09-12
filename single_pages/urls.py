from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('food/', views.food),
    path('cafe/', views.CafeList.as_view()),
    path('place/', views.place),
    path('review/', views.review),
    path('date_course/', views.date_course),
    path('cafe_detail/<int:pk>/', views.cafe_detail, name='cafe_detail'),
    path('food_detail/', views.food_detail),
    path('place_detail/', views.place_detail),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)