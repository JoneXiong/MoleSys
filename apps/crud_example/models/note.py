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
    
    base_templates = {
        'index': 'note_index.html',
        'add': 'note_add.html',
        'edit': 'note_edit.html',
        'delete': 'admin/models/delete.html',
        'export': 'admin/models/export.html',
    }
    
Note.Admin = NoteAdmin

class Attentions(CrudModel):
    autor = CharField(verbose_name=u'提交人')
    title = CharField(verbose_name=u'主题')
    content = TextField(verbose_name=u'内容')
    created_date = DateTimeField(default=datetime.datetime.now)
    
    
class AttentionsAdmin(ModelAdmin):
    columns = ('autor', 'title', 'content', 'created_date',)
    exclude = ('created_date',)
    
    base_templates = {
        'index': 'attentions_index.html',
        'add': 'attentions_add.html',
        'edit': 'attentions_edit.html',
        'delete': 'admin/models/delete.html',
        'export': 'admin/models/export.html',
    }
    
Attentions.Admin = AttentionsAdmin