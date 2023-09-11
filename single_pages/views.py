from django.shortcuts import render
from .models import Post

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

def food(request):
    return render(request, 'single_pages/food.html')

def cafe(request):
    return render(request, 'single_pages/cafe.html')

def place(request):
    return render(request, 'single_pages/place.html')

def review(request):
    return render(request, 'single_pages/review.html')

def date_course(request):
    return render(request, 'single_pages/date_course.html')
