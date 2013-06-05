# -*- coding: utf-8 -*-
##################### 系统环境设置 #######################
def set_lib_path():
    import sys
    import os
    sys.path.append('./lib')
set_lib_path()

#安装的mosys、apps系统模块
import apps
import mosys

#加入SessionMiddleware 中间件
COOKIE_KEY = '457rxK8ytkKiqkfqwfoiQS@kaJSFOo8h'
from mole.mole import default_app
from mole.sessions import SessionMiddleware
app = default_app()
app = SessionMiddleware(app=app, cookie_key=COOKIE_KEY,no_datastore=True)

#运行服务器
from mole import run
if __name__  == "__main__":
    run(app=app,host='0.0.0.0', port=8081)