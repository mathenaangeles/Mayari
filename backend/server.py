from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config.BaseConfig")
CORS(app)

from models import db
db.init_app(app)
with app.app_context():
    db.create_all()

migrate = Migrate(app, db, render_as_batch=True)

from api import loan_api, user_api, article_api
app.register_blueprint(loan_api.loans_api, url_prefix="/loans")
app.register_blueprint(user_api.users_api, url_prefix="/users")
app.register_blueprint(article_api.articles_api, url_prefix="/articles")
@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"
if __name__ == "__main__":
    app.run()