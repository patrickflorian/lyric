import uuid
import datetime

from sqlalchemy import update
from app.main import db

from app.main.model.lyric import Lyric



def save_new_lyric(data):
    new_lyric = Lyric(
        id=str(uuid.uuid4()),
        title=data['title'],
        content=data['content'],
        audio=data['audio'],
        image=data['image'],
        registered_on=datetime.datetime.utcnow(),
        public_id=str(uuid.uuid4()),
        genre_id= data["genre_id"]
    )
    save_changes(new_lyric)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201

def update_lyric(id, data):
    exist_lyric = Lyric.query.filter(
        Lyric.id == id
    ).one_or_none()

    if exist_lyric is None:
        response_object = {
            'status': 'fail',
            'message': 'Lyric don\'t exists.',
        }
        return response_object, 404
    else:
        updated_lyric = Lyric(
            id = exist_lyric.id,
            title=data['title'],
            content=data['content'],
            audio=data['audio'],
            image=data['image'],
            registered_on=datetime.datetime.utcnow(),
            public_id=str(uuid.uuid4()),
            genre_id= data["genre_id"]
        )
        db.session.merge(updated_lyric)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully updated.'
        }
        return response_object, 201

def delete_lyric(id):
    exist_lyric = Lyric.query.filter(
        Lyric.id == id
    ).one_or_none()

    if exist_lyric is not None:
        db.session.delete(exist_lyric)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lyric doesn\'t exist.'
        }
        return response_object, 404


def get_all_lyrics():
    return Lyric.query.all()


def get_a_lyric(id):
    return Lyric.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()