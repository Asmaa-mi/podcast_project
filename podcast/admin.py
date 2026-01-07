from django.contrib import admin
from .models import Podcast, Episode
from .models import Favorite

admin.site.register(Podcast)
admin.site.register(Episode)
admin.site.register(Favorite)
