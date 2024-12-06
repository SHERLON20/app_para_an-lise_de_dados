from rest_framework import serializers
from .models import sale

class Saleserializer(serializers.ModelSerializer):
    class Meta:
        model = sale
        fields = '__all__'