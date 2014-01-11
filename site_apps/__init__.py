# -*- coding: utf-8 -*-
from mole import route, static_file

#安装的子应用
apps_list = (
        ('crud_example',u'模型管理'),
        )

# 配置公共模板目录
from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./apps/templates/')

# 配置静态目录
@route('/media/:file#.*#')
def media(file):
    return static_file(file, root='./apps/media')

# 配置系统app
COOKIE_KEY = '457rxK8ytkKiqkfqwfoiQS@kaJSFOo8h'
from mole.mole import default_app
app = default_app()

# Crud ORM数据库配置
crud_db_config =  {
    'name': 'db/site.db',
    'engine': 'peewee.SqliteDatabase',
    'check_same_thread': False,
}

# 工作目录
workspace = '.'
