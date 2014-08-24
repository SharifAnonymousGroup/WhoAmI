from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.fields.related import *


GENDER_CHOISES = (('F', 'Female'), ('M', 'Male'), ('N', 'Not known'))


class Logged(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        abstract = True


class Member(AbstractUser):
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES, null=True)
    credit = models.IntegerField(null=True)
    picture = models.ImageField(upload_to='Data/profile_pictures', null=True)
    def __unicode__(self):
        return self.get_full_name()

class GameHistory(Logged):
    winner = models.ForeignKey('Member')
    players = ManyToManyField('Member', related_name='games', through='Result')


class Result(models.Model):
    player = models.ForeignKey('Member', related_name='p')
    game = models.ForeignKey('GameHistory', related_name='g')
    rate = models.IntegerField()
    added_credit = models.IntegerField()







