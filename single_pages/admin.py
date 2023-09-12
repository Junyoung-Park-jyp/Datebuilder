from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import * 
# Register your models here.

#admin페이지에 카테고리 추가하기
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class CourseAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content')
    list_filter = ('subject', 'content')
    search_fields = ('subject', 'content')
admin.site.register(Food,MarkdownxModelAdmin )
admin.site.register(Cafe, MarkdownxModelAdmin )
<<<<<<< HEAD
admin.site.register(Place, MarkdownxModelAdmin )
=======
admin.site.register(Food, MarkdownxModelAdmin )
admin.site.register(Place, MarkdownxModelAdmin )
admin.site.register(Play, MarkdownxModelAdmin )
>>>>>>> 3ae35e781c762579f7f6926c0b2763a9dc16067c
# 포스트 연결 테스트
admin.site.register(Post, MarkdownxModelAdmin )
#admin페이지에 카테고리, Tags 추가하기
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Course)