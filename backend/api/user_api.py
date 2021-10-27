from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request, current_app

import sys
sys.path.append("..") 

from models import db, User

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
    return jsonify({ 'token': token.decode('UTF-8') })