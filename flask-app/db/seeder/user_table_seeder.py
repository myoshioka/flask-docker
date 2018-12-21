from orator.seeds import Seeder


class UserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        try:
            self.db.table('user').insert([
                {
                    'name': 'admin',
                    'password': 'admin'
                }
            ])
        except Exception as e:
            print(e.args)
