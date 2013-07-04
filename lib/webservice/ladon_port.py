# -*- coding: utf-8 -*-

def get_charset(env,default='UTF-8'):
    import re
    try:
        rx_ctype_charset = re.compile('charset\s*=\s*([-_.a-zA-Z0-9]+)',re.I)
        res = rx_ctype_charset.findall(env['CONTENT_TYPE'])
        if len(res):
            return res[0]
        return env['HTTP_ACCEPT_CHARSET'].split(';')[0].split(',')[0]
    except:
        return default
    
def parse_environ(environ):
    import re
    rx_detect_multipart = re.compile('multipart/([^; ]+)',re.I)
    rx_detect_boundary = re.compile('boundary=([^; ]+)',re.I)
    # Multipart detection
    multipart = boundary = None
    if 'CONTENT_TYPE' in environ:
        content_type = environ['CONTENT_TYPE']
        content_type = content_type.replace('\n','')
        multipart_match = rx_detect_multipart.findall(content_type)
        if len(multipart_match):
            multipart = multipart_match[0]
            boundary_match = rx_detect_boundary.findall(content_type)
            if len(boundary_match):
                boundary = boundary_match[0]
    return multipart,boundary

def generate_service(service):
    '''
    service实例结构
    '''
    from ladon.interfaces import _interfaces
    from ladon.compat import type_to_jsontype,PORTABLE_STRING_TYPES
    def get_ladontype(typ):
        if type(typ)==list:
            if typ[0] in service.typemanager.type_dict:
                return typ[0].__name__
            else:
                return False
        else:
            if typ in service.typemanager.type_dict:
                return typ.__name__
            else:
                return False
        
    def type_to_string(typ):
        paramtype = typ
        if type(paramtype)==list:
            paramtype = paramtype[0]
            if paramtype in service.typemanager.type_dict:
                paramtype_str = '[ %s ]' % paramtype.__name__
            else:
                paramtype_str = '[ %s ]' % type_to_jsontype[paramtype]
        else:
            if paramtype in service.typemanager.type_dict:
                paramtype_str = paramtype.__name__
            elif paramtype in type_to_jsontype:
                paramtype_str = type_to_jsontype[paramtype]
            else:
                paramtype_str = paramtype.__name__
        return paramtype_str
    
    service_info = {
        'servicename': service.servicename,
        'doc_lines': service.doc_lines,
        'interfaces': _interfaces.keys(),
        'methods': [],
        'types': [],
        'charset': 'utf-8',
    }
    '''获取所有可用接口方法的信息'''
    for method in service.method_list():
        method_info = {
            'methodname': method.name(),
            'params': [],
            'doc_lines': method._method_doc,
            'returns': {
                'type': type_to_string(method._rtype),
                'ladontype': get_ladontype(method._rtype),
                'doc_lines': method._rtype_doc } }
        for param in method.args():
            param_info = {
                'name': param['name'],
                'type': type_to_string(param['type']),
                'ladontype': get_ladontype(param['type']),
                'optional': param['optional'],
                'doc_lines': param['doc'] }
            if 'default' in param:
                default_type = param['default']
                if param['type'] in PORTABLE_STRING_TYPES:
                    param_info['default'] = '"%s"' % param['default']
                else:
                    param_info['default'] = str(param['default'])
            method_info['params'] += [ param_info ]
        service_info['methods'] += [method_info]
    ''''获取所有可用类型的信息￐ￍﾵￄ￐ￅￏﾢ '''
    types = service_info['types']
    type_order = service.typemanager.type_order
    for typ in type_order:
        if type(typ)==dict:
            desc_type = {}
            desc_type['name'] = typ['name']
            desc_type['attributes'] = {}
            for k,v,props in typ['attributes']:
                desc_type_val = type_to_string(v)
                desc_type['attributes'][k] = {
                    'type': desc_type_val,
                    'props': props,
                    'ladontype': get_ladontype(v) }
            types += [desc_type]
    return service_info