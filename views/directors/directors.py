from flask_restx import Namespace, Resource

from models import Director, directors_schema, director_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors_all = Director.query.all()
        return directors_schema.dump(directors_all), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director_one = Director.query.get(did)
        return director_schema.dump(director_one), 200
