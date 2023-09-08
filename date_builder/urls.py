"""
URL configuration for date_builder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index, name='index'),
    path('nav/', views.main),
    path('login',views.login),
    path('', include('allauth.urls')),
    # path('main/restaurant', views.restaurant),
    # path('main/cafe', views.cafe),
    # path('main/play', views.play),
    path('markdownx/', include('markdownx.urls')),
    # path('searchbar/', ('single_pages.urls')),index
    path('food/', include('single_pages.urls')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)