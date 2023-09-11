from django.db import models

# Create your models here.
#  파이썬 게시판 기능 관련 모델 만들기
#  질문 모델 만들기

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
#  질문 모델 만들기 끝

#  답변 모델 만들기 끝
class Answer(models.Model)    :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    
#  답변 모델 만들기 끝