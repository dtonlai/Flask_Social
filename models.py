import datetime

from peewee import *
from flask.ext.login import UserMixin


DATABASE = SqliteDatabase("social.db")


class User(UserMixin, Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField(max_length = 100)
	joinDate = DateTImeField(default=datetime.datetime.now)
	isAdmin = BooleanField(default=False)

	class Meta:
		database = DATABASE

if __name__ = "__main__":
	DATABASE.connect()
	DATABASE.create_tables([User], safe=True)
	order_by("--joinDate",)
