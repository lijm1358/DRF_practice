from rest_framework import serializers
from .models import Recommend

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = ['User_ID', 'lat', 'long', 'epsilon', 'keywords']
