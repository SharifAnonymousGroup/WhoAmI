from django.db import models

# Create your models here.
from django.db.models.fields.related import ManyToManyField
import user_manager

GENDER_CHOISES = (('F', 'Female'), ('M', 'Male'), ('N', 'Not known'))

class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES)
    nick_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    credit = models.IntegerField()
    registration_time = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='Date/profile_pictures')

class game(models.Model):
    playing_date = models.DateTimeField(auto_now_add=True)
    winner = models.ForeignKey('user')
    players = ManyToManyField('user', related_name='games', through='Result')

class Result(models.Model):
    player = models.ForeignKey('user', related_name='rel')
    game = models.ForeignKey('game', related_name='ral')
    rate = models.IntegerField()
    added_credit = models.IntegerField()









