from __future__ import unicode_literals
from django.db import models

#different tables of the database are declared here

#this table stores the users who are registered to vote
class User(models.Model):
    email = models.CharField(max_length=50)
    userid = models.CharField(max_length=15)
    def __unicode__(self):
        return self.userid

#this table stores the details of the candidates and the party they belong to
class Candidate(models.Model):
    party_name = models.CharField(max_length=100, null=False, blank=False)
    candidate1 = models.CharField(max_length=50, null=False, blank=False)
    candidate2 = models.CharField(max_length=50, null=True, blank=True)
    candidate3 = models.CharField(max_length=50, null=True, blank=True)
    candidate4 = models.CharField(max_length=50, null=True, blank=True)
    candidate5 = models.CharField(max_length=50, null=True, blank=True)
    candidate6 = models.CharField(max_length=50, null=True, blank=True)
    candidate7 = models.CharField(max_length=50, null=True, blank=True)
    candidate8 = models.CharField(max_length=50, null=True, blank=True)
    candidate9 = models.CharField(max_length=50, null=True, blank=True)
    candidate10 = models.CharField(max_length=50, null=True, blank=True)
    candidate11 = models.CharField(max_length=50, null=True, blank=True)
    candidate12 = models.CharField(max_length=50, null=True, blank=True)
    candidate13 = models.CharField(max_length=50, null=True, blank=True)
    candidate14 = models.CharField(max_length=50, null=True, blank=True)
    candidate15 = models.CharField(max_length=50, null=True, blank=True)
    def __unicode__(self):
        return self.party_name

#this table stores the details of how many votes the respective numbered candidate in a list has got
class Vote(models.Model):
    partyname = models.CharField(max_length=100, null=False, blank=False)
    totalvotes = models.IntegerField(default=0)
    vote1 = models.IntegerField(default=0)
    vote2 = models.IntegerField(default=-1)
    vote3 = models.IntegerField(default=-1)
    vote4 = models.IntegerField(default=-1)
    vote5 = models.IntegerField(default=-1)
    vote6 = models.IntegerField(default=-1)
    vote7 = models.IntegerField(default=-1)
    vote8 = models.IntegerField(default=-1)
    vote9 = models.IntegerField(default=-1)
    vote10 = models.IntegerField(default=-1)
    vote11 = models.IntegerField(default=-1)
    vote12 = models.IntegerField(default=-1)
    vote13 = models.IntegerField(default=-1)
    vote14 = models.IntegerField(default=-1)
    vote15 = models.IntegerField(default=-1)
    def __unicode__(self):
        return self.partyname
