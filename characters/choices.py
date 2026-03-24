from django.db.models import TextChoices


class CharacterStatusChoices(TextChoices):
    ALIVE = "Alive"
    DEAD = "Dead"
    UNKNOWN = "Unknown"


class CharacterGenderChoices(TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    GENDERLESS = "Genderless"
    UNKNOWN = "Unknown"
