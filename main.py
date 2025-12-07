from flask import Flask
from controllers.page_controller import open_page_routes
from controllers.user_controller import open_user_routes
from controllers.login_controller import open_login_routes
from controllers.movie_controller import open_movie_routes
from models.user import User
from models.movie import Movie
from models.user_movies import UserMovies
from dotenv import load_dotenv
import os
from db import db

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')

    # configure
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['APP_SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = app.config['APP_SECRET_KEY']

    # initialize database
    db.init_app(app)

    # create tables and open routes
    with app.app_context():
        db.create_all()
    open_page_routes(app)
    open_user_routes(app)
    open_login_routes(app)
    open_movie_routes(app)
    return app


# run application
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
