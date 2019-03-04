from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.site.register(Question);

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Content',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)