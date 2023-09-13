from typing import Any
from django.shortcuts import render, redirect
from .models import Post, Cafe, Food, Place, Review, Category
from django.views.generic import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin

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




class CafeList(ListView):
    model = Cafe
    template_name = "single_pages/cafe.html"
    context_object_name = "cafes"
    ordering = '-pk'
    paginate_by = 4

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

    def get_context_data(self, **kwargs):
        context = super(ReviewList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_reviews_count'] = Review.objects.filter(category=None).count()
        return context
    
def category_page(request, slug):
    if  slug == 'no_category':
        category = '미분류'
        review = Review.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        review = Review.objects.filter(category=category)

    return render(request, 'single_pages/review.html', {
        'review': review,
        'categories': Category.objects.all(),
        'no_category_reviews_count': Review.objects.filter(category=None).count(),
        'category': category,
    })



class ReviewSinglePage(DetailView):
    model = Review
    template_name = "single_pages/review_single_page.html"
    # context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super(ReviewSinglePage, self).get_context_data()
        # context['categories'] = Category.objects.all()
        # context['no_category_reviews_count'] = Review.objects.filter(category=None).count()
        return context
    
class ReviewCreate(CreateView):
    model = Review
    fields = ['title', 'content', 'head_image', 'category']


# 함수형 view들
# def food(request):
#     return render(request, 'single_pages/food.html')

# def cafe(request):
#     return render(request, 'single_pages/cafe.html')

# def place(request):
#     return render(request, 'single_pages/place.html')

# def review(request):
#     reviews = Review.objects.all().order_by('-pk')
#     return render(request, 'single_pages/review.html', {'reviews':reviews})

# def review_single_page(request, pk):
#     review = Review.objects.get(pk=pk)
#     return render(request, 'single_pages/review_single_page.html', {'review':review})

def date_course(request):
    return render(request, 'single_pages/date_course.html')