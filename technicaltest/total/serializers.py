from rest_framework import serializers
from .models import Total
from rest_framework.serializers import ModelSerializer


class TotalSerializer(serializers.ModelSerializer):


    class Meta:
        model = Total
        fields = ('total',)