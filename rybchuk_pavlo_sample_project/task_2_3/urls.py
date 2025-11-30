from django.urls import path
from . import views

urlpatterns = [
    path('', views.anagram_check, name='anagram_check'),
    path('results/<str:are_anagrams>/', views.anagram_result, name='anagram_result'),
    path('feedback/', views.send_feedback, name='send_feedback'),
    path('rating/', views.get_feedbacks, name='get_feedbacks'),
]