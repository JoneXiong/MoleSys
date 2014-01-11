# coding=utf-8
from mole_api import JTemplate, HTTPError

   
def GridModelView(request, app_label, model_name):
    from load import APP_PAGES
    from custom_model import GridModel
    request.user = None
    key = '%s.%s'%(app_label, model_name)
    m_post = request.params
    for e in APP_PAGES:
        if e[0]==key:
            if issubclass(e[1], GridModel):
                try:
                    offset = int(m_post.get('page', 1))
                except:
                    offset=1
                try:
                    psize = int(m_post.get('rp', 15))
                except:
                    psize=15
                arg = {'offset':offset,'psize':psize}
                sortname = m_post.get('sortname', 'undefined')
                sortorder = m_post.get('sortorder', 'undefined')
                if sortname!='undefined':
                    arg['sortname'] = sortname
                    arg['sortorder'] = (sortorder=='undefined') and 'asc' or sortorder
                query = m_post.get('query', '')
                qtype = m_post.get('qtype', '')
                if query!='':
                    arg['query'] = query
                    arg['qtype'] = qtype
                grid_model = e[1](request)
    #            grid_model.grid.ParseArg(**arg)
                if "export" in m_post:
                    return GridExport(request,grid_model,**arg)
                else:
                    return GridView(request,grid_model,**arg)
    return HTTPError(404, "File does not exist.")
    

from forms.encoding import smart_str #^^^^^^^^^^^^^^^^^^^
from mole_api  import json_dumps#^^^^^^^^^^^^^^     
         
def GridView(request,grid_model,**arg):
    m_grid = grid_model.grid
    grid_model.SetPageSize(arg['psize'])
    grid_model.MakeData(request,**arg)
    grid_model.grid.ParseArg(**arg)
    if not grid_model._paged:
        grid_model.Paging(arg['offset'])
    ret = m_grid.ResultDic()
    return smart_str(json_dumps(ret))

def GridExport(request,grid_model,**arg):
    m_grid = grid_model.grid

    hide_index = request.GET.get('hide',None)
    if hide_index:
        m_hide_index = [int(e) for e  in hide_index.split(',')]
    else:
        m_hide_index = []
    grid_model.SetPageSize(0)
    grid_model.MakeData(request,**arg)
    grid_model.grid.ParseArg(**arg)
    if not grid_model._paged:
        grid_model.Paging(1)
    ret = m_grid._GetData(m_hide_index)
    head = {}
    field = []
    i = 0
    for e in m_grid.dic:
        if i in m_hide_index:
            pass
        else:
            head[e[0]] = e[1]
            field.append(e[0])
        i +=1
    ret.insert(0, head)
    ret.insert(0, field)
    from grid_export import ExportGrid
    return ExportGrid(request,ret)
    
def AppPageView(request, app_label, model_name):
    from load import APP_PAGES
    key = '%s.%s'%(app_label, model_name)
    for e in APP_PAGES:
        if e[0]==key:
            return PageView(request, e[1])
    return HTTPError(404, "File does not exist.")

def PageView(request, model):
    page = model(request)
    menu_group = page.app_menu
    PageName = page.__class__.__name__

    m_urlparams = dict(request.GET)
    m_params = []
    for e in m_urlparams.keys():
        m_value = m_urlparams[e]
        if type(m_value)==type([]):
            m_value = ','.join(m_value)
        m_params.append({"name":str(e),"value":str(m_value)})
        
    response_context = {
                        'app_label':menu_group,
                        'model_name':PageName,
                        'urlparams':m_params,
                        'select_fieldname':request.GET.get('fieldname',''),
                        'ids':request.GET.get('ids',''),
                        'verbose_name':page.verbose_name}
#    if not page.template.endswith('_window.html'):
#        page.template = page.template.replace(".html","_pure.html")

    if page.context:
        if callable(page.context):
            response_context.update(page.context())
        else:
            response_context.update(page.context)
    return JTemplate(page.template,**response_context)

def FormActionView(request, app_label, model_name,action):
    from load import FORM_ACTIONS
    from custom_model import FormAction
    request.user = None
    if FORM_ACTIONS.has_key(app_label):
        if FORM_ACTIONS[app_label].has_key(model_name):
            form_actions = FORM_ACTIONS[app_label][model_name]
            for e in form_actions:
                if e[0]==action:
                    m_form_action = e[1]
                    try:
                        m_form_action().action(request)
                        return {"status":"ok", "msg":''}
                    except Exception, e:
                        return {"status":"err", "msg": '%s'%e.message}
            return {"status":"err", "msg": u'操作非法'}
        else:
            return {"status":"err", "msg": u'操作非法'}
    else:
        return {"status":"err", "msg": u'操作非法'}