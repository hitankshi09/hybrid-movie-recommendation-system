import pandas as pd

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

movie_ratings = ratings.merge(movies, on="movieId")

user_movie_matrix = movie_ratings.pivot_table(
    index="userId",
    columns="title",
    values="rating"
)