# from django.shortcuts import render

# Create your views here.
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Rating, Watchlist
from .serializers import MovieSerializer, RatingSerializer, WatchlistSerializer

from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import generics, permissions
from django.http import Http404

from django.contrib.auth.models import User


class MovieLists(APIView):
    # permission_classes=(permissions.IsAuthenticated,)
    """
    List all movies, or create a new movie.
    """
    def get(self, request, format=None):
        
        movies= Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
   
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetails(APIView):
    """
    Retrieve, update or delete a movie instance.
    """
    def get_object(self, slug):
        try:
            return Movie.objects.get(slug=slug)
        except Movie.DoesNotExist:
            raise Http404
    def get(self, request, slug, format=None):
        movie = self.get_object(slug)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    def put(self, request, slug, format=None):
        movie = self.get_object(slug)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, slug, format=None):
        movie = self.get_object(slug)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RatingsList(APIView):
    # permission_classes=(permissions.AllowAny,)
    # Getting all the ratings list
    def get(self, request, format=None):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    # Creating a new rating
    def post(self, request, format=None):
        # AnonymousUser
        # is_anom_user = self.request.user == "AnonymousUser"
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            print(self.request.user)
            print(request.data)
            print()
            if 'author' in request.data:
                serializer.save()
            else:
                # serializer.save(author=1 if is_anom_user else self.request.user)
                serializer.save(author=self.request.user)
            # instance = serializer.save()
            # instance.author = request.user
            # instance.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get_user(self):
        
        user = self.request.user
        return user

    def perform_create(self, serializer):
        
        serializer.save(author=self.get_user())
    # Data

## ---------------------------------------------------------------------

# class MovieListView(generics.ListCreateAPIView):
    # permission_classes=(permissions.AllowAny,)
    # queryset=Movie.objects.all()
    # serializer_class= MovieSerializer

# class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Movie.objects.all()
#     serializer_class= MovieSerializer