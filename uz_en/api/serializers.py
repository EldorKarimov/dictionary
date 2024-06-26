from rest_framework import serializers
from uz_en.models import UzbekWord, EnglishWord
from dictionary.api.serializers import DirectionSerializer

class UzbekEnglishSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer(read_only = True)
    class Meta:
        model = UzbekWord
        fields = ('id', 'word', 'direction', 'is_new')
        extra_kwargs = {
            'id':{'read_only':True}
        }