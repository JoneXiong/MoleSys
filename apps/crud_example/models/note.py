# -*- coding: utf-8 -*-

import datetime

from mocrud.auth import BaseUser
from mocrud.db import CrudModel
from mocrud.admin import ModelAdmin
from peewee import *

from models import User

class Note(CrudModel):
    user = ForeignKeyField(User)
    message = TextField()
    status = IntegerField(choices=((1, 'live'), (2, 'deleted')), null=True)
    created_date = DateTimeField(default=datetime.datetime.now)
    
class NoteAdmin(ModelAdmin):
    columns = ('user', 'message', 'created_date',)
    exclude = ('created_date',)
    
Note.Admin = NoteAdmin