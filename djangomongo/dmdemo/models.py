from django.db import models

from mongoengine import *
import datetime

connect(db="djangomongo", host="localhost")


class Form(Document):
    user_name = StringField(required=True)
    data = DictField()
