from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request, current_app

import sys
import jwt
sys.path.append("..") 

from models import db, User
from utils import token_required

users_api = Blueprint('users', __name__)

@users_api.route('/register/', methods=('POST',))
def register():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@users_api.route('/login/', methods=('POST',))
def login():
    data = request.get_json()
    user = User.authenticate(**data)
    if not user:
        return jsonify({ 'message': 'Invalid credentials...', 'authenticated': False }), 401
    token = jwt.encode({
        'sub': user.email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({ 'token': token })

@token_required
@users_api.route('/<int:id>/', methods=('GET','PUT'))
def update_user(id):
    if request.method == 'GET':
        user = User.query.get(id)
        return jsonify(user.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        user = User.query.get(data['id'])
        user.birthdate = data['birthdate']
        user.street_address = data['street_address'] 
        user.city = data['city']
        user.zip_code = data['zip_code']
        user.region = data['region']
        user.country = data['country']
        user.gender = data['gender']
        user.marital_status = data['marital_status']
        db.session.commit()
        return jsonify(user.to_dict()), 201