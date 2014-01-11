# -*- coding: utf-8 -*-

#from ooredis import *

from mosys.custom_model import AppPage

class RedisRedirect(AppPage):
    verbose_name=u'设备报告'
    menu_grup = 'att_monitor'
    icon_class = "menu_pathing"
    template = 'redis_redirect.html'
    pass
    
    def context(self):
        ret = [['4567897', '127.0.0.1','1'],['45613744', '127.0.0.1','1'],['7984513246', '127.0.0.1','1'],['123457899', '127.0.0.1','1']]
        return {'table_data':ret,'web_port':8080}