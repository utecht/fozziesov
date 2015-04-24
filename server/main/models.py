from django.db import models
from django.db.models import (Model, 
                              ForeignKey,
                              CharField, 
                              IntegerField, 
                              DateField,
                              DateTimeField)

from crest_app.models import EveUser

class Alliance(Model):
    alliance_id = IntegerField(unique=True)
    name = CharField(max_length=200)
    ticker = CharField(max_length=5)

    def __str__(self):
        return "[{}] {}".format(self.ticker, self.name)

class Corporation(Model):
    corporation_id = IntegerField(unique=True)
    name = CharField(max_length=200)
    ticker = CharField(max_length=5)
    alliance = ForeignKey(Alliance)

    def __str__(self):
        return "[{}] {}".format(self.ticker, self.name)

class Character(Model):
    character_id = IntegerField(unique=True)
    name = CharField(max_length=50)
    corporation = ForeignKey(Corporation)

    def __str__(self):
        return "{}".format(self.name)

class Constellation(Model):
    const_id = IntegerField(unique=True)
    region = CharField(max_length=50)
    name = CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.name, self.region)

class System(Model):
    system_id = IntegerField(unique=True)
    constellation = ForeignKey(Constellation)
    name = CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)

class Structure(Model):
    structure_id = IntegerField(unique=True)
    name = CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)

class Stratop(Model):
    constellation = ForeignKey(Constellation)
    good_guys = ForeignKey(Alliance)
    user = ForeignKey(EveUser)
    date = DateTimeField()

    def __str__(self):
        return "{} - {} - {}".format(self.constellation.name, self.user.username, self.date)

class Battle(Model):
    stratop = ForeignKey(Stratop)
    system = ForeignKey(System)
    structure = ForeignKey(Structure)

    def __str__(self):
        return "{} - {}".format(self.system.name, self.structure.name)

class ControlNode(Model):
    battle = ForeignKey(Battle)
    system = ForeignKey(System)
    control = ForeignKey(Alliance, blank=True, null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.battle, self.system, self.control)

class AllianceState(Model):
    stratop = ForeignKey(Stratop)
    alliance = ForeignKey(Alliance)
    number = IntegerField()

    def __str__(self):
        return "{} - {}".format(self.alliance, self.number)

class Event(Model):
    time = DateTimeField()
    stratop = ForeignKey(Stratop)
    text = CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.text)

class SystemAllianceState(Model):
    stratop = ForeignKey(Stratop)
    alliance = ForeignKey(Alliance)
    system = ForeignKey(System)
    number = IntegerField()

    def __str__(self):
        return "{} - {} - {}".format(self.system, self.alliance, self.number)

class SystemEvent(Model):
    stratop = ForeignKey(Stratop)
    system = ForeignKey(System)
    time = DateTimeField()
    text = CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.system, self.text)
