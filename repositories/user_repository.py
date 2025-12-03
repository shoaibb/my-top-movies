from models.user import User
from db import db

class UserRepository:
    #create
    @classmethod
    def create_user(cls, username: str, password: str) -> User:
        new_user = User(username=username, hashed_password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    
    #read
    @classmethod
    def get_user_by_id(cls, user_id: int) -> User:
        return User.query.get(user_id)


    @classmethod
    def get_user_by_username(cls, username: str) -> User:
        return User.query.get(username)


    #update

    @classmethod
    def update_user_password(cls, user_id: int, new_hashed_password: str) -> User:
        user = User.query.get(user_id)
        user.hashed_password = new_hashed_password
        db.session.commit()

    #delete

    @classmethod
    def delete_user(cls, user_id: int) -> None:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()