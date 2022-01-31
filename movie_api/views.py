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


    ## ---------------------------------------------------------------------

# class MovieListView(generics.ListCreateAPIView):
    # permission_classes=(permissions.AllowAny,)
    # queryset=Movie.objects.all()
    # serializer_class= MovieSerializer

# class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Movie.objects.all()
#     serializer_class= MovieSerializer