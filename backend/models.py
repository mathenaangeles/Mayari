from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(255), default=u'regular_user')
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile_photo = db.Column(db.String(255), nullable=True)
    birthdate = db.Column(db.Date, nullable=True)
    street_address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    zip_code = db.Column(db.String(10), nullable=True)
    region = db.Column(db.String(255), nullable=True)
    country = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(255), nullable=True)
    marital_status = db.Column(db.String(255), nullable=True)
    loans = db.relationship("Loan", backref="borrower", cascade="all,delete", lazy=False)
    
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
                    role=self.role,
                    email=self.email, 
                    name=self.first_name + " " + self.last_name,
                    mobile_number=self.mobile_number,
                    profile_photo=self.profile_photo,
                    birthdate=self.birthdate,
                    street_address=self.street_address,
                    city=self.city,
                    zip_code=self.zip_code,
                    region=self.region,
                    country=self.country,
                    gender=self.gender,
                    marital_status=self.marital_status)


class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    borrower_id =  db.Column(db.Integer, db.ForeignKey('users.id'))
    business = db.relationship("Business",  backref="loan", cascade="all,delete", uselist=False)
    requested_amount = db.Column(db.Float, nullable=False)
    collateral_type = db.Column(db.String(255), nullable=False)
    payment_term = db.Column(db.Integer, nullable=False)
    primary_id = db.Column(db.String(255), nullable=False)
    proof_of_income = db.Column(db.String(255), nullable=False)
    collateral = db.Column(db.String(255), nullable=True)
    interest_rate = db.Column(db.Float, nullable=True)
    principal = db.Column(db.Float, nullable=True)
    total_amount = db.Column(db.Float, nullable=True)
    outstanding_balance =  db.Column(db.Float, nullable=True)
    overdue_balance = db.Column(db.Float, nullable=True)
    installments = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(255),  default=u'pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, requested_amount, collateral_type, payment_term, primary_id, proof_of_income):
        self.requested_amount = requested_amount
        self.collateral_type = collateral_type
        self.payment_term = payment_term
        self.primary_id = primary_id
        self.proof_of_income = proof_of_income

    def to_dict(self):
      return dict(id=self.id,
                  borrower_id=self.borrower_id,
                  requested_amount=self.requested_amount,
                  collateral_type=self.collateral_type,
                  collateral = self.collateral,
                  payment_term = self.payment_term,
                  primary_id = self.primary_id,
                  proof_of_income = self.proof_of_income,
                  interest_rate = self.interest_rate,
                  principal = self.principal,
                  total_amount=self.total_amount,
                  outstanding_balance = self.outstanding_balance,
                  overdue_balance = self.overdue_balance,
                  installments = self.installments,
                  status = self.status,
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
    monthly_income = db.Column(db.Float, nullable=False)
    monthly_expenses= db.Column(db.Float, nullable=False)
    years = db.Column(db.Integer, nullable=False)

    def __init__(self, name, street_address, city, zip_code, industry, monthly_income, 
    monthly_expenses, years):
        self.name = name
        self.street_address = street_address
        self.city = city
        self.zip_code = zip_code
        self.industry = industry
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        self.years = years

    def to_dict(self):
      return dict(id=self.id,
                  name=self.name,
                  industry=self.industry,
                  street_address=self.street_address,
                  city=self.city,
                  zip_code=self.zip_code)

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    preview = db.Column(db.String(255), nullable=False)
    body = db.Column(db.UnicodeText(), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    is_published = db.Column(db.Boolean,  default=False)
    is_featured = db.Column(db.Boolean,  default=False)
    preview_image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, author, title, preview, body, category):
        self.author = author
        self.title = title
        self.preview = preview
        self.body = body
        self.category = category

    def to_dict(self):
      return dict(id=self.id,
                  author=self.author,
                  title=self.title,
                  preview=self.preview,
                  body=self.body,
                  category=self.category,
                  preview_image=self.preview_image,
                  is_published=self.is_published,
                  is_featured=self.is_featured,
                  created_at=self.created_at,
                  updated_at=self.updated_at)

@db.event.listens_for(Article, 'before_update')
def article_updated_listener(mapper, connection, target):
  target.updated_at = datetime.utcnow()