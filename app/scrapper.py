import requests

from django.conf import settings
from characters.models import Character


def scrap_characters() -> list[Character]:
    next_url = settings.RICK_MORTY_CHARACTERS_API

    characters = []

    while next_url is not None:
        response = requests.get(next_url)

        if response.status_code != 200:
            next_url = None
            break

        characters_response = response.json()

        for character in characters_response["results"]:
            api_id = character["id"]
            name = character["name"]
            status = character["status"]
            species = character["species"]
            gender = character["gender"]
            image = character["image"]

            character = Character(
                api_id=api_id,
                name=name,
                status=status,
                species=species,
                gender=gender,
                image=image,
            )

            characters.append(character)

            next_url = characters_response["info"]["next"]

    return characters


def sync_characters() -> None:
    api_characters = scrap_characters()
    Character.objects.bulk_create(api_characters)
