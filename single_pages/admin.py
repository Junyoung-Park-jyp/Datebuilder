from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import * 
# 포스트 연결 테스트
from .models import Post
# Register your models here.


admin.site.register(Restaurant,MarkdownxModelAdmin )
admin.site.register(Cafe, MarkdownxModelAdmin )
admin.site.register(Play, MarkdownxModelAdmin )
# 포스트 연결 테스트
admin.site.register(Post, MarkdownxModelAdmin )
