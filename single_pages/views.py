from typing import Any
from django.shortcuts import render
from .models import Post, Cafe, Food, Place, Review
from django.views.generic import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# 포스트 연결하기 테스트
from single_pages.models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'single_pages/landing.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'single_page/single_post_page.html',
        {
            'post': post,
        }
    )

# 포스트 연결하기 테스트
def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
        }
    )

# 포스트 연결하기 테스트

# def food(request):
#     return render(request, 'single_pages/food.html')

# def cafe(request):
#     return render(request, 'single_pages/cafe.html')

# def place(request):
#     return render(request, 'single_pages/place.html')



class CafeList(ListView):
    model = Cafe
    template_name = "single_pages/cafe.html"
    context_object_name = "cafes"
    ordering = '-pk'
    paginate_by = 4
    # paginator = Paginator(cafe,9)
                          
    # try:
    #     page_obj = paginator.page(page)
    # except PageNotAnInteger:
    #     page = 1
    #     page_obj = paginator.page(page)
    # except EmptyPage:
    #     page = paginator.num_pages
    #     page_obj = paginator.page(page)

    # leftIndex = (int(page) - 9)
    # if leftIndex < 1:
    #     leftIndex = 1

    # rightIndex = (int(page) + 9)

    # if rightIndex > paginator.num_pages:
    #     rightIndex = paginator.num_pages

    # custom_range = range(leftIndex, rightIndex+1)


class FoodList(ListView):
    model = Food
    template_name = "single_pages/food.html"
    context_object_name = "foods"
    ordering = '-pk'
    paginate_by = 4

class PlaceList(ListView):
    model = Place
    template_name = "single_pages/place.html"
    context_object_name = "places"
    ordering = '-pk'
    paginate_by = 4

class ReviewList(ListView):
    model = Review
    template_name = "single_pages/review.html"
    context_object_name = "reviews"
    ordering = '-pk'
    paginate_by = 4

class ReviewSinglePage(DetailView):
    model = Review
    template_name = "single_pages/review_single_page.html"

    def get_context_data(self, **kwargs):
        context = super(ReviewSinglePage, self).get_context_data()

        return context
    

# def review(request):
#     reviews = Review.objects.all().order_by('-pk')
#     return render(request, 'single_pages/review.html', {'reviews':reviews})

# def review_single_page(request, pk):
#     review = Review.objects.get(pk=pk)
#     return render(request, 'single_pages/review_single_page.html', {'review':review})

def date_course(request):
    return render(request, 'single_pages/date_course.html')