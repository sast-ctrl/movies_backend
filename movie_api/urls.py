from django.urls import path
from .views import MovieLists, MovieDetails, RatingsList, RatingsDetails, UserDetails, UserWatchlistList#, MovieListView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('movies/', MovieLists.as_view()),
    path('movies/<str:slug>/', MovieDetails.as_view(), name='movie_detail'),

    path('ratings/', RatingsList.as_view()),
    path('ratings/<int:pk>/', RatingsDetails.as_view()),

    path('users/', UserWatchlistList.as_view()),
    path('users/<int:pk>/', UserDetails.as_view(), name='user_detail'),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api_movies/', MovieListView.as_view(), name='movie_details'),
    # path('api_movies/<slug:slug>', MovieDetail.as_view())
]