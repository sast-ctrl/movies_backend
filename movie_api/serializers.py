from rest_framework import serializers
from .models import Movie, Rating, Watchlist
from django.contrib.auth.models import User

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
    class Meta:
        fields = [
            'id',
            'title',
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

    