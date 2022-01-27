from flask import Blueprint, jsonify, request

import sys
sys.path.append("..") 

from models import db, Loan, Business, User
from utils import token_required, admin_token_required

loans_api = Blueprint('loans', __name__)

@loans_api.route('/', methods=('POST',))
@token_required
def create_loan(user):
    data = request.get_json()
    loan = Loan(data['requested_amount'],data['collateral_type'],data['payment_term'])
    loan.borrower = user
    business = Business(**data['business'])
    loan.business = business
    db.session.add(loan)
    db.session.commit()
    return jsonify(loan.to_dict()), 201

@loans_api.route('/user/<int:id>/', methods=('GET',))
@token_required
def fetch_loans(user, id=id):
    loans = Loan.query.filter_by(borrower_id=id).all()
    return jsonify([loan.to_dict() for loan in loans]), 201

@loans_api.route('/<int:id>/', methods=('GET',))
@token_required
def fetch_loan(user, id=id):
    loan = Loan.query.get(id)
    return jsonify(loan.to_dict()), 201
 
@loans_api.route('/edit/<int:id>/', methods=('PUT',))
@admin_token_required
def update_loan(user, id=id):
    data = request.get_json()
    print(data, file=sys.stderr)
    loan = Loan.query.get(data['id'])
    loan.interest_rate = data['interest_rate']
    loan.payment_term = data['payment_term'] 
    loan.principal = data['principal']
    loan.outstanding_balance = data['outstanding_balance']
    loan.total_amount = data['total_amount']
    loan.status = data['status']
    db.session.commit()
    return jsonify(loan.to_dict()), 201

@loans_api.route('/', methods=('GET',))
@admin_token_required
def fetch_all_loans(user):
    loans = Loan.query.all()
    return jsonify([loan.to_dict() for loan in loans]), 201
