from django.db import models
from django.db.models import (Model, 
                              ForeignKey,
                              CharField, 
                              IntegerField, 
                              DateField,
                              DateTimeField)

from crest_app.models import EveUser

class Alliance(Model):
    alliance_id = IntegerField()
    name = CharField(max_length=200)
    ticker = CharField(max_length=5)

class Corporation(Model):
    corporation_id = IntegerField()
    name = CharField(max_length=200)
    ticker = CharField(max_length=5)
    alliance = ForeignKey(Alliance)

class Character(Model):
    character_id = IntegerField()
    name = CharField(max_length=50)
    corporation = ForeignKey(Corporation)

class Constellation(Model):
    const_id = IntegerField()
    region = CharField(max_length=50)
    name = CharField(max_length=50)

class System(Model):
    system_id = IntegerField()
    constellation = ForeignKey(Constellation)
    name = CharField(max_length=50)

class Structure(Model):
    structure_id = IntegerField()
    name = CharField(max_length=50)

class Stratop(Model):
    constellation = ForeignKey(Constellation)
    good_guys = ForeignKey(Alliance)
    user = ForeignKey(EveUser)
    date = DateTimeField()

class Battle(Model):
    stratop = ForeignKey(Stratop)
    system = ForeignKey(System)
    structure = ForeignKey(Structure)

class ControlNode(Model):
    battle = ForeignKey(Battle)
    system = ForeignKey(System)
    control = ForeignKey(Alliance, null=True)

class AllianceState(Model):
    stratop = ForeignKey(Stratop)
    alliance = ForeignKey(Alliance)
    number = IntegerField()

class Event(Model):
    time = DateField()
    stratop = ForeignKey(Stratop)
    text = CharField(max_length=50)

class SystemAllianceState(Model):
    stratop = ForeignKey(Stratop)
    alliance = ForeignKey(Alliance)
    system = ForeignKey(System)
    number = IntegerField()

class SystemEvent(Model):
    stratop = ForeignKey(Stratop)
    system = ForeignKey(System)
    time = DateField()
    text = CharField(max_length=50)
