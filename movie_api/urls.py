from django.urls import path
from .views import MovieLists, MovieDetails # , MovieLists, MovieDetails

urlpatterns = [
    path('movies/', MovieLists.as_view()),
    path('movies/<slug:slug>/', MovieDetails.as_view(), name='movie_detail'),

    # path('api_movies/', MovieLists.as_view(), name='movie_details'),
    # path('api_movies/<slug:slug>', MovieDetail.as_view())
]