from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os
# Create your models here.

class Restaurant(models.Model):
    subject = models.CharField(max_length=40)
    content = MarkdownxField()
    create_date = models.DateTimeField(auto_now_add=True)

    def get_content_markdown(self):
      return markdown(self.content)
    
    def __str__(self):
      return f'[{self.pk}] {self.subject}'
    
class Cafe(models.Model):
    subject = models.CharField(max_length=40)
    content = MarkdownxField()
    create_date = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
=======
    updated_date = models.DateTimeField(auto_now=True)
>>>>>>> ea3eb31283cdcccdfbb67f50688bd060e7c9f398

    def get_content_markdown(self):
      return markdown(self.content)
    
    def __str__(self):
      return f'[{self.pk}] {self.subject}'
    
class Play(models.Model):
    subject = models.CharField(max_length=40)
    content = MarkdownxField()
    create_date = models.DateTimeField(auto_now_add=True)

    def get_content_markdown(self):
      return markdown(self.content)
    
    def __str__(self):
      return f'[{self.pk}] {self.subject}'
    # 포스트 연결 테스트 영역
class Post(models.Model):
   title = models.CharField(max_length=30)
   content = models.TextField()

   created_at = models.DateTimeField(auto_now_add=True, null=True)
   updated_date = models.DateTimeField(auto_now=True, null=True)

   def __ste__(self):
      return f'[{self.pk}]{self.title}'
    # 포스트 연결 테스트 영역

