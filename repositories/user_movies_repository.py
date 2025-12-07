from models.user_movies import UserMovies
from db import db

class UserMoviesRepository:
    #create
    @classmethod
    def create_user_movie(cls, user_id: int, movie_id: int) -> UserMovies:
        new_user_movie = UserMovies(user_id=user_id, movie_id=movie_id)
        db.session.add(new_user_movie)
        db.session.commit()

    #read
    @classmethod
    def get_user_movies_by_id(cls, user_movie_id: int) -> list[UserMovies]:
        return UserMovies.query.get(user_movie_id)


    @classmethod
    def get_all_user_movies_by_id(cls, user_id: int) -> list[UserMovies]:
       return UserMovies.query.filter_by(user_id=user_id).all()
    
    #delete
    @classmethod
    def delete_user_movie(cls, user_id, movie_id: int) -> None:
        user_movie = UserMovies.query.filter_by(user_id=user_id, movie_id=movie_id).first()
        if user_movie:
            db.session.delete(user_movie)
            db.session.commit()