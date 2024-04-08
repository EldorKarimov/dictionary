from rest_framework.response import Response
from rest_framework import status
from uz_en.models import EnglishWord, UzbekWord
from rest_framework.views import APIView
from .serializers import UzbekEnglishSerializer
from django.http import HttpResponse

class UzbekEnglishWordsAPIView(APIView):
    def get(self, request):
        uz_words = UzbekWord.objects.all()
        uz_en_list = []
        for i in uz_words:
            serializer = UzbekEnglishSerializer(i).data
            
            serializer.update({"enWords": EnglishWord.get_english_word_lsit(i.word)})
            uz_en_list.append(serializer)
        print(uz_en_list)
        data = {
            'status': status.HTTP_200_OK,
            'data': uz_en_list
        }
        return Response(data)