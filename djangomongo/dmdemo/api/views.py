from rest_framework_mongoengine.viewsets import ModelViewSet
from .serializers import FormSerializer
from dmdemo.models import Form


class FormViewSet(ModelViewSet):
    serializer_class = FormSerializer

    def get_queryset(self):
        return Form.objects.all()
