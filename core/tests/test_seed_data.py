import pytest
from django.core.management import call_command
from core.models import Character, Film, Planet


@pytest.mark.django_db
def test_seed_data_command_creates_expected_objects(capfd):
    # Run the custom management command
    call_command("seed_data")

    # Check Planets
    planets = Planet.objects.all()
    assert planets.count() == 2
    names = set(planets.values_list("name", flat=True))
    assert "Tatooine" in names
    assert "Alderaan" in names

    # Check Characters
    characters = Character.objects.all()
    assert characters.count() == 2
    char_names = set(characters.values_list("name", flat=True))
    assert "Luke Skywalker" in char_names
    assert "Leia Organa" in char_names

    # Check Films
    films = Film.objects.all()
    assert films.count() == 1
    film = films.first()
    assert film.title == "A New Hope"
    assert film.episode_id == 4
    assert film.director == "George Lucas"
    assert film.producers == "Gary Kurtz, Rick McCallum"
    assert film.release_date.strftime("%Y-%m-%d") == "1977-05-25"

    # Check relations
    assert set(film.characters.values_list("name", flat=True)) == {"Luke Skywalker", "Leia Organa"}
    assert set(film.planets.values_list("name", flat=True)) == {"Tatooine", "Alderaan"}

    # Check output
    out, _ = capfd.readouterr()
    assert "Seeding database..." in out
    assert "Database seeded successfully" in out


@pytest.mark.django_db
def test_seed_data_command_deletes_existing_data():
    # Create dummy data
    Planet.objects.create(name="Dummy", climate="none", population=0)
    Character.objects.create(name="Dummy", birth_year="0BBY", gender="none")
    Film.objects.create(title="Dummy", episode_id=0, opening_crawl="", director="", producers="", release_date="2000-01-01")

    # Run the command
    call_command("seed_data")

    # Only the seeded data should exist
    assert Planet.objects.filter(name="Dummy").count() == 0
    assert Character.objects.filter(name="Dummy").count() == 0
    assert Film.objects.filter(title="Dummy").count() == 0