from flask import request, url_for, redirect, flash
from services.user_service import user_service
from services.hashing_service import HashingService
from models.user import User



def open_user_routes(app):
    hashing_service = HashingService()
    @app.route('/my-top-movies/create-new-user', methods=['POST'])
    def create_new_user():
        entered_username = request.form.get('username')
        entered_password = request.form.get('password')
        
        if user_service.check_if_username_exists(entered_username):
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('show_create_new_user_page'))
        else:
            secured_password = hashing_service.hash_password(entered_password)
            new_user = User(username=entered_username, hashed_password=secured_password)
            user_service.create_new_user(new_user)
            return redirect(url_for('show_login_page'))

