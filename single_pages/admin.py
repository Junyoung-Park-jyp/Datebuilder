from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import * 
# Register your models here.

#admin페이지에 카테고리 추가하기
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Restaurant,MarkdownxModelAdmin )
admin.site.register(Cafe, MarkdownxModelAdmin )
admin.site.register(Play, MarkdownxModelAdmin )
#admin페이지에 카테고리, Tags 추가하기
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
