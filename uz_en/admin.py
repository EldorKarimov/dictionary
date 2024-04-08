from django.contrib import admin

from .models import EnglishWord, UzbekWord

class EnglishWordInline(admin.TabularInline):
    model = EnglishWord
    fields = ['word']

@admin.register(UzbekWord)
class UzbekWordAdmin(admin.ModelAdmin):
    inlines = [EnglishWordInline]
    list_display = ['word', 'direction', 'created', 'updated']
    search_fields = ['word']
    list_filter = ('direction',)
    fieldsets = (
        ("Uzbek Word", {"fields": ("word", "direction")}),
    )