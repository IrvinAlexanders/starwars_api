from django.contrib import admin

from .character import * # NoQA: F401, F403
from .film import * # NoQA: F401, F403
from .planet import * # NoQA: F401, F403


admin.site.register(Character)
admin.site.register(Film)
admin.site.register(Planet)