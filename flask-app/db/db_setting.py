from orator import DatabaseManager
from orator import Model

import db.db_conf as db_conf

dbm = DatabaseManager(db_conf.DATABASES)
Model.set_connection_resolver(dbm)
