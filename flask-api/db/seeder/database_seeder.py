import sys
import os
sys.path.append(os.getcwd())

from orator.seeds import Seeder
from db.seeder.user_table_seeder import UserTableSeeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(UserTableSeeder)
