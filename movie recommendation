import requests_with_caching
import json

def get_movies_from_tastedive(s):
    baseurl = 'https://tastedive.com/api/similar'
    parameters = {'q': s,'type': 'movies', 'limit': 5}
    res = requests_with_caching.get(baseurl, params = parameters)
    return res.json()

def extract_movie_titles(dic):
    return [movie['Name'] for movie in dic['Similar']['Results']]

def get_related_titles(lst):
    movies = []
    for movie in lst:
        titles = extract_movie_titles(get_movies_from_tastedive(movie))
        for movie in titles:
            if movie not in movies:
                 movies.append(movie)
    return movies


def get_movie_data(name):
    url = 'http://www.omdbapi.com/'
    params = {'t': name, 'r':'json'}
    res = requests_with_caching.get(url, params)
    return res.json() 

def get_movie_rating(ratings):
    for rating in ratings['Ratings']:
        if rating['Source'] == 'Rotten Tomatoes':
            return int(rating['Value'][:2])
    return 0

def get_sorted_recommendations(movie):
    movies = get_related_titles(movie)
    return sorted(sorted(movies), key = lambda x: get_movie_rating(get_movie_data(x)), reverse = True)
