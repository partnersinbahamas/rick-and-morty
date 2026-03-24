from django.db import models
from .choices import CharacterStatusChoices, CharacterGenderChoices


class Character(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=CharacterStatusChoices.choices,
        default=CharacterStatusChoices.UNKNOWN,
    )
    image = models.URLField(max_length=255, unique=True)
    species = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=50,
        choices=CharacterGenderChoices.choices,
        default=CharacterGenderChoices.UNKNOWN,
    )

    def __str__(self):
        return self.name
