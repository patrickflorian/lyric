import uuid
import datetime

from app.main import db
from app.main.model.lyric import Genre


def save_new_genre(data):
    new_genre = Genre(
        id=str(uuid.uuid4()),
        name=data['name'],
        registered_on=datetime.datetime.utcnow(),
    )
    save_changes(new_genre)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201
    
def update_genre(id, data):
    exist_genre = Genre.query.filter(
        Genre.id == id
    ).one_or_none()

    if exist_genre is None:
        response_object = {
            'status': 'fail',
            'message': 'Genre don\'t exists.',
        }
        return response_object, 404
    else:
        updated_genre = Genre(
            id = exist_genre.id,
            name=data['name']
        )
        db.session.merge(updated_genre)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully updated.'
        }
        return response_object, 201

def delete_genre(id):
    exist_genre = Genre.query.filter(
        Genre.id == id
    ).one_or_none()

    if exist_genre is not None:
        db.session.delete(exist_genre)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully deleted.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'genre doesn\'t exist.'
        }
        return response_object, 404


def get_all_genres():
    return Genre.query.all()


def get_a_genre(id):
    return Genre.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()