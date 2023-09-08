from django.shortcuts import render
from .models import Post

<<<<<<< HEAD
# Create your views here.
def searchbar(request):
    return render(request, 'single_pages/searchbar.html')

# def base(request):
#     return render(request, 'single_pages/base.html')
=======
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
>>>>>>> 3d258ebe1010dc7a5a12660344daba859c5590cd
