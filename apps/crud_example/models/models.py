# -*- coding: utf-8 -*-
import datetime

from mocrud.auth import BaseUser
from mocrud.db import CrudModel
from peewee import *

class User(CrudModel, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    def __unicode__(self):
        return self.username

    def following(self):
        return User.select().join(
            Relationship, on=Relationship.to_user
        ).where(Relationship.from_user==self).order_by(User.username)

    def followers(self):
        return User.select().join(
            Relationship, on=Relationship.from_user
        ).where(Relationship.to_user==self).order_by(User.username)

    def is_following(self, user):
        return Relationship.select().where(
            Relationship.from_user==self,
            Relationship.to_user==user
        ).exists()

    def gravatar_url(self, size=80):
        return 'http://static.oschina.net/uploads/user/52/105889_100.jpg'

class Relationship(CrudModel):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')

    def __unicode__(self):
        return 'Relationship from %s to %s' % (self.from_user, self.to_user)
