# -*- coding: utf-8 -*-
'''
用于构建Mole系统web服务扩展
'''

__version__ = "0.1"

from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./lib/webservice/templates/')

import route_func