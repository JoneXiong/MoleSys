# -*- coding: utf-8 -*-

menus = (
         ('att_report',u'报表数据', 'grup_info'),
         )

####### 自定义视图 #########
import routes

from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./apps/att/templates/')