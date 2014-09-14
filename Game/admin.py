from django.contrib import admin

# Register your models here.
from Game.models import *


admin.site.register(Player)
admin.site.register(Game)