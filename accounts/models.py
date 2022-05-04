from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # add additional fields in here
    is_station = models.BooleanField(default=False)

class Officer(models.Model):
    RANK_TYPE = (
        ('Assistant Police Sub Inspector(A.S.I.)', 'Assistant Police Sub Inspector(A.S.I.)'),
        ('Police Sub Inspector (P.S.I.)', 'Police Sub Inspector (P.S.I.)'),
        ('Police Inspector (P.I.)', 'Police Inspector (P.I.)'),
        ('Police Chief Inspector (P.C.I.)', 'Police Chief Inspector (P.C.I.)'),
        ('Police Chief', 'Police Chief'),
    )
    phone = models.BigIntegerField(blank=True, null=True)
    rank = models.CharField(max_length=50, choices=RANK_TYPE, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class CaseType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name

class Station(models.Model):
    subadmin = models.ForeignKey(Officer, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=0)
    phone = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0, null=True, blank=True)