from django.contrib import admin

from listings.models import English
from listings.models import Example

class EnglishAdmin(admin.ModelAdmin):
    list_display = ('word', 'id', 'meaning', 'rank', 'active', 'genre', 'created_at', 'updated_at')
    list_filter = ('active', 'rank', 'genre')
    search_fields = ('word', 'meaning')
    ordering = ['rank', 'word']
    readonly_fields = ('created_at', 'updated_at')

class ExampleAdmin(admin.ModelAdmin):
    list_display = ('example', 'english', 'created_at', 'updated_at')
    search_fields = ('english', 'example')
    ordering = ['english', 'example']
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(English, EnglishAdmin)
admin.site.register(Example, ExampleAdmin)