# Неймспейс и представления для Movie
from flask import request
from flask_restx import Namespace, Resource

from models import Movie, movies_schema, movie_schema
from setup_db import db

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        # Если есть ключ director_id - получаем его и выводим список фильмов. Если список пустой - выводим пустой список
        if director_id:
            movies = Movie.query.filter(Movie.director_id == director_id).all()
            return movies_schema.dump(movies), 200
        # Если есть ключ genre_id - получаем его и выводим список фильмов. Если список пустой - выводим пустой список
        elif genre_id:
            movies = Movie.query.filter(Movie.genre_id == genre_id).all()
            return movies_schema.dump(movies), 200
        # Если есть ключ year - получаем его и выводим список фильмов. Если список пустой - выводим пустой список
        elif year:
            movies = Movie.query.filter(Movie.year == year).all()
            return movies_schema.dump(movies), 200


        else:
            all_movies = Movie.query.all()
            return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        db.session.add(new_movie)
        db.session.commit()
        return movie_schema.dump(new_movie), 201, {"location": f"/movies/{new_movie.id}"}

@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = Movie.query.get(mid)
        return movie_schema.dump(movie), 200


    def put(self, mid):
        movie = Movie.query.get(mid)
        req_json = request.json
        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return movie_schema.dump(movie), 200


    def delete(self, mid):
        movie = Movie.query.get(mid)
        db.session.delete(movie)
        db.session.commit()
        return movie_schema.dump(Movie.query.get(mid)), 204

