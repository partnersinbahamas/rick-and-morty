from django.urls import path
from .views import get_random_character_view, CharacterList

app_name = "characters"

urlpatterns = [
    path("characters/", CharacterList.as_view(), name="characters"),
    path("characters/random/", get_random_character_view, name="characters-random"),
]
