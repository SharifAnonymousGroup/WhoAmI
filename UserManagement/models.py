from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
from django.db.models.fields.related import *


GENDER_CHOISES = (('F', 'Female'), ('M', 'Male'), ('N', 'Not known'))


class Logged(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    class Meta:
        abstract = True


class MemberManager(UserManager):
    def create_member(self, age, gender, username, last_name, first_name, password, email):
        if not username:
            raise ValueError("You must have username")
        member = self.model(
            age=age, gender=gender, credit=0, username=username,
            last_name=last_name, first_name=first_name, email=email
        )
        member.set_password(password)
        member.save()


class Member(AbstractUser):
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES, null=True)
    credit = models.IntegerField(null=True)
    picture = models.ImageField(upload_to='Data/profile_pictures', null=True, blank=True)
    objects = MemberManager()

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







