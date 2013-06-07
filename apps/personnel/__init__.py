# -*- coding: utf-8 -*-

menus = (
         ('att_monitor',u'数据监控', 'grup_disc'),
#         ('aboutEmp',u'人员相关', 'grup_info'),
#         ('baseinfo',u'基本资料', 'grup_alarm'),
#         ('reportEmp',u'人事报表', 'grup_disc'),
         )

####### 自定义视图 #########
import routes

from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./apps/personnel/templates/')