from rest_framework import serializers
from .models import Movie, Rating, Watchlist
from django.contrib.auth.models import User

from django.db.models import Avg # for avg_rating

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = [
            'id',
            'username'
        ]

        model = User

class RatingSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=False, read_only=True)
    class Meta:
        fields = [
            'id',
            'author',
            # No movie
            'rating',
            'comment',
            'created_at'
        ]

        model = Rating

class RatingSaveSerializer(serializers.ModelSerializer):

    # author = AuthorSerializer(many=False, read_only=True)
    class Meta:
        fields = [
            'id',
            'author',
            'movie',
            'rating',
            'comment',
            'created_at'
        ]

        model = Rating

class MovieSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()

    def get_avg_rating(self, ob):
        return ob.ratings.all().aggregate(Avg('rating'))['rating__avg'] or 0
    class Meta:
        fields = [
            'id',
            'title',
            'avg_rating',
            'release_date',
            'genre',
            'plot',
            'slug',
            'ratings'
        ]
        
        model = Movie

class WatchlistMovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'title',
        ]
        
        model = Movie

class WatchlistSerializer(serializers.ModelSerializer):
    movie = WatchlistMovieSerializer(many=False, read_only=True)
    class Meta:
        fields = [
            'id',
            'movie',
            'created_at'
        ]
        model = Watchlist

class WatchlistUserSerializer(serializers.ModelSerializer):
    # movie = WatchlistMovieSerializer(many=False, read_only=True)
    class Meta:
        fields = [
            'id',
            'movie',
            'created_at'
        ]
        model = Watchlist

class AuthorWatchlistSerializer(serializers.ModelSerializer):
    # Text
    watchlist = WatchlistSerializer(many = True, read_only=True)
    class Meta:
        fields = [
            'id',
            'username',
            'watchlist'
        ]
        model = User

    