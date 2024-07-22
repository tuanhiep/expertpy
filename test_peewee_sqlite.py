import unittest
from peewee import *

DATABASE = SqliteDatabase(':memory:')


class User(Model):
    username = CharField(unique=True)
    email = CharField(unique=True)

    class Meta:
        database = DATABASE


class DatabaseTests(unittest.TestCase):

    def setUp(self):
        DATABASE.connect()
        DATABASE.create_tables([User], safe=True)

    def tearDown(self):
        try:
            DATABASE.drop_tables([User])
        except:
            pass
        DATABASE.close()

    def test_check_user_table(self):
        assert User.table_exists()

    def test_drop_table(self):
        DATABASE.drop_tables([User])
        assert User.table_exists() == False


class UserTableTests(unittest.TestCase):

    def setUp(self):
        DATABASE.connect()
        try:
            DATABASE.create_tables([User])
        except:
            pass
        User.create(
            username='testUsername',
            email='testEmail@testEmail.com')

    def tearDown(self):
        User.delete().where(User.username == 'testUsername').execute()
        DATABASE.close()


    def test_create_username(self):
        user = User.get(username='testUsername')
        self.assertEqual(user.username, 'testUsername')




