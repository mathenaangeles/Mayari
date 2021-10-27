from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object("config.BaseConfig")
CORS(app, resources={r"/*":{"origins":"*"}})

from models import db
db.init_app(app)

from api import loan_api, user_api
app.register_blueprint(loan_api.loans_api, url_prefix="/loans")
app.register_blueprint(user_api.users_api, url_prefix="/users")

if __name__ == "__main__":
    app.run()