from services.movie_service import MovieService
from services.user_movies_service import UserMoviesService
from flask import render_template, request, redirect, session, url_for

movie_service = MovieService()
user_movies_service = UserMoviesService()

def open_movie_routes(app):
    
    @app.route('/my-top-movies/create-new-movie', methods=['POST'])
    def create_new_movie():
        logged_in_user = session.get('user_id')
        
        movie_title = request.form.get('movie_title')
        movie_ranking = request.form.get('movie_ranking')
        
        movie_service.create_new_movie(movie_title, movie_ranking)

        added_movie = movie_service.get_movie_by_title(movie_title)

        user_movies_service.create_new_user_movie(logged_in_user, added_movie.id)

        return redirect(url_for('show_movies_page'))

    @app.route('/my-top-movies/delete-movie', methods=['POST'])
    def delete_movie():
        movie_id = request.form.get('movie_id')
        logged_in_user = session.get('user_id')

        user_movies_service.delete_user_movie(logged_in_user,movie_id)
        #movie_service.delete_movie(movie_id)
        return redirect(url_for('show_movies_page'))