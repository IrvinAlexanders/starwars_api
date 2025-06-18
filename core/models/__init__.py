from django.contrib import admin

from .character import Character
from .film import Film
from .planet import Planet


admin.site.register(Character)
admin.site.register(Film)
admin.site.register(Planet)
