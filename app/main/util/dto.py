from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class LyricDto:
    api = Namespace('lyric', description="lyrics related operations")
    lyric = api.model('lyric', {
        'title': fields.String(required=True, description='The lyric title'),
        'content': fields.String(required=True, description='The lyric text content'),
        'audio': fields.String(required=False, description='the lyric audio file'),
        'image': fields.String(required=False, description='the lyric related image'),
        'id':fields.String(description="lyric identifier"),
        'genre_id': fields.String(description="lyric's genre")
    })

class GenreDto:
    api = Namespace('genre', description="genre related operations")
    genre = api.model('genre', {
        'name': fields.String(required=True, description='The genre title'),
        'id':fields.String(description="genre identifier")
    })

class Upload:
    api = Namespace('upload', description="lyric's media (image and audio) upload ")