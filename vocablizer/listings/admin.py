from django.contrib import admin

from listings.models import English

class EnglishAdmin(admin.ModelAdmin):
    list_display = ('word', 'meaning', 'example', 'rank', 'active', 'genre', 'created_at', 'updated_at')
    list_filter = ('active', 'rank', 'genre')
    search_fields = ('word', 'meaning', 'example')
    ordering = ['rank', 'word']
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(English, EnglishAdmin)