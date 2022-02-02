# Getting started with the project

The following project involves the use of a JSON Web Token (JWT).


## Running the server locally

Within the project directory, run:

```
pip install -r requirements.txt
```

Once you're done with that, you'll need to follow the next steps:

### Configuring the database

The current build uses PostgreSQL and if you want to use it as well, then replace the `DATABASES` configuration within the `settings.py` file (which is within the movies_backend subdir) as follows:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'ip_of_db',
        'PORT': 'num_of_port',
    }
}
```

### Applying migrations

In order to start the server, Django needs to create the tables within the database and that's called 'migration'. And we can create them using the following commands:

```
python manage.py makemigrations
python manage.py migrate
```
*Beware that you still need to be within the project directory (`manage.py` should be at your root).

### Running the server

Finally, you only need to execute this command:

```
python manage.py runserver
```

Now you'll need to follow the instructions to access the API and the Admin interface.

## Using Heroku to access the backend

The project is already linked and deployed with Heroku, this the URL:

https://movies-backend-ns.herokuapp.com/

Keep in mind that there's is no home page, so it will return an `error 404` if you just copy and paste it.

# API Instructions

Everything needs `/api/` before the following instructions. 

E.g.: In order to get the list of movies you need to add `movies/`, so the full URL will be:

```
Using Heroku: https://movies-backend-ns.herokuapp.com/api/movies/
Using local server: localhost:8000/api/movies/
```

## Movies

Get lists of movies: `movies/`

Post a new movie: `movies/`

Fields necessary
```json
{
    "title": "O'reilly",
    "release_date": "2022-01-10",
    "genre": "Documentary",
    "plot": "blah blah blah o'reilly"
}
```

Use the following to get a single movie or delete it: `movies/<str:slug>/`

*The slug is auto-generated when introducing a title. E.g.: The Last Samurai = the-last-samurai

## Users Watchlist

To access a user's watchlist or add a movie to the list: `users/pk/`

*Keep in mind that the pk is automatically retrieved from the session data. You'll just need this `users/`

E.g.: Post data
```json
{
    "movie": 2  // Movie ID   
}
```

## Ratings

Ratings list (GET) or create one (POST): `ratings/`

Single rating: `ratings/<int:pk>/`

E.g.: Post data
```json
{
    "rating": 3,
    "comment": "Nuevo Rating",
    "movie": 2,
    "created_at": "2022-01-31T07:42:56.732328Z"
}
```

## Sign up
Use `signup/`

E.g.: Post Data
```json
{
    "username" : "usuario03",
    "password" : "contra03@04",
    "password2": "contra03@04"
}
```

## Log in (Get Token)

Use `token/`

E.g.: Post Data
```json
{
    "username" : "usuario01",
    "password" : "pass01"
}
```

# Admin View

You'll need to add `admin/` to the base URL.

E.g.:
```
Using Heroku: https://movies-backend-ns.herokuapp.com/admin/
Using local server: localhost:8000/admin/
```

## Creating super user

If you're running locally, then you can create a super user with:

```
django-admin createsuperuser
```

Follow the instructions of the terminal

