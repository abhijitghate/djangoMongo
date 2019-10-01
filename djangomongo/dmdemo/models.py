from django.db import models

from mongoengine import *
import datetime

connect(db="djangomongo", host="localhost")

DATA_TYPES = ('int', 'str')


class CustomField(EmbeddedDocument):
    name = StringField(required=True)
    field_type = StringField(required=True, choices=DATA_TYPES)
    field_value = DynamicField()

    def clean(self):
        if ((type(self.field_value) != int and self.field_type != 'int') or
                (type(self.field_value) != str and self.field_type != 'str')):
            raise ValidationError("Field types and their values don't match")


class Form(Document):
    user_name = StringField(required=True)
    location = StringField(required=True)
    data = DictField()
    custom_field = ListField(EmbeddedDocumentField(CustomField))
