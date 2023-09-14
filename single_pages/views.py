from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import JsonResponse
from typing import Any
from django.views.generic import *
from django.http import JsonResponse
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CourseForm
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
        'build/landing.html',
        {
            'recent_posts': recent_posts,
        }
    )

def review(request):
    return render(request, 'single_pages/review.html')

def introduce(request):
    return render(request, 'single_pages/introduce.html')


def introduce(request):
    return render(request, 'single_pages/introduce.html')

def date_course(request):
    return render(request, 'single_pages/date_course.html')


class CafeDetail(DetailView):
    model = Cafe
    template_name = "single_pages/cafe_detail.html"
    pk_url_kwarg = 'cafe_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context
    
class FoodDetail(DetailView):
    model = Food
    template_name = "single_pages/food_detail.html"
    pk_url_kwarg = 'food_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context
    
class PlaceDetail(DetailView):
    model = Place
    template_name = "single_pages/place_detail.html"
    pk_url_kwarg = 'place_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

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

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            # 원하는 로직 추가 가능
            return redirect('pickfood')  # 선택 후 리다이렉트할 URL로 수정
    else:
        form = CourseForm()

    return render(request, 'single_pages/createcourse.html', {'form': form})
    ordering = '-pk'
    paginate_by = 4

class DateCourseList(ListView):
    model = DateCourse
    template_name = "single_pages/date_course.html"
    context_object_name = "courses"
    ordering = '-pk'
    paginate_by = 8
    
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

    def get_context_data(self, **kwargs):
        context = super(ReviewSinglePage, self).get_context_data()
        return context
    
class ReviewCreate(CreateView):
    model = Review
    fields = ['title', 'content', 'head_image', 'category']

