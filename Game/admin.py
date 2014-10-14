from django.contrib import admin

# Register your models here.
from Game.models import *


admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Message)
admin.site.register(Round)