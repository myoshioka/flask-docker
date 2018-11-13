from orator.seeds import Seeder


class UserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('user').insert([
            {
                'name': 'admin',
                'password': 'admin'
            }
        ])
