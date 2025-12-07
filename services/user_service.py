from models.user import User
from db import db

class UserService:
    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()
    
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)
    
    def create_user(self, username, password_hash):
        user = User(username=username, password=password_hash)
        db.session.add(user)
        db.session.commit()
        return user
    
    def check_if_username_exists(self, username):
        return User.query.filter_by(username=username).first() is not None

    def create_new_user(self, user):
        db.session.add(user)
        db.session.commit()
        return user
    
user_service = UserService()