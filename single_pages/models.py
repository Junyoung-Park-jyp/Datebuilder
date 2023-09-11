from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os
# Create your models here.

#Category 모델 제작
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "notyet"
    class Meta:
        verbose_name_plural = 'Categories'
    
#Tag 모델 제작
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "notyet"
#url주소는 차후 제작
    

#Category, Tags 사용 예시
class Restaurant(models.Model):
    subject = models.CharField(max_length=40)
    content = MarkdownxField()
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag,blank=True)
    def get_content_markdown(self):
      return markdown(self.content)
    
    def __str__(self):
      return f'[{self.pk}] {self.subject}'
    
class Cafe(models.Model):
    subject = models.CharField(max_length=40)
    content = MarkdownxField()
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

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
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    # 포스트 연결 테스트 영역


