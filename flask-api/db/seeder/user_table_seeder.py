from orator.seeds import Seeder


class UserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('user').insert([
            {
                'name': 'john',
                'address': 'tokyo',
                'email': 'john@sample.com'
            },
            {
                'name': 'chris',
                'address': 'osaka',
                'email': 'chris@sample.com'
            }
        ])
