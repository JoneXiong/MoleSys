# -*- coding: utf-8 -*-

menus = (
         ('aboutEmp',u'菜单组一', 'grup_chat'),
         ('baseinfo',u'菜单组二', 'grup_chart'),
         ('reportEmp',u'菜单组二', 'grup_disc')
         )

####### 自定义视图 #########
import routes

from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./apps/crud_example/templates/')