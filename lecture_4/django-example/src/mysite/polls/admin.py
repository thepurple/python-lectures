"""
Poll admin setting
"""
from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    """
    Choice admin settings
    """
    list_display = ('question', 'choice_text', 'votes')
    ordering = ('question', 'choice_text',)

    list_filter = ('question', )
    exclude = ('votes', )
