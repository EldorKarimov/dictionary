from rest_framework import serializers
from dictionary.models import EnglishWord, UzbekWord, Direction

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'
    
class EnglishWordSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer()
    class Meta:
        model = EnglishWord
        fields = '__all__'

class UzbekWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UzbekWord
        fields = ['id', 'uzWord']