from repositories.user_repository import UserRepository

class UserService:
    
    def __init__(self):
        self.user_repository = UserRepository()


    #CRUD reference methods
    def create_new_user(self, user):
        self.user_repository.create_user(user.username, user.hashed_password)
    
    def get_user_by_id(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)
    
    def get_user_by_username(self, username: str):
        return self.user_repository.get_user_by_username(username)
    
    def update_user(self, user):
        self.user_repository.update_user(user)

    def delete_user(self, user_id: int):
        self.user_repository.delete_user(user_id)


    #Business logic

    def check_if_username_exists(self, entered_username: str) -> bool:
        user = self.user_repository.get_user_by_username(entered_username)
        return user is not None
    