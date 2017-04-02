import datetime

from peewee import *
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash


DATABASE = SqliteDatabase("social.db")


class User(UserMixin, Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField(max_length =100)
	joinDate = DateTimeField(default=datetime.datetime.now)
	isAdmin = BooleanField(default=False)

	class Meta:
		database = DATABASE

	@classmethod
	def createUser(cls, username, email, password, admin=False):
		try:
			cls.create(
				username = username,
				email = email,
				passsword = generate_password_hash(password),
				isAdmin = admin,
				)
		except IntegrityError:
			raise ValueError("User already exists!")

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User], safe=True)
	DATABASE.close()

if __name__ == "__main__":
	DATABASE.connect()
	DATABASE.create_tables([User], safe=True)
	order_by("--joinDate",)
