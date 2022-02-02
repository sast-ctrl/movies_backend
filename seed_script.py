# Libraries
import requests
import json
from movie_api.models import Movie
from movie_api.serializers import MovieSerializer

MOVIE_API_KEY = "3d68daed4d7199375af68fe9ceffca92"

# ---------------------------------------------------------
# Mode Selection 0                   1
mode = ['one_movie', 'top_rated_movies']
index_num = 1
#----------------------------------------------------------

# -------------------------------------------------------------------
if mode[index_num] == 'one_movie' : 
    base_url = "https://api.themoviedb.org/3/movie/"
    movie_id = "2"
    params = {'api_key': MOVIE_API_KEY, 'language': 'en-US'}

    response = requests.get(base_url + movie_id, params=params)
    data = dict(response.json())

    search_fields = ['title', 'release_date', 'genres', 'overview']
    movie_api_fields = ['title', 'release_date', 'genre', 'plot']

    parsed_data = {}
    for field in search_fields:
        if isinstance(data[field], list):
            parsed_data[movie_api_fields[search_fields.index(field)]] = data[field][0]['name']
        else:
            parsed_data[movie_api_fields[search_fields.index(field)]] = data[field]

    print(parsed_data)

    new_movie_serializer = MovieSerializer(data=parsed_data)

    if new_movie_serializer.is_valid():
        print('----- Saved -----')
        new_movie_serializer.save()
    else:
        print('Error')
        print(new_movie_serializer.errors)

# -------------------------------------------------------------------
elif mode[index_num] == 'top_rated_movies':
    
    base_url = "https://api.themoviedb.org/3/movie/top_rated"
    params = {'api_key': MOVIE_API_KEY, 'language': 'en-US', 'page': '1'}

    # Genre ids --------------
    genre_ids = [
        {"id":28,"name":"Action"}, 
        {"id":12,"name":"Adventure"}, 
        {"id":16,"name":"Animation"}, 
        {"id":35,"name":"Comedy"}, 
        {"id":80,"name":"Crime"}, 
        {"id":99,"name":"Documentary"}, 
        {"id":18,"name":"Drama"}, 
        {"id":10751,"name":"Family"}, 
        {"id":14,"name":"Fantasy"}, 
        {"id":36,"name":"History"}, 
        {"id":27,"name":"Horror"}, 
        {"id":10402,"name":"Music"}, 
        {"id":9648,"name":"Mystery"}, 
        {"id":10749,"name":"Romance"}, 
        {"id":878,"name":"Science Fiction"}, 
        {"id":10770,"name":"TV Movie"}, 
        {"id":53,"name":"Thriller"}, 
        {"id":10752,"name":"War"}, 
        {"id":37,"name":"Western"}]

    def get_genre_id(id_num):
        if type(id_num) is int:
            genre_dict = [x for x in genre_ids if x['id'] == id_num]
            return genre_dict[0]['name']
        elif id_num.isnumeric():
            id_num = int(id_num)
            genre_dict = [x for x in genre_ids if x['id'] == id_num]
            return genre_dict[0]['name']
        else:
            print("Error - Non Valid Genre ID field")
            raise ValueError


    response = requests.get( base_url, params=params )

    raw_data = dict(response.json())
    print(raw_data['results'][0]['genre_ids'])

    # Printing sections for page 1
    loop_range = 2
    # loop_range = len(raw_data['results'])
    search_fields = ['title', 'release_date', 'genre_ids', 'overview']
    movie_api_fields = ['title', 'release_date', 'genre', 'plot']

    parsed_data = {}
    for movie in range( loop_range ):
        for field in search_fields:
            if isinstance(raw_data['results'][movie][field], list):
                parsed_data[movie_api_fields[search_fields.index(field)]] = get_genre_id( raw_data['results'][movie][field][0] )
            else:
                parsed_data[movie_api_fields[search_fields.index(field)]] = raw_data['results'][movie][field]
        
        # print(parsed_data)
        parsed_data.clear()

    # ----------------------------------------------------
    # Doing the same with pages included
    pages = ['1', '2', '3', '4', '5']
    for page in pages:
        params['page'] = page
        response = requests.get( base_url, params=params)
        raw_data.clear()
        raw_data = dict( response.json() )
        
        loop_range = 3
        # loop_range = len(raw_data['results'])
        search_fields = ['title', 'release_date', 'genre_ids', 'overview']
        movie_api_fields = ['title', 'release_date', 'genre', 'plot']

        parsed_data = {}
        for movie in range( loop_range ):
            for field in search_fields:
                if isinstance(raw_data['results'][movie][field], list):
                    parsed_data[movie_api_fields[search_fields.index(field)]] = get_genre_id( raw_data['results'][movie][field][0] )
                else:
                    parsed_data[movie_api_fields[search_fields.index(field)]] = raw_data['results'][movie][field]

            # Saving to the database
            all_movies_serializer = MovieSerializer(data=parsed_data)
            if all_movies_serializer.is_valid():
                print('----- Saved -----')
                all_movies_serializer.save()
            else:
                print('Error')
                print(all_movies_serializer.errors)
            # print(parsed_data)
            parsed_data.clear()