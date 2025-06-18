from django.db import models

from core.models.planet import Planet


class Film(models.Model):
    """
    Represents a Star Wars film.

    Attributes:
        title (CharField): The title of the film.
        episode_id (IntegerField): The episode number of the film.
        opening_crawl (TextField): The opening crawl text shown at the
        beginning of the film.
        director (CharField): The name of the film's director.
        producers (CharField): A comma-separated list of the film's producers.
        release_date (DateField): The release date of the film.
        planets (ManyToManyField): The planets featured in the film.
    Methods:
        __str__(): Returns a string representation of the film in the format
        "Episode {episode_id}: {title}".
    """

    title = models.CharField(max_length=150)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField()
    director = models.CharField(max_length=100)
    producers = models.CharField(max_length=250)
    release_date = models.DateField()

    planets = models.ManyToManyField(Planet, related_name="films")

    def __str__(self):
        return f"Episode {self.episode_id}: {self.title}"
