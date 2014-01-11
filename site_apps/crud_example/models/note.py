# -*- coding: utf-8 -*-

import datetime

from mocrud.auth import BaseUser
from mocrud.db import CrudModel
from mocrud.admin import ModelAdmin
from peewee import *


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