import db.db_setting as db_setting
from orator import Model
from flask_login import UserMixin


class User(UserMixin, Model):

    #__fillable__ = ['name', 'address', 'email']
    __guarded__ = ['id', 'name', 'password']

    __connection__ = 'pgsql'
    __table__ = 'user'
    __primary_key__ = 'id'

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    @classmethod
    def get(self, id):
        # return self.find(id).serialize()
        return self.find(id)

    @classmethod
    def name(self, name):
        # return self.where('name', name).first().serialize()
        return self.where('name', name).first()
