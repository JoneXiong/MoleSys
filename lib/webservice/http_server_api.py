# -*- coding: utf-8 -*-

from mole import request
from mole import response
from mole.mole import HTTPError

from mole.template import template, Jinja2Template
def render_to_response(*args, **kwargs):
    kwargs['template_adapter'] = Jinja2Template
    return template(*args, **kwargs)

from mole.sessions import valid_user

def add_route(func, path=None, method='GET', no_hooks=False, decorate=None,
              template=None, template_opts={}, callback=None, name=None,
              static=False):
    '''
    添加路由
    '''
    from mole.mole import app, makelist,yieldroutes
    m_app = app()
    # @route can be used without any parameters
    if callable(path): path, callback = None, path
    # Build up the list of decorators
    decorators = makelist(decorate)
    if template:     decorators.insert(0, view(template, **template_opts))
    if not no_hooks: decorators.append(m_app._add_hook_wrapper)
    #decorators.append(partial(self.apply_plugins, skiplist))

    for rule in makelist(path) or yieldroutes(func):
        for verb in makelist(method):
            if static:
                rule = rule.replace(':','\\:')
                utils.depr("Use backslash to escape ':' in routes.")
            #TODO: Prepare this for plugins
            m_app.router.add(rule, verb, len(m_app.routes), name=name)
            m_app.routes.append((func, decorators))

def getJSResponse(msg):
    return msg

def RequestContext(request,info):
    return info

def HttpResponse(content,content_type=None):
    if content_type:
        response.headers['Content-Type'] = content_type
    return content