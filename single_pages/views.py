from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.db.models import Q


def food(request):
    return render(request, 'single_pages/food.html')

def place(request):
    return render(request, 'single_pages/place.html')

def review(request):
    return render(request, 'single_pages/review.html')

def date_course(request):
    return render(request, 'single_pages/date_course.html')


class CafeList(ListView):
    model = Cafe
    template_name = "single_pages/cafe.html"
    context_object_name = "cafes"

class FoodList(ListView):
    model = Food
    template_name = "single_pages/food.html"
    context_object_name = "foods"

class PlaceList(ListView):
    model = Place
    template_name = "single_pages/place.html"
    context_object_name = "places"

# 서치 
class PostSearch(FoodList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.object.filter(
            Q(title__contains=q) | Q(tags__name__contains=q)
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search:{q} ({self.get_queryset().count()})'

        return context