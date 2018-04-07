# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Branch(models.Model):

    name = models.TextField()
    address = models.TextField()
    postal_code = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    smsq = models.TextField()
    operating_hours = models.TextField()
    week_day_start_time = models.TextField()
    week_day_end_time = models.TextField()
    week_end_start_time = models.TextField()
    week_end_end_time = models.TextField()

    def __str__(self):
        return "Name: " + self.name + ", Address: " + self.address + ", Postal_Code: " + self.postal_code


class RelationshipManager(models.Model):

    user = models.ForeignKey(User)
    branch = models.ForeignKey(Branch)


class Appointment(models.Model):

    user = models.ForeignKey(User)
    title = models.TextField()
    description = models.TextField()
    branch = models.ForeignKey(Branch)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    rm = models.ForeignKey(RelationshipManager)
    status = models.TextField()

