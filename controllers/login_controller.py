from flask import render_template, request, redirect, url_for, session, flash
from services.user_service import user_service
from services.hashing_service import HashingService

hashing_service = HashingService()

def open_login_routes(app):
    @app.route('/attempt-login', methods=['POST'])
    def attempt_login():
            entered_username = request.form.get('username')
            entered_password = request.form.get('password')
            
            found_user = user_service.get_user_by_username(entered_username)
            if found_user is None:
                flash("Login failed: User not found")
                return redirect(url_for('show_login_page'))
            else:
                if hashing_service.check_password(entered_password, found_user.hashed_password):
                     session['user_id'] = found_user.id


                     return redirect(url_for('show_movies_page'))
                else:
                    flash("Login failed: Incorrect password")
                    return redirect(url_for('show_login_page'))
    
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('show_login_page'))