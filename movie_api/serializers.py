from rest_framework import serializers
from .models import Movie, Rating, Watchlist

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        
        model = Movie

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = Rating

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

        model = Watchlist