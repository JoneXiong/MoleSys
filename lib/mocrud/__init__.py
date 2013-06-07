# -*- coding: utf-8 -*-
'''
crud
'''

__version__ = "0.1"

from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./lib/mocrud/templates/')

import apps as conf

from mole import static_file
@conf.app.route('/static_crud/:filename#.*#',name='admin.static')
def admin_static(filename):
    return static_file(filename, root='./lib/mocrud/static')

#from db import Database
#from apps import crud_db_config
#db = Database(crud_db_config)