from rest_framework_mongoengine.viewsets import ModelViewSet
from .serializers import FormSerializer, CustomFieldSerializer
from dmdemo.models import Form, CustomField


class FormViewSet(ModelViewSet):
    serializer_class = FormSerializer

    def get_queryset(self):
        return Form.objects.all()


class CustomFieldViewSet(ModelViewSet):
    serializer_class = CustomFieldSerializer

    def get_queryset(self):
        return CustomField.objects.all()
