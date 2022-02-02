<h1>Table of contents:</h1>

- [Getting started with the project](#getting-started-with-the-project)
  - [Running the server locally](#running-the-server-locally)
    - [Configuring the database](#configuring-the-database)
    - [Applying migrations](#applying-migrations)
    - [Running the server](#running-the-server)
  - [Using Heroku to access the backend](#using-heroku-to-access-the-backend)
- [API Instructions](#api-instructions)
  - [Movies](#movies)
  - [Users Watchlist](#users-watchlist)
  - [Ratings](#ratings)
  - [Sign up](#sign-up)
  - [Log in (Get Token)](#log-in-get-token)
- [Admin site](#admin-site)
  - [Creating super user](#creating-super-user)
  - [View after logging in](#view-after-logging-in)
  - [Interacting with the Admin site](#interacting-with-the-admin-site)
    - [Creating a new user](#creating-a-new-user)
      - [From admin site](#from-admin-site)
      - [Through the `Users` admin site](#through-the-users-admin-site)
    - [Editing a user](#editing-a-user)
    - [Deleting a user](#deleting-a-user)
    - [Other options](#other-options)
- [Front-end user site](#front-end-user-site)
- [Seeding the database](#seeding-the-database)
  - [Executing the script locally](#executing-the-script-locally)
  - [Executing the script on heroku](#executing-the-script-on-heroku)

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

The project is already linked and deployed with Heroku, this is the URL:

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

**Get** lists of movies: `movies/`

**Post** a new movie: `movies/`

Fields necessary
```json
{
    "title": "O'reilly",
    "release_date": "2022-01-10",
    "genre": "Documentary",
    "plot": "blah blah blah o'reilly"
}
```

Use the following to **get** a single movie, update it (method=`PUT`) or **delete** it: `movies/<str:slug>/`

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

# Admin site

You'll need to add `admin/` to the base URL.

E.g.:
```
Using Heroku: https://movies-backend-ns.herokuapp.com/admin/
Using local server: localhost:8000/admin/
```

This should be the expected output if you're not logged in:

![django-admin-log-in](https://drive.google.com/uc?export=view&id=1UvQ1IcgRzPIJ6Jamf3VzCmPgj57yNkq1)

## Creating super user

If you're running locally, then you can create a super user with:

```
django-admin createsuperuser
```

Follow the instructions of the terminal (you can leave the email field empty).

## View after logging in

You'll be welcomed by the Django default Admin site:

![django-admin-view-image](https://drive.google.com/uc?export=view&id=1FD8ofIbSfbRrNoxuPTPXC8AGZAavU8Yp)

As you can see, we have the four categories we're interested in:

- Users
- Movies
- Ratings
- Watchlists

## Interacting with the Admin site

You can easily add a new entry by clicking the (:heavy_plus_sign:`Add`) option.

For other options, you can click the name of what you're interested.
E.g.: For checking the `users` then click either `Users` or the `Change` that's within the `Users` row.

### Creating a new user

#### From admin site

Click (:heavy_plus_sign:`Add`) that's within the `Users` row. You'll see the following output:

![django-admin-create-new-user](https://drive.google.com/uc?export=view&id=1UIjPoOMzsbgPWoilfihBliADTNoHiKGD)

By this point, you only need to fill the form and save.

<hr style="border-bottom:1px dashed">

#### Through the `Users` admin site

Click `Users` (Within the Authentication and authorization section) and you'll see the following output:

![django-admin-user-view](https://drive.google.com/uc?export=view&id=1yiGCWewQYojUL8eMvBLXYuoZ_IVO9QpH)

What you're seeing is something that we'll call the "`user admin site`". Now click "Add user", fill and save.

### Editing a user

From within the "`user admin site`", just click any user you'd like to edit and this will be output:

![django-admin-edit-user](https://drive.google.com/uc?export=view&id=1bSvA4XAqojtZPFgO7MCumFsHNb6QdKke)

Change whatever you want.

### Deleting a user

From witih the "`user admin site`":
- Click the checkbox that's beside the user you want to delete
- In the **Action** dropdown menu, select *Delete selected users*.
- Click **Go**.
- Confirm.

This will be what it'll look like after following the first to steps:

![django-admin-delete-user](https://drive.google.com/uc?export=view&id=1aEgAO2lCxhtVIurOk1n1VOOzYjXvGQLS)

### Other options

You can use the previous instructions for any other thing you're interested.

E.g.: Following the instructions with `Movies` in order to create a new movie should take you to this site

![django-admin-create-movie](https://drive.google.com/uc?export=view&id=1n7B3-JQtxGSCU4q1cdJ-KksWdp6WdhM7)

# Front-end user site

The frontend has also been deployed on heroku, [click here](https://movie-frontend-ns.herokuapp.com) and you'll see the home page:

![django-frontend-site](https://drive.google.com/uc?export=view&id=1ZzN41MXDjnKkKAMVvkZOXVejzgUDhV3D)

The aforementioned is also on Github, [click here](https://github.com/sast-ctrl/movies_frontend) to go the repository and check the details.

# Seeding the database

In order to fill the database with movies information, [themoviedb](https://www.themoviedb.org/) API is used with a local script called '`seed_script.py'`. But the current version of the script does not handle the "duplicated item" error, so you need to delete all the movies before doing a seed.

## Executing the script locally

Type and run the following command from within the project directory:

```
python manage.py shell
```

Now, within the shell, type and run this command:

```py
exec( open('seed_script.py').read() )
```

It outputs '-----Saved-----' per each successful upload.

## Executing the script on heroku

When you've created the app for the backend, you can click on '**More**' to get access to the console (click `Run console`):

![django-heroku](https://drive.google.com/uc?export=view&id=14RMvkhzk3f5X1y15oBiIpaSyD8NfvBOq)

Now you just need to type and run this on the bash:

```
python manage.py shell
```

And execute this line on the shell:

```py
exec( open('seed_script.py').read() )
```
