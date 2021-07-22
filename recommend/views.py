from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecommendSerializer
from .models import Recommend

# Create your views here.
@api_view(['GET'])
def recommend_list(request):
    print(request.data)
    recommendation = Recommend.objects.all()
    serializers = RecommendSerializer(recommendation, many=True)
    return Response(serializers.data)
