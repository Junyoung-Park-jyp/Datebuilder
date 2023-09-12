from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.views.generic import *

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
    return render(request, 'build/review.html')

def date_course(request):
    return render(request, 'build/date_course.html')

def cafe_detail(request):
    return render(request, 'single_pages/cafe_detail.html')

def food_detail(request):
    return render(request, 'single_pages/food_detail.html')

def place_detail(request):
    return render(request, 'single_pages/place_detail.html')


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

def create_course(request):
    if request.method == 'GET':
        # 클라이언트에서 전달한 데이터 ID 가져오기
        data_id = request.GET.get('data_id')

        # 각 모델에서 해당 데이터 조회
        selected_food = get_object_or_404(Food, pk=data_id)
        selected_cafe = get_object_or_404(Cafe, pk=data_id)
        selected_place = get_object_or_404(Place, pk=data_id)

        # Course 모델에 데이터 저장
        course = Course(
            subject=f"{selected_food.subject}, {selected_cafe.subject}, {selected_place.subject}",
            content=f"{selected_food.content}, {selected_cafe.content}, {selected_place.content}"
        )
        course.save()

        # JSON 응답 반환
        response_data = {
            'message': 'Course created successfully!',
            'course_id': course.pk  # 새로 생성된 Course의 ID 반환
        }
        return JsonResponse(response_data)

    return render(request, 'build/create_course.html')