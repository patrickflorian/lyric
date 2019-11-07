from flask import request,current_app
from flask_restplus import Resource
import uuid
from app.main.util.decorator import admin_token_required

from ..util.dto import LyricDto,Upload
from ..service.lyric_service import save_new_lyric, get_all_lyrics, get_a_lyric,update_lyric,delete_lyric
import os
from ..service import parsers
api = LyricDto.api
_lyric = LyricDto.lyric

u_api= Upload.api

@api.route('/')
class LyricList(Resource):
    @api.doc('list_of_registered_lyrics')
    @api.marshal_list_with(_lyric, envelope='data')
    @admin_token_required
    def get(self):
        """List all registered lyrics"""
        return get_all_lyrics()

    @api.response(201, 'Lyric successfully created.')
    @api.doc('create a new lyric')
    @api.expect(_lyric, validate=True)
    @admin_token_required
    def post(self):
        """Creates a new Lyric """
        data = request.json
        return save_new_lyric(data=data)

@api.route('/<public_id>')
@api.param('public_id', 'The Lyric identifier')
@api.response(404, 'Lyric not found.')
class Lyric(Resource):
    @api.doc('get a lyric')
    @api.marshal_with(_lyric)
    @admin_token_required
    def get(self, public_id):
        """get a lyric given its identifier"""
        lyric = get_a_lyric( public_id)
        if not lyric:
            api.abort(404)
        else:
            return lyric
    
    @api.doc('update existings lyric')
    @api.expect(_lyric, validate=True)
    @admin_token_required
    def put(self,public_id):
        """update existings lyric """
        data = request.json
        return update_lyric(public_id,data=data)
    
    @api.doc('delete existings lyric')
    @admin_token_required
    def delete(self,public_id):
        """delete a lyric by id"""
        return delete_lyric(public_id)
@u_api.route("/")
class file_upload(Resource):
    """ upload media files """
    @u_api.expect(parsers.file_upload)
    def post(self):
        args = parsers.file_upload.parse_args()
        
        destination = os.path.join(current_app.config.get('DATA_FOLDER'),'medias\\')
        print(destination)
        if not os.path.exists(destination):
            os.makedirs(destination)
        file_loc = '%s%s%s' % (destination ,str(uuid.uuid4()), args['file'].filename) 
        args['file'].save(file_loc)
        return { 'status' : 'Done', 'file_path' : file_loc}