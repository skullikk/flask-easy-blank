# Неймспейс и представления для Genre
from flask_restx import Namespace, Resource

from models import Genre, genres_schema, genre_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres_all = Genre.query.all()
        return genres_schema.dump(genres_all), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre_one = Genre.query.get(gid)
        if genre_one:
            return genre_schema.dump(genre_one), 200
        else:
            return genre_schema.dump(genre_one), 404
