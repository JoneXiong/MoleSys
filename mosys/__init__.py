# -*- coding: utf-8 -*-
'''
用于构建Mole系统页面基础架构
'''
import os

import mole.const
mole.const.ERROR_PAGE_TEMPLATE = """
%try:
    %from mole import DEBUG, HTTP_CODES, request
    %status_name = HTTP_CODES.get(e.status, 'Unknown').title()
             {"statusCode":"300", "message":'
            <title>ops! Error {{e.status}}: {{status_name}}</title>

            <h1>ops! Error {{e.status}}: {{status_name}}</h1>
            <p>Sorry, the requested URL <tt>{{request.url}}</tt> caused an error:</p>
            <pre>{{str(e.output)}}</pre>
            %if DEBUG and e.exception:
              <h2>Exception:</h2>
              <pre>{{repr(e.exception)}}</pre>
            %end
            %if DEBUG and e.traceback:
              <h2>Traceback:</h2>
              <pre>{{e.traceback}}</pre>
            %end
            '}
%except ImportError:
    <b>ImportError:</b> Could not generate the error page. Please add mole to sys.path
%end
"""

from mole.const import TEMPLATE_PATH
cur = os.path.split(os.path.realpath(__file__))[0]
templates_path = os.path.join(cur,'templates')
TEMPLATE_PATH.append(templates_path)


# 配置静态目录
from mole import route,static_file
static_path = os.path.join(cur,'static')
@route('/static_mosys/:filename#.*#',name='mosys.static')
def admin_static(filename):
    return static_file(filename, root=static_path)

@route('/tmpfile/:file#.*#')    #导出供下载的目录
def media(file):
    return static_file(file, root='./tmpfile')


####################### 全局初始化 #######################
#加载全局模型对象
from load import ModelScan
apps = None

def setup(tar):
    global apps
    apps = tar
    ModelScan()

#引入路由视图
import route_func