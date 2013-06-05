# -*- coding: utf-8 -*-

menus = (
         ('pos_simulate',u'模拟操作', 'grup_calculator'),
         ('pos_simulate',u'菜单组', 'grup_configure'),
         )

####### 自定义视图 #########


import routes

from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./apps/pos/templates/')