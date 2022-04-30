from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class PostAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'get_photo', 'category', 'data_ad', 'urlmov', 'views', 'slug','released', 'director', 'side', 'actors', 'genre', 'translation', 'quality', 'rateKP', 'rateIMDB')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    readonly_fields = ('views', 'data_ad', 'get_photo')
    fields = ('title', 'logo', 'get_photo', 'category', 'data_ad', 'urlmov', 'views', 'slug', 'content', 'released', 'director', 'side', 'actors', 'genre', 'translation', 'quality', 'rateKP', 'rateIMDB')

    def get_photo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="50">')
        return '-'
    get_photo.short_description = 'Фото'


admin.site.register(Post, PostAdmin)
admin.site.register(Quality)

admin.site.register(Category)
# admin.site.register(Tag)


