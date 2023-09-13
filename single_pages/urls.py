from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('review/', views.review),
    path('date_course/', views.date_course),
    path('createcourse/', views.create_course, name='createcourse'),
    path('cafe/', views.CafeList.as_view(), name='pickcafe'),
    path('food/', views.FoodList.as_view(), name='pickfood'),
    path('place/', views.PlaceList.as_view(), name='pickplace'),
    path('cafe/<int:cafe_id>/', views.CafeDetail.as_view(), name='cafe_detail'),
    path('food/<int:food_id>/', views.FoodDetail.as_view(), name='food_detail'),
    path('place/<int:place_id>/', views.PlaceDetail.as_view(), name='place_detail'),
    path('introduce/', views.introduce),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)