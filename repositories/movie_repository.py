from models.movie import Movie
from db import db

class MovieRepository:
    #create
    @classmethod
    def create_movie(cls, title: str, ranking: int) -> Movie:
        new_movie = Movie(title=title, ranking=ranking)
        db.session.add(new_movie)
        db.session.commit()
    
    
    #read
    @classmethod
    def get_movie_by_id(cls, movie_id: int) -> Movie:
        return Movie.query.get(movie_id)


    @classmethod
    def get_movie_by_title(cls, title: str) -> Movie:
        return Movie.query.filter_by(title=title).first()


    #update

    @classmethod
    def update_movie(cls, updated_movie: Movie) -> Movie:
        old_movie = Movie.query.get(updated_movie.id)
        old_movie.title = updated_movie.title
        old_movie.ranking = updated_movie.ranking
        db.session.commit()


    #delete

    @classmethod
    def delete_movie(cls, movie_id: int) -> None:
        movie = Movie.query.get(movie_id)
        db.session.delete(movie)
        db.session.commit()