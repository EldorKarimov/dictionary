from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from dictionary.models import UzbekWord, EnglishWord, Direction
from .serializers import DirectionSerializer, EnglishWordSerializer, UzbekWordSerializer
from pprint import pprint as print



class EnglishWordListAPIView(APIView):
    def get(self, request):
        enWords = EnglishWord.objects.all()
        en_uz = []
        for i in enWords:
            x = EnglishWordSerializer(i).data
            uzbek = UzbekWord.get_uz_word_list(i.word)
            x.update({"uzWords": uzbek})
            en_uz.append(x)
        data = {
            'status':status.HTTP_200_OK,
            'data': en_uz
        }
        return Response(data)