from django.urls import path
from .views import notes_lyric


urlpatterns = [path("notes/", notes_lyric, name="notes_lyric")]
