from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from dictionary.models import UzbekWord, EnglishWord, Direction
from .serializers import EnglishWordSerializer, EnglishWordUpdateSerializer
from pprint import pprint as print



class EnglishWordListAPIView(APIView):
    def get(self, request):
        enWords = EnglishWord.objects.filter(is_new = True)
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

class EnglishWordUpdateAPIVIew(APIView):
    def get(self, request, word_id):
        word = EnglishWord.objects.get(id = word_id)
        serializer = EnglishWordSerializer(word)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
    
    def patch(self, request, word_id):
        word = get_object_or_404(EnglishWord, id = word_id)
        serializer = EnglishWordUpdateSerializer(data=request.data, instance = word,  partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)