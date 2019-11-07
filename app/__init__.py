from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.lyric_controller import api as lyric_ns, u_api as upload_ns
from .main.controller.genre_controller import api as genre_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS LYRIC\'S API  WITH JWT',
          version='1.0',
          description='lyrics restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(genre_ns,path='/genre')
api.add_namespace(lyric_ns,path='/lyric')
api.add_namespace(upload_ns,path='/uploads')