from django.contrib import admin
from .models import Tournament, New, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'tournament')
    list_editable = ('tournament',)
    search_fields = ('text',)
    list_filter = ('pub_date', 'author')
    empty_value_display = '-пусто-'


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


class NewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text')

admin.site.register(Post, PostAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(New, NewAdmin)
