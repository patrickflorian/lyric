from flask_restplus import Api
from flask import Blueprint,url_for

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.lyric_controller import api as lyric_ns, u_api as upload_ns
from .main.controller.genre_controller import api as genre_ns


blueprint = Blueprint('api', __name__)

# Authorizationo dictionnary
authorizations={
    'apikey':{
        'in':'header',
        'type':'apiKey',
        'name':'Authorization',
    }
}
class MyApi(Api):
    @property
    def specs_url(self):
        """ Monkey patch for HTTPS"""
        scheme = 'https' if 'https' in self.base_url else 'http'
        return url_for(self.endpoint('specs'),_external=True, _scheme=scheme)

description="this is <b> Lyrics</b> API .All request in regards to the application can be found here, in general most of the methods require you being as an active user to be able to access"

api = MyApi(blueprint,
          doc='/doc/',
          title=' LYRIC\'S API',
          version='1.0',
          authorizations=authorizations,
          description=description,
          default='auth',
          default_label='lyrics related operations'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(genre_ns,path='/genre')
api.add_namespace(lyric_ns,path='/lyric')
api.add_namespace(upload_ns,path='/uploads')