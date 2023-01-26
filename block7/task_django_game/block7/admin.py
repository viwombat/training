from django.contrib import admin
from .models import Game, Genre, User, Publisher
# Register your models here.

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(User)
admin.site.register(Publisher)
