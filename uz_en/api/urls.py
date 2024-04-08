from django.urls import path
from . import views

urlpatterns = [
    path('', views.UzbekEnglishWordsAPIView.as_view())
]