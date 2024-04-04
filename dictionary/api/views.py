from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404

from dictionary.models import UzbekWord, EnglishWord, Direction
from .serializers import DirectionSerializer, EnglishWordSerializer, UzbekWordSerializer

class DirectionListApiView(APIView):
    def get(self, request):
        directions = Direction.objects.all()
        serializer = DirectionSerializer(directions, many = True)
        data = {
            'status': status.HTTP_200_OK,
            'data': serializer.data
        }
        return Response(data=data)

class EnglishWordListAPIView(APIView):
    def get(self, request):
        enWords = EnglishWord.objects.all()
        serializer = EnglishWordSerializer(enWords, many=True)
        data = {
            'status':status.HTTP_200_OK,
            'data':serializer.data
        }
        return Response(data)
    
class EnglishWordByDirection(APIView):
    def get(self, request, d_slug):
        enWords = EnglishWord.objects.filter(direction__slug = d_slug)
        serializer = EnglishWordSerializer(enWords, many = True)
        data = {
            'status': status.HTTP_200_OK,
            'data': serializer.data
        }
        return Response(data)

    
class UzbekWordListAPIView(APIView):
    def get(self, request):
        uzWords = UzbekWord.objects.all()
        serializer = UzbekWordSerializer(uzWords, many=True)
        data = {
            'status':status.HTTP_200_OK,
            'data':serializer.data
        }
        return Response(data)