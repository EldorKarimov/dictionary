from django.db import models
from shared.models import BaseModel
from dictionary.models import Direction

class UzbekWord(BaseModel):
    word = models.CharField(max_length=50, unique=True, verbose_name="Uzbek word")
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Uzbek word'
        verbose_name_plural = 'Uzbek words'

class EnglishWord(BaseModel):
    word = models.CharField(max_length=50, verbose_name="english word")
    uzWord = models.ForeignKey(UzbekWord, on_delete=models.CASCADE)

    def __str__(self):
        return self.word
    
    @classmethod
    def get_english_word_lsit(cls, word):
        en = []
        for i in cls.objects.filter(uzWord__word = word):
            en.append(i.word)
        return en
    
    class Meta:
        verbose_name = 'English word'
        verbose_name_plural = "English words"