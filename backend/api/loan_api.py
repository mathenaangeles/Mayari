from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request

import sys
sys.path.append("..") 

from models import db, Loan, Business
from utils import token_required

loans_api = Blueprint('loans', __name__)

@token_required
@loans_api.route('/', methods=('POST',))
def create_loan(user):
    data = request.get_json()
    loan = Loan(**data)
    loan.borrower = user
    business = Business(**data['business'])
    loan.business = business
    db.session.add(loan)
    db.session.commit()
    return jsonify(loan.to_dict()), 201

@token_required
@loans_api.route('/', methods=('GET',))
def fetch_loans(user_id):
    loans = Loan.query.filter_by(borrower_id=user_id).all()
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
        loan.interest_rate = data['interest_rate']
        loan.payment_term = data['payment_term'] 
        loan.principal = data['principal']
        loan.total_amount = data['total_amount']
        loan.status = data['status']
        db.session.commit()
        return jsonify(loan.to_dict()), 201
 