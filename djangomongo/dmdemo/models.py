from django.db import models

from mongoengine import *

connect(db="djangomongo", host="localhost")


class Form(Document):
    user_name = StringField(required=True)
    date = DateTimeField()
    data = DictField()
