from django.contrib import admin

from .models import Question
from .models import Choice


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	search_fields = ['question_text']
	list_filter = ['pub_date']
	search_fields = ['question_text']


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)