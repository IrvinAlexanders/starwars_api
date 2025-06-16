from django.db import models


class Planet(models.Model):
    """Represents a planet in the Star Wars universe.
    
    Attributes:
        name (CharField): The name of the planet.
        climate (CharField): The climate of the planet (can be blank).
        terrain (CharField): The terrain of the planet (can be blank).
        population (CharField): The population of the planet (can be blank).

    Methods:
        __str__(): Returns the string representation of the planet (the name).
    """

    name = models.CharField(max_length=100)
    climate = models.CharField(max_length=100, blank=True)
    terrain = models.CharField(max_length=100, blank=True)
    population = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name