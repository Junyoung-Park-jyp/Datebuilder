from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import *
# Register your models here.

admin.site.register(Restaurant,MarkdownxModelAdmin )
admin.site.register(Cafe, MarkdownxModelAdmin )
admin.site.register(Play, MarkdownxModelAdmin )