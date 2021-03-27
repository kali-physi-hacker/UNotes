from django.urls import path 
from .views import notes_lyric


urlpatterns = [
    path("notes_lyrics/", notes_lyric, name="notes_lyric"),
]