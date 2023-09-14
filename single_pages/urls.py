from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('food/', views.FoodList.as_view()),
    path('cafe/', views.CafeList.as_view()),
    path('place/', views.PlaceList.as_view()),
    path('review/', views.ReviewList.as_view()),
    path('review/<int:pk>/', views.ReviewSinglePage.as_view(), name='reviewdetail'),
    path('review/category/<str:slug>/', views.category_page),
    path('review/create_review/', views.ReviewCreate.as_view()),
    path('date_course/', views.DateCourseList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)