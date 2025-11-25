from flask import Flask
from controllers.page_controller import open_page_routes
from dotenv import load_dotenv
import os
from db import db

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)

    # configure
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

    # initialize database
    db.init_app(app)

    # create tables and open routes
    with app.app_context():
        db.create_all()

    open_page_routes(app)

    return app

# run application
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
