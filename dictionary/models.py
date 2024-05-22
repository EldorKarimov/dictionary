from django.db import models
import requests
import json
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

from shared.models import BaseModel

class Direction(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class EnglishWord(BaseModel):
    word = models.CharField(max_length=50, unique=True, verbose_name='Word(en)')
    definition = models.CharField(max_length=255, null=True, blank=True)
    audio = models.CharField(max_length=255, null=True, blank=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=True)
    


    def __str__(self):
        return self.word
    
    def save(self, *args, **kwargs):
        app_id = "447981f0"
        app_key = "6c19369a08246da2faa3f61869424793"
        language = "en-gb"
        word_id = self.word
        try:
            url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
            r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
            res = r.json()
            self.audio = res.get('results')[0].get('lexicalEntries')[0]['entries'][0]['pronunciations'][0]['audioFile']
            super(EnglishWord, self).save(*args, **kwargs)
        except:
            raise ValidationError("Word not found with audio")
        

class UzbekWord(BaseModel):
    uzWord = models.CharField(max_length=50, verbose_name='Word(uz)')
    enWord = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)

    def __str__(self):
        return self.uzWord
    
    @classmethod
    def get_uz_word_list(cls, en):
        uz = []
        uz_words = cls.objects.filter(enWord__word = en)
        for i in uz_words:
            uz.append(i.uzWord)
        return uz

class About(BaseModel):
    content = RichTextUploadingField()
    share = models.URLField(verbose_name="URL")

    def __str__(self):
        return str(self.created)