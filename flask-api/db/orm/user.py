from orator import Model


class User(Model):

    __fillable__ = ['name', 'address', 'email']
    __guarded__ = ['id']

    __connection__ = 'pgsql'
    __table__ = 'user'
    __primary_key__ = 'id'
