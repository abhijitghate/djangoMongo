
from rest_framework_mongoengine import serializers as s
from dmdemo.models import Form


class FormSerializer(s.DocumentSerializer):
    class Meta:
        model = Form
        fields = '__all__'
