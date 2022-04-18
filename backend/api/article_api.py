from flask import Blueprint, jsonify, request
import uuid

import sys
sys.path.append("..") 

from models import db, Article
from utils import token_required, admin_token_required, upload_file

articles_api = Blueprint('articles', __name__)

BUCKET = "mayari-uploads"

@articles_api.route('/', methods=('POST',))
@admin_token_required
def create_article(user):
    data = request.form
    article = Article(data['author'],data['title'],data['preview'],data['body'],data['category'])
    if data['is_published']=='true':
        article.is_published=True
    if data['is_featured']=='true':
        article.is_featured=True
    if 'preview_image' in request.files:
        preview_image = request.files['preview_image']
        preview_image_url = upload_file(preview_image, BUCKET, "preview-images/{}".format(preview_image.filename))
        article.preview_image = preview_image_url
    db.session.add(article)
    db.session.commit()
    return jsonify(article.to_dict()), 201

@articles_api.route('/published/', methods=('GET',))
def fetch_articles():
    articles = Article.query.filter_by(is_published=True).all()
    return jsonify([article.to_dict() for article in articles]), 201

@articles_api.route('/<int:id>/', methods=('GET',))
def fetch_article(id=id):
    article = Article.query.get(id)
    return jsonify(article.to_dict()), 201
 
@articles_api.route('/edit/<int:id>/', methods=('PUT',))
@admin_token_required
def update_article(user, id=id):
    data = request.form
    article = Article.query.get(id)
    article.author = data['author']
    article.title = data['title'] 
    article.preview = data['preview']
    article.body = data['body']
    article.category = data['category']
    article.is_published = data['is_published']
    article.is_featured = data['is_featured']
    if 'preview_image' in request.files:
        preview_image = request.files['preview_image']
        preview_image_url = upload_file(preview_image, BUCKET, "preview-images/{}".format(preview_image.filename))
        article.preview_image = preview_image_url
    db.session.commit()
    return jsonify(article.to_dict()), 201

@articles_api.route('/', methods=('GET',))
@admin_token_required
def fetch_all_articles(user):
    articles = Article.query.all()
    return jsonify([article.to_dict() for article in articles]), 201

@articles_api.route('/delete/<int:id>/', methods=('DELETE',))
@admin_token_required
def delete_article(user, id=id):
    article = Article.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return 201