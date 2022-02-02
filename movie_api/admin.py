from django.contrib import admin

from .models import Movie, Rating, Watchlist

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'release_date'
    ordering = ('release_date',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'movie',)
    autocomplete_fields = ('author', 'movie',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'movie',)
    autocomplete_fields = ('author', 'movie',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)