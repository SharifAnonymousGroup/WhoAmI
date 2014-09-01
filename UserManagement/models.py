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
        member = self.model(
            age=age, gender=gender, credit=0, username=username,
            last_name=last_name, first_name=first_name, email=email
        )
        member.set_password(password)
        member.save()

    def create_superuser(self, username, email, password, **extra_fields):
        member = self.model(age=extra_fields['age'],
                            gender=extra_fields['gender'],
                            credit=0,
                            username=username,
                            last_name=extra_fields['last_name'],
                            first_name=extra_fields['first_name'],
                            email=email)
        member.is_superuser = True
        member.is_admin = True
        member.set_password(password)
        member.save()


class Member(AbstractUser):
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOISES)
    credit = models.IntegerField()
    picture = models.ImageField(upload_to='Data/profile_pictures', null=True, blank=True)
    objects = MemberManager()

    def __unicode__(self):
        return self.get_full_name() + self.gender + self.password

    class Meta:
        unique_together = ('email',)


class GameHistory(Logged):
    winner = models.ForeignKey('Member')
    players = ManyToManyField('Member', related_name='games', through='Result')


class Result(models.Model):
    player = models.ForeignKey('Member', related_name='p')
    game = models.ForeignKey('GameHistory', related_name='g')
    rate = models.IntegerField()
    added_credit = models.IntegerField()







