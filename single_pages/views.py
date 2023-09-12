<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.views.generic import *
from django.http import JsonResponse
import json
=======
from django.shortcuts import render
from .models import Post, Cafe, Food, Place
from django.views.generic import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
>>>>>>> 3ae35e781c762579f7f6926c0b2763a9dc16067c

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

<<<<<<< HEAD
=======
# 포스트 연결하기 테스트

# def food(request):
#     return render(request, 'single_pages/food.html')

# def cafe(request):
#     return render(request, 'single_pages/cafe.html')

# def place(request):
#     return render(request, 'single_pages/place.html')

>>>>>>> 3ae35e781c762579f7f6926c0b2763a9dc16067c
def review(request):
    return render(request, 'build/review.html')

def date_course(request):
<<<<<<< HEAD
    return render(request, 'build/date_course.html')

def cafe_detail(request):
    return render(request, 'single_pages/cafe_detail.html')

def food_detail(request):
    return render(request, 'single_pages/food_detail.html')

def place_detail(request):
    return render(request, 'single_pages/place_detail.html')
=======
    return render(request, 'single_pages/date_course.html')
>>>>>>> 3ae35e781c762579f7f6926c0b2763a9dc16067c


class CafeList(ListView):
    model = Cafe
    template_name = "single_pages/cafe.html"
    context_object_name = "cafes"
<<<<<<< HEAD
=======
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

>>>>>>> 3ae35e781c762579f7f6926c0b2763a9dc16067c

class FoodList(ListView):
    model = Food
    template_name = "single_pages/food.html"
    context_object_name = "foods"
<<<<<<< HEAD
=======
    ordering = '-pk'
>>>>>>> 3ae35e781c762579f7f6926c0b2763a9dc16067c

class PlaceList(ListView):
    model = Place
    template_name = "single_pages/place.html"
    context_object_name = "places"
<<<<<<< HEAD

# def create_course(request):
#     if request.method == 'GET':
#         # 클라이언트에서 전달한 데이터 ID 가져오기
#         data_id = request.GET.get('data_id')

#         # 각 모델에서 해당 데이터 조회
#         selected_food = get_object_or_404(Food, pk=data_id)
#         selected_cafe = get_object_or_404(Cafe, pk=data_id)
#         selected_place = get_object_or_404(Place, pk=data_id)

#         # Course 모델에 데이터 저장
#         course = Course(
#             subject=f"{selected_food.subject}, {selected_cafe.subject}, {selected_place.subject}",
#             content=f"{selected_food.content}, {selected_cafe.content}, {selected_place.content}"
#         )
#         course.save()

#         # JSON 응답 반환
#         response_data = {
#             'message': 'Course created successfully!',
#             'course_id': course.pk  # 새로 생성된 Course의 ID 반환
#         }
#         return JsonResponse(response_data)

#     return render(request, 'build/create_course.html')

from django.http import JsonResponse
import json

def create_course(request):
    if request.method == 'POST':
        # 클라이언트에서 전달한 데이터 ID 배열 가져오기
        data_ids = json.loads(request.body)

        # 선택한 데이터 ID 배열을 저장할 리스트
        selected_data = []

        # 각 데이터 ID를 순회하며 객체를 조회하고 selected_data에 추가
        for data_id in data_ids:
            selected_cafe = get_object_or_404(Cafe, pk=data_id)
            selected_food = get_object_or_404(Food, pk=data_id)
            selected_place = get_object_or_404(Place, pk=data_id)

            selected_data.append({
                'cafe_subject': selected_cafe.subject,
                'cafe_content': selected_cafe.content,
                'food_subject': selected_food.subject,
                'food_content': selected_food.content,
                'place_subject': selected_place.subject,
                'place_content': selected_place.content,
            })

        # Course 모델에 데이터 저장
        course = Course.objects.create(
            subject=", ".join([f"{data['cafe_subject']}, {data['food_subject']}, {data['place_subject']}" for data in selected_data]),
            content=", ".join([f"{data['cafe_content']}, {data['food_content']}, {data['place_content']}" for data in selected_data]),
        )

        # JSON 응답 반환
        response_data = {
            'message': 'Course created successfully!',
            'course_id': course.pk  # 새로 생성된 Course의 ID 반환
        }
        return JsonResponse(response_data)

    return render(request, 'single_pages/create_course.html')
=======
    ordering = '-pk'
>>>>>>> 3ae35e781c762579f7f6926c0b2763a9dc16067c
