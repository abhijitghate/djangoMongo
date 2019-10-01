
from rest_framework_mongoengine import serializers as s
from dmdemo.models import Form, CustomField


class FormSerializer(s.DocumentSerializer):
    class Meta:
        model = Form
        fields = '__all__'


class CustomFieldSerializer(s.DocumentSerializer):
    class Meta:
        model = CustomField
        fields = '__all__'
