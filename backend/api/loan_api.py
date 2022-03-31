from flask import Blueprint, jsonify, request, send_file
import uuid

import sys
sys.path.append("..") 

from models import db, Loan, Business
from utils import token_required, admin_token_required, upload_file, download_file

loans_api = Blueprint('loans', __name__)

BUCKET = "mayari-uploads"

@loans_api.route('/', methods=('POST',))
@token_required
def create_loan(user):
    data = request.form
    primary_id = request.files['primary_id']
    proof_of_income = request.files['proof_of_income']
    primary_id_url = upload_file(primary_id, BUCKET, "primary-ids/{}-{}".format(str(uuid.uuid4()),primary_id.filename))
    proof_of_income_url = upload_file(proof_of_income, BUCKET, "proofs-of-income/{}-{}".format(str(uuid.uuid4()),proof_of_income.filename))
    loan = Loan(data['requested_amount'],data['collateral_type'],data['payment_term'], primary_id_url, proof_of_income_url)
    loan.borrower = user
    business = Business(data['name'], data['street_address'], data['city'], data['zip_code'], data['industry'], 
    data['monthly_income'], data['monthly_expenses'], data['years'])
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
    business = Business.query.filter_by(loan_id=loan.id).first()
    return jsonify(loan.to_dict(), business.to_dict()), 201

@loans_api.route('/download/<folder>/<filename>/', methods=('GET',))
@token_required
def download_loan_file(user, filename, folder):
    file = download_file(filename, BUCKET, folder)
    return send_file(file, as_attachment=True)
 
@loans_api.route('/edit/<int:id>/', methods=('PUT',))
@admin_token_required
def update_loan(user, id=id):
    data = request.get_json()
    loan = Loan.query.get(data['id'])
    loan.interest_rate = data['interest_rate']
    loan.payment_term = data['payment_term'] 
    loan.principal = data['principal']
    loan.outstanding_balance = data['outstanding_balance']
    loan.overdue_balance = data['overdue_balance']
    loan.total_amount = data['total_amount']
    loan.installments = data['installments']
    loan.status = data['status']
    loan.collateral = data['collateral']
    db.session.commit()
    return jsonify(loan.to_dict()), 201

@loans_api.route('/', methods=('GET',))
@admin_token_required
def fetch_all_loans(user):
    loans = Loan.query.all()
    return jsonify([loan.to_dict() for loan in loans]), 201
