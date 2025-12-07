from repositories.user_movies_repository import UserMoviesRepository


class UserMoviesService:
    
    def __init__(self):
        self.user_movies_repository = UserMoviesRepository()



    #CRUD reference methods
    def create_new_user_movie(self, user_id: int, movie_id: int):
        self.user_movies_repository.create_user_movie(user_id, movie_id)

    def get_user_movies_by_id(self, user_movie_id: int):
        return self.user_movies_repository.get_user_movies_by_id(user_movie_id)

    def delete_user_movie(self, user_id: int, movie_id: int): 
        self.user_movies_repository.delete_user_movie(user_id, movie_id)

    def get_all_user_movies_by_id(self, user_id: int):
        return self.user_movies_repository.get_all_user_movies_by_id(user_id)

    def delete_user(self, user_id: int):
        self.user_repository.delete_user(user_id)

