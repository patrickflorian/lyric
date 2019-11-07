from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required

from ..util.dto import GenreDto
from ..service.genre_service import save_new_genre, get_all_genres, get_a_genre,update_genre

api = GenreDto.api
_genre = GenreDto.genre


@api.route('/')
@api.response(401, "not Authorized login first")
class GenreList(Resource):
    @api.doc('list_of_registered_genres', security='apikey')
    @api.marshal_list_with(_genre, envelope='data')
    @admin_token_required
    
    def get(self):
        """List all registered genres"""
        return get_all_genres()

    @api.response(201, 'Genre successfully created.')
    @api.doc('create a new genre', security='apikey')
    @api.expect(_genre, validate=True)
    @admin_token_required
    def post(self):
        """Creates a new Genre """
        data = request.json
        return save_new_genre(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Genre identifier')
@api.response(404, 'Genre not found.')
@api.response(401, "not Authorized login first")
class Genre(Resource):
    @api.doc('get a genre', security='apikey')
    @api.marshal_with(_genre)
    @admin_token_required
    def get(self, public_id):
        """get a genre given its identifier"""
        genre = get_a_genre( public_id)
        if not genre:
            api.abort(404)
        else:
            return genre
    @api.doc('update existings genre', security='apikey')
    @api.expect(_genre, validate=True)
    @api.response(201, 'Genre successfully updated.')
    @admin_token_required
    def put(self,public_id):
        """update existings genre """
        data = request.json
        return update_genre(public_id,data=data)