# -*- coding: utf-8 -*-
##################### 系统环境设置 #######################
def set_lib_path():
    import sys
    import os
    sys.path.append('./lib')
set_lib_path()

#安装的apps、mosys系统模块(有先后顺序)
import site_apps
import mocrud
import mosys
mosys.setup(site_apps)


#加入SessionMiddleware 中间件
from mole.sessions import SessionMiddleware
app = SessionMiddleware(app=site_apps.app, cookie_key=site_apps.COOKIE_KEY,no_datastore=True)

#运行服务器
from mole import run
if __name__  == "__main__":
    run(app=app,host='0.0.0.0', port=8081)