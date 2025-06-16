from django.db import models

from core.models.film import Film


class Character(models.Model):
    """Represents a character from the Star Wars universe.

    Attributes:
        name (CharField): The name of the character.
        birth_year (CharField): The birth year of the character (can be blank or null).
        gender (CharField): The gender of the character (can be blank or null).
        films (ManyToManyField): The films in which this character appears.

    Methods:
        __str__(): Returns the string representation of the character (the name).
    """
    name = models.CharField(max_length=100)
    birth_year = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    films = models.ManyToManyField(Film, related_name="characters")

    def __str__(self):
        return self.name
