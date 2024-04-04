from django.contrib import admin

from .models import EnglishWord, UzbekWord, Direction


class UzWordInline(admin.TabularInline):
    model = UzbekWord
    fields = ['uzWord']

@admin.register(EnglishWord)
class EnglishAdmin(admin.ModelAdmin):
    list_display = ['word', 'direction', 'created', 'updated']
    list_filter = ('direction', )
    search_fields = ('word', 'direction', )
    inlines = [UzWordInline]

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name', )}