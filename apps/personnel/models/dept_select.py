# -*- coding: utf-8 -*-
from mosys.custom_model import AppPage,GridModel
from mosys import forms

from apps.personnel.common import GetAuthoIDs

    
class DeptSelect(GridModel):
    '''
    组织选择
    '''
    
    verbose_name=u'组织选择'
    icon_class = "menu_vault"
    app_menu ="personnel"
    menu_index=15
    visible = False
    head = [('DeptID',u'DeptID'),('code',u'组织代码'),('DeptName',u'组织名称')]
    search_form = [
                   ('DeptName',forms.CharField(label=u'组织名称')),
                   ('code',forms.CharField(label=u'组织代码')),
                   ]
    option = {
            "usepager": True,
            "useRp": True,
            "rp": 20,
            "height":195,
            'checkbox' : True,
            "showTableToggleBtn":False,
            "onToggleCol" : False,
            'sortname' : "code",
            'sortorder' : "asc",
            "buttons":[
                       {"name": '选择', "bclass": 'select', "onpress" : '$do_select$'},
                       ],
              }
    def __init__(self, request):
        super(DeptSelect, self).__init__()
        #设置sql
        from mosys.sql_utils import  get_sql
        self.grid.sql = get_sql("sqls","dept_select")
      
        #设置 colum 属性
        self.grid.fields["DeptID"]["width"]=10
        self.grid.fields["code"]["width"]=200
        self.grid.fields["DeptName"]["width"]=200
        
        self.grid.fields["DeptID"]["hide"] = True
    def MakeData(self,request,**arg):
        self.ParseLike(request)
        deptids = GetAuthoIDs(request.user,1)    
        if deptids:
            self.grid.sql += " and DeptID in (%s)"%deptids
       #添加数据
        pass