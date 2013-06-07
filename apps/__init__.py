# -*- coding: utf-8 -*-
from mole import route, static_file

#安装的子应用
apps_list = (
        ('personnel',u'人事管理'),
        ('att',u'考勤管理'),
        ('crud_example',u'模型管理')
        )

# 配置公共模板目录
from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./apps/templates/')

# 配置静态目录
@route('/static/:file#.*#')
def media(file):
    return static_file(file, root='./apps/media')

@route('/media/:file#.*#')
def media(file):
    return static_file(file, root='./apps/media')

# 配置系统app
COOKIE_KEY = '457rxK8ytkKiqkfqwfoiQS@kaJSFOo8h'
from mole.mole import default_app
app = default_app()

# 安装公共路由视图
import routes

#数据库接口配置
from DBUtils.PooledDB import PooledDB
############ Mysql ########
#import MySQLdb as pyDB
#dbpool = PooledDB(
#            creator=MySQLdb, 
#            maxusage=1000,
#            host='localhost',
#            user='root', 
#            passwd='root',
#            db='db_name')
############ Mssql #########
import pymssql as pyDB
conn_args = {
               'host':'127.0.0.1\SQLEXPRESS',
                'user':'sa', 
                'charset':'utf8',
                'password':'123123', 
                'database': 'ltcj_x'}

args = (0,0,0,100,0,0,None )
dbpool = PooledDB(pyDB, *args, **conn_args)


# Crud ORM数据库配置
crud_db_config =  {
    'name': 'db/example.db',
    'engine': 'peewee.SqliteDatabase',
    'check_same_thread': False,
}

# 工作目录
workspace = '.'
