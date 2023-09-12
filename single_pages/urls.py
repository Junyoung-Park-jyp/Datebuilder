from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('review/', views.review),
    path('date_course/', views.date_course),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('cafe/<int:cafe_id>/', views.cafe_detail, name='cafe_detail'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('createcourse/', views.create_course, name='create_course'),
    # path('cafe_detail/<int:pk>/', views.cafe_detail, name='cafe_detail'),
    # path('food_detail/', views.food_detail),
    # path('place_detail/<int:place_id>', views.place_detail),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)