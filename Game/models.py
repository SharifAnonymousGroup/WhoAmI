from django.db import models

# Create your models here.


class Player(models.Model):
    member = models.ForeignKey('UserManagement.models.Member', related_name='player')