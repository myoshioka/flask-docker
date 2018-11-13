from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('user') as table:
            table.increments('id')
            table.string('name', 60)
            table.string('password', 200)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('batch_history')
