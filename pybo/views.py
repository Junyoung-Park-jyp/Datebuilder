from django.shortcuts import render

from .models import Question

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('안녕하세요 pybo에 오신 것을 환영합니다.')

#  질문 목록 조회 구현하기

def index(request):
    """
    
    pybo 목록 출력
    """

    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # return HttpResponse('안녕하세요 blog에 오신 것을 환영합니다.')
    return render(request, 'pybo/question_list.html', context)

    