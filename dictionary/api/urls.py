from django.urls import path
from . import views

urlpatterns = [
    path('en-uz/', views.EnglishWordListAPIView.as_view()),
    
]