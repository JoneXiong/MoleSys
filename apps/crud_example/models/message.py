# -*- coding: utf-8 -*-

import datetime

from mocrud.auth import BaseUser
from mocrud.db import CrudModel
from mocrud.admin import ModelAdmin
from peewee import *

from models import User

class Message(CrudModel):
    user = ForeignKeyField(User,verbose_name = u'用户')
    content = TextField(verbose_name=u'内容')
    pub_date = DateTimeField(default=datetime.datetime.now,verbose_name=u'提交时间')

    def __unicode__(self):
        return '%s: %s' % (self.user, self.content)
    
class MessageAdmin(ModelAdmin):
    columns = ('user', 'content', 'pub_date',)
    foreign_key_lookups = {'user': 'username'}
    filter_fields = ('user', 'content', 'pub_date', 'user__username')
    
#    def get_admin_name(self):
#        '''菜单名字'''
#        return u'人员消息'
#    
    def get_display_name(self):
        '''模型名字'''
        return u'消息'
    
Message.Admin = MessageAdmin