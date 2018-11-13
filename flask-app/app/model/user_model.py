import db.db_setting as db_setting
from db.orm.user import User


class UserModel():

    def __init__(self):
        pass

    def get(self, id):
        return User.find(id).serialize()

    def get_all(self):
        return User.all().serialize()

    def create(self, name, address, email):
        user = User()
        user.name = name
        user.address = address
        user.email = email
        user.save()
