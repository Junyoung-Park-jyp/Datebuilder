from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os
# Create your models here.

class Restaurant(models.Model):
    subject = models.CharField(max_length=40)
    content = MarkdownxField()
    create_date = models.DateTimeField()

    def get_content_markdown(self):
      return markdown(self.content)
    
    def __str__(self):
      return f'[{self.pk}] {self.subject}'
    
class Cafe(models.Model):
    subject = models.CharField(max_length=40)
    content = MarkdownxField()
    create_date = models.DateTimeField()

    def get_content_markdown(self):
      return markdown(self.content)
    
    def __str__(self):
      return f'[{self.pk}] {self.subject}'
    
class Play(models.Model):
    subject = models.CharField(max_length=40)
    content = MarkdownxField()
    create_date = models.DateTimeField()

    def get_content_markdown(self):
      return markdown(self.content)
    
    def __str__(self):
      return f'[{self.pk}] {self.subject}'