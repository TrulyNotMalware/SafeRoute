from .models import Subway
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subway
        fields = '__all__'