from rest_framework import serializers
from dictionary.models import EnglishWord, UzbekWord, Direction, About

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ('id', 'name', 'slug')
    
class EnglishWordSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer()
    class Meta:
        model = EnglishWord
        fields = ('id', 'word', 'definition', 'audio', 'direction', 'is_new')

class EnglishWordUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWord
        fields = ('id', 'is_new')
        extra_kwargs = {
            'id':{'read_only': True}
        }

class UzbekWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UzbekWord
        fields = ['id', 'uzWord']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'content')