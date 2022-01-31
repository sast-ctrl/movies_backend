from rest_framework import serializers
from .models import Movie, Rating, Watchlist
from django.contrib.auth.models import User


from django.db.models import Avg # for avg_rating

from django.contrib.auth.password_validation import validate_password

class SignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password" : "Password fields didn't match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

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

    