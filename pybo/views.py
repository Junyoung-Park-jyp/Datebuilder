from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

# def index(request):
#     return HttpResponse('안녕하세요 pybo에 오신 것을 환영합니다.')

#  질문 목록 조회 구현하기

def index(request):
    """
    
    pybo 목록 출력
    """

    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # return HttpResponse('안녕하세요 blog에 오신 것을 환영합니다.')
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """

    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변 등록
    """

    question = get_object_or_404(Question, pk=question_id)
    if request.method =='POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = AnswerForm()    
    context = {'question': question, 'form': form}    
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    """
    pybo 질문 등록
    """

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()    
    context = {'form': form}    
    return render(request, 'pybo/question_form.html', context)
    

    
    