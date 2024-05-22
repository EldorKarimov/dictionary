from django.urls import path
from . import views

urlpatterns = [
    path('en-uz/', views.EnglishWordListAPIView.as_view()),
    path('en-uz/update/<int:word_id>/', views.EnglishWordUpdateAPIVIew.as_view()),
    path('about/', views.AboutAPIView.as_view())
]