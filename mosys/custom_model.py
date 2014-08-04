# coding=utf-8

class AppPage(object):
    verbose_name=None
    icon_class = "menu_interact"
    app_menu =None
    menu_grup = '_default_grup'
    menu_index=0
    context = {}
    template = 'app_page.html'
    visible = True
    
    def __init__(self, request=None):
        pass
    
from forms.encoding import smart_str #^^^^^^^^^^^^^^^^^^^
from mole_api  import json_dumps#^^^^^^^^^^^^^^     

class GridModel(AppPage):
    verbose_name=None
    app_menu =None
    menu_index=0
    m_context = {}
    template = 'grid_model_pure.html'
    visible = False
    _firstrun = True
    
    head = {}
    option = {}
    search_form = []
    hide_list = []
#    buttons = []#[{},{}]
    grid = None
    _paged = False
    _binded = False
    
    def __init__(self, request=None):
        from grid_utils import GridBase
        self.grid = GridBase(self.head,self._GetPageSize())
        self.request = None
        self.hide_list = []
        self.m_context = {}
        
    def GetHeads(self):
        return self.grid.fields
    
    def Paging(self,offset,item_count=None):
        self.grid.paging(offset=offset,item_count=item_count)
        self._paged = True
    
    def SetPageSize(self,psize):
        self.grid.pagesize = psize
        #self.option["rp"] = psize
        
    def _GetPageSize(self):
        if self.option.has_key("rp"):
            return self.option["rp"]
        else:
            return 15
    
    def ParseLike(self,request):
        search_fields = [e[0] for e in self.search_form]
        for m in  search_fields:
            data = request.params.get(m, '')
            if data:
                self.grid.sql += " and %s like '%%%%%s%%%%'"%(m,data)
    
    def context(self):
        m_HeadDic = self.grid.HeadDic()
        app_label = self.app_menu
        model_name = self.__class__.__name__
        m_init_option = {
            "url":"/grid/%s/%s/"%(app_label, model_name),
            "dataType":"json",
            "usepager": True,
            "useRp": True,
            "rp": 15,
            "showTableToggleBtn":True,
            "onToggleCol":'$do_ToggleCol$',
            "onSubmit":'$do_Submit$',
            "pagestat":'显示 {from} 到 {to} ,共 {total} 条记录',
            'nomsg':'无记录',
            'procmsg':'正在处理中...',
            'pagetext':'第',
            'outof': '页 / 共',
            'findtext': '查找'
              }
        m_init_option.update(self.option)
        if self.__class__._firstrun:
            from load import FORM_ACTIONS
            if FORM_ACTIONS.has_key(app_label):
                if FORM_ACTIONS[app_label].has_key(model_name):
                    m_form_actions = FORM_ACTIONS[app_label][model_name]
                    if len(m_form_actions)>0:
                        if m_init_option.has_key("buttons"):
                            tar = m_init_option["buttons"]
                        else:
                            m_init_option["buttons"]=[]
                            tar = m_init_option["buttons"]
                        for e in m_form_actions:
                            tar.append( {"name": e[1].verbose_name, "bclass": e[1].icon, "onpress" : "$%s$"%e[0]} )
            self.__class__._firstrun=False
        
        m_HeadDic.update(m_init_option)
        addition = {"grid_option":smart_str(json_dumps(m_HeadDic)).replace('"$','').replace('$"','')}
        addition["hide_list"] = self.hide_list
        if self.search_form:
            ''' 查询表单的处理 '''
            import forms
            form=forms.Form()
            for e in self.search_form:
                field = e[1]
                form.fields[e[0]]=field
            addition["search_form"] = form
        addition.update(self.m_context)
        return addition
    
    def MakeData(self,request,**arg):
        '''
        组装 items 或 组装sql语句
        '''
        pass
    
    def SetBlank(self):
        self.Paging(1)
        self.grid.blank = True

    def SetHide(self,filed):
        self.grid.fields[filed]["hide"] = True
        self.hide_list.append(self.grid.GetFieldNames().index(filed))

    def AddContext(self,m_dict):
        self.m_context.update(m_dict)
        
    def BindO(self, orm):
        self._binded = True
        
class FormAction(object):
    verbose_name=None
    icon = "export_xls"
    model_name = None
    menu_index=0
    visible = True
    
    def __init__(self, request=None):
        pass
    
    def action(self,request=None):
        pass