from functools import wraps
from flask import jsonify, request, current_app
import jwt
import boto3

import sys
sys.path.append("..") 

from models import User

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()
        invalid_msg = {
            'message': 'Invalid token...',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token...',
            'authenticated': False
        }
        missing_headers = {
            'message': 'Invalid headers...',
            'authenticated': False
        }
        if len(auth_headers) != 2:
            return jsonify(missing_headers), 400
        try:
            token = auth_headers[1]
            data = jwt.decode(token, 'whorunthehelloworld',  algorithms=['HS256'])
            user = User.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User could not be found.')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 
        except (jwt.InvalidTokenError) :
            return jsonify(invalid_msg), 401
    return _verify

def admin_token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()
        invalid_msg = {
            'message': 'Invalid token...',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token...',
            'authenticated': False
        }
        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401
        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'],  algorithms=['HS256'])
            user = User.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User could not be found.')
            if user.role != 'admin':
                return jsonify(invalid_msg), 401
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 
        except (jwt.InvalidTokenError, Exception) as e:
            return jsonify(invalid_msg), 401
    return _verify

def upload_file(file, bucket, key):
    s3_client = boto3.client('s3',
        aws_access_key_id=current_app.config['AWS_ACCESS_KEY'],
        aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
        region_name = current_app.config['REGION_NAME'])
    s3_client.upload_fileobj(file, bucket, key)
    file_url = 'https://%s.s3.amazonaws.com/%s' % (bucket, key)
    return file_url

def download_file(file, bucket, folder):
    s3 = boto3.resource('s3', 
        aws_access_key_id=current_app.config['AWS_ACCESS_KEY'],
        aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'],
        region_name = current_app.config['REGION_NAME'])
    output = f"/{folder}/{file}"
    key = f"{folder}/{file}"
    s3.meta.client.download_file(bucket, key, file)
    return output