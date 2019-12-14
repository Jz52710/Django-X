from django.contrib import admin
from .models import Question,Choice
from django.utils.html import format_html
from django.db import models
import random

# admin.site.register(Question)
# admin.site.register(Choice)
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    max_num = 3
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    创建question模型的后台
    """
    # pass
    list_display = ("question_text",'pub_date')
    search_fields = ('questions_text',)
    inlines = [ChoiceInline,]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    color_code = models.CharField(max_length=6)
    """
    创建choice模型的后台
    """
    # pass
    def list_votes(self,obj):
        return format_html('<div style="color:pink">%s</div>'%(str(obj.votes)+'个'))#表格数字加单位
    list_display = ("choice_text",'list_votes')
    search_fields = ('choice_text',)
    list_filter = ('question',)

