from flask import request, url_for, redirect, flash
from services.user_service import UserService
from models.user import User



def open_user_routes(app):
    user_service = UserService()

    @app.route('/my-top-movies/create-new-user', methods=['POST'])
    def create_new_user():
        entered_username = request.form.get('username')
        entered_password = request.form.get('password')
        
        if user_service.check_if_username_exists(entered_username):
            flash('Username already exists. Please choose a different one.')
            return redirect('/my-top-movies/create-new-user')
        else:
            new_user = User(username=entered_username, hashed_password=entered_password)
            user_service.create_new_user(new_user)
            flash('User created successfully! Please log in.')
            return redirect('/my-top-movies/login')
        
