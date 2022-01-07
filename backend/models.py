from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import ChoiceType
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    USER_ROLES = [
        (u'super_admin', u'Super Admin'),
        (u'admin', u'Admin'),
        (u'regular_user', u'Regular User'),
    ]
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(ChoiceType(USER_ROLES), default=u'regular_user')
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    street_address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    zip_code = db.Column(db.String(10), nullable=True)
    region = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(255), nullable=True)
    marital_status = db.Column(db.String(255), nullable=True)
    loans = db.relationship("Loan", backref="borrower", lazy=False)
    
    def __init__(self, email, first_name, last_name, mobile_number, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.password = generate_password_hash(password, method="sha256")

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get("email")
        password = kwargs.get("password")
        if not email or not password:
            return None
        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None
        return user

    def to_dict(self):
        return dict(id=self.id, 
                    email=self.email, 
                    name=self.first_name + self.last_name)


class Loan(db.Model):
    COLLATERAL_TYPES = [
        (u'with_collateral', u'with collateral'),
        (u'without_collateral', u'without collateral'),
    ]
    STATUS = [
        (u'pending', u'pending'),
        (u'approved', u'approved'),
        (u'rejected', u'rejected'),
    ]
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    borrower_id =  db.Column(db.Integer, db.ForeignKey('users.id'))
    business = db.relationship("Business",  backref="loan", uselist=False)
    amount = db.Column(db.Integer, nullable=False)
    collateral_type = db.Column(ChoiceType(COLLATERAL_TYPES), nullable=False)
    payment_term = db.Column(db.String(255), nullable=False)
    interest_rate = db.Column(db.Float, nullable=True)
    status = db.Column(ChoiceType(STATUS),  default=u'pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, amount, collateral_type, payment_term):
        self.amount = amount
        self.collateral_type = collateral_type
        self.payment_term = payment_term

    def to_dict(self):
      return dict(id=self.id,
                  borrower_id=self.borrower_id,
                  amount=self.amount,
                  interest_rate=self.interest_rate,
                  created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'))

class Business(db.Model):
    __tablename__ = 'business'
    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('loans.id'))
    name = db.Column(db.String(255), nullable=False)
    street_address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    zip_code = db.Column(db.String(10), nullable=True)
    industry = db.Column(db.String(255), nullable=False)
    monthly_income = db.Column(db.Integer, nullable=False)
    monthly_expenses= db.Column(db.Integer, nullable=False)
    years = db.Column(db.Integer, nullable=False)

    def to_dict(self):
      return dict(id=self.id,
                  loan_id=self.loan_id,
                  name=self.name)