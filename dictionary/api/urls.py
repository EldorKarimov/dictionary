from django.urls import path
from . import views

urlpatterns = [
    path('en/', views.EnglishWordListAPIView.as_view()),
    path('uz/', views.UzbekWordListAPIView.as_view()),
    path('directions/', views.DirectionListApiView.as_view()),
    path('en/word/<slug:d_slug>/', views.EnglishWordByDirection.as_view())
]