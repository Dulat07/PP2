movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]

def is_high_score(movie):
    return movie["imdb"] > 5.5

print(is_high_score({"name": "Hitman", "imdb": 6.3, "category": "Action"}))

def movies_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

high_score_movies = movies_above_5_5(movies)
print(high_score_movies)

def movies_by_category(movies, category_name):
    return [movie for movie in movies if movie["category"].lower() == category_name.lower()]

romance_movies = movies_by_category(movies, "Romance")
print(romance_movies)

def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

average_score = average_imdb(movies)
print(average_score)

def average_imdb_by_category(movies, category_name):
    category_movies = [movie["imdb"] for movie in movies if movie["category"].lower() == category_name.lower()]
    if not category_movies:
        return 0
    return sum(category_movies) / len(category_movies)

average_romance_score = average_imdb_by_category(movies, "Romance")
print(average_romance_score)

print(is_high_score({"name": "Hitman", "imdb": 6.3, "category": "Action"}))
print(movies_above_5_5(movies))
print(movies_by_category(movies, "Romance"))
print(average_imdb(movies))
print(average_imdb_by_category(movies, "Romance"))