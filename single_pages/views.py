from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'single_pages/index.html',
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