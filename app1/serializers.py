from rest_framework.serializers import ModelSerializer

from .models import *

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"