from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request

import sys
sys.path.append("..") 

from models import db, Loan
from utils import token_required

loans_api = Blueprint('loans', __name__)

@token_required
@loans_api.route('/', methods=('POST',))
def create_loan(current_user):
    data = request.get_json()
    loan = Loan(amount=data['amount'])
    loan.borrower_id = current_user
    db.session.add(loan)
    db.session.commit()
    return jsonify(loan.to_dict()), 201

@token_required
@loans_api.route('/', methods=('GET',))
def fetch_loans():
    loans = Loan.query.all()
    return jsonify([loan.to_dict() for loan in loans])

@token_required
@loans_api.route('/<int:id>/', methods=('GET','PUT'))
def fetch_loan(id):
    if request.method == 'GET':
        loan = Loan.query.get(id)
        return jsonify(loan.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        loan = Loan.query.get(data['id'])
        loan.amount = data['amount'] 
        loan.interest_rate = data['interest_rate']
        db.session.commit()
        return jsonify(loan.to_dict()), 201
 