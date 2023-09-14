from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question, Answer, Comment
from ..forms import QuestionForm, AnswerForm, CommentForm
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo 질문 추천 등록

    """

    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question_id)    

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    pybo 질문 추천 등록

    """

    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer_id)