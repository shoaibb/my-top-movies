from flask import render_template, flash, get_flashed_messages, redirect, url_for, session
from services.user_movies_service import UserMoviesService

user_movies_service = UserMoviesService()

def open_page_routes(app):
    @app.route('/my-top-movies/login')
    def show_login_page():
        return render_template('login-page.html')

    @app.route('/home')
    def home():
        return render_template('home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/my-top-movies/create-new-user')
    def show_create_new_user_page():
        user_exists = get_flashed_messages()
        return render_template('create-new-user-page.html', message=user_exists)
    
    @app.route('/my-top-movies/movies')
    def show_movies_page():
        
        # Get all the movies of a user

        logged_in_user = session.get('user_id')

        if not logged_in_user:
            flash("Please log in to view your movies.")
            return redirect(url_for('show_login_page'))



        user_movies = user_movies_service.get_all_user_movies_by_id(logged_in_user)

        return render_template('movies-page.html', movies=user_movies)


    @app.route('/my-top-movies/create-new-movie', methods=['GET'])
    def show_create_new_movie_page():
        return render_template('create-new-movie-page.html')