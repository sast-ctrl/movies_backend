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

    author = AuthorSerializer(many=False)
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

class MovieSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True)
    class Meta:
        fields = [
            'title',
            'release_date',
            'genre',
            'plot',
            'slug',
            'ratings'
        ]
        
        model = Movie



class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = Watchlist