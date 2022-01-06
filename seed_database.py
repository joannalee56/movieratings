"""Seed the database."""

import os 
import json
from random import choice, randint
from datetime import datetime
import server, model, crud

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())



# Create movies, store them in list so we can use them
# to create fake ratings later

# 'release_date': '2019-09-20'

movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    
    overview = movie["overview"]
    poster_path = movie["poster_path"]
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")
    title = movie["title"]

    new_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(new_movie)



for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here
    user = crud.create_user(email, password)

    # TODO: create 10 ratings for the user
    all_movies = model.Movie.query.all()
    # all_movies = movies_in_db
    for m in range(10):
        random_movie = choice(all_movies)
        random_rating = randint(1,5)
        rating = crud.create_rating(user,random_movie, random_rating)