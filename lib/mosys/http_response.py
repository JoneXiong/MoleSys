#coding=utf-8
'''
定义 ajax 的 200 300 301 状态的返回
'''

def ajax_success(msg,navTabId=None):
    json_str = ''' 
        { 
         "statusCode":"200",  
         "message":"%s",  
         "navTabId":"%s",  
         "rel":"",  
         "callbackType":"closeCurrent", 
         "forwardUrl":"" 
        }
    '''%(msg,navTabId or '')
    return json_str

def ajax_fail(msg):
    json_str = '''  {"statusCode":"300", "message":"%s"} '''%msg
    return json_str

def ajax_timeout(msg):
    '''
    会话超时 
    '''
    json_str = '''  {"statusCode":"301", "message":"%s"} '''%msg
    return json_str

def ajax_timeout_or_nopermission():
    '''
    会话超时 
    '''
    return ajax_timeout("会话已经过期或者权限不够,请重新登入!")

def ajax_fail_nomodel():
    return ajax_fail('内部错误,模型不存在')

def ajax_fail_nopermission():
    return ajax_fail('没有权限')
