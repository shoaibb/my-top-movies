from repositories.movie_repository import MovieRepository

class MovieService:
    
    def __init__(self):
        self.movie_repository = MovieRepository()



    #CRUD reference methods
    def create_new_movie(self, movie_title, movie_ranking):
        self.movie_repository.create_movie(movie_title, movie_ranking)
    
    def get_movie_by_id(self, movie_id: int):
        return self.movie_repository.get_movie_by_id(movie_id)
    
    def get_movie_by_title(self, title: str):
        return self.movie_repository.get_movie_by_title(title)

    def update_movie(self, updated_movie):
        self.movie_repository.update_movie(updated_movie)

    def delete_movie(self, movie_id: int):
        self.movie_repository.delete_movie(movie_id)