import bcrypt

class HashingService:
    @staticmethod
    def hash_password(password_in_plain_text: str) -> str:
        password_to_bytes = password_in_plain_text.encode('utf-8')
        salt = bcrypt.gensalt()
        hash_and_salt_the_bytes = bcrypt.hashpw(password_to_bytes, salt)
        now_a_secured_password = hash_and_salt_the_bytes.decode('utf-8')
        return now_a_secured_password

    @staticmethod
    def check_password(password_in_plain_text: str, stored_password: str) -> bool:
        return bcrypt.checkpw(password_in_plain_text.encode('utf-8'), stored_password.encode('utf-8'))
