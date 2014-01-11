# -*- coding: utf-8 -*-
from mosys.custom_model import AppPage,GridModel
from mosys import forms


import model_custom_sql as sqlUtil
from apps.personnel.common import GetAuthoIDs

class EmpSelect(GridModel):
    '''
    人员选择
    '''
    
    verbose_name=u'人员选择'
    icon_class = "menu_people"
    app_menu ="personnel"
    menu_index=15
    visible = False
#    template = 'TransInfo_GridModel.html'
    head = [('userid',u'userid'),('badgenumber',u'身份证号码'),('name',u'姓名'),('DeptName',u'组织'),('code',u'组织代码'),('DeptID',u'组织ID')]
    search_form = [
                   ('DeptName',forms.CharField(label=u'组织名称')),
                   ('code',forms.CharField(label=u'组织代码')),
                   ('name',forms.CharField(label=u'人员姓名')),
                   ('badgenumber',forms.CharField(label=u'身份证号码'))
                   ]
    option = {
            "usepager": True,
            "useRp": True,
            "rp": 20,
            "height":170,
            'checkbox' : True,
            "showTableToggleBtn":False,
            "onToggleCol" : False,
            'sortname' : "DeptName",
            'sortorder' : "asc",
            "buttons":[
                       {"name": '选择', "bclass": 'select', "onpress" : '$do_select$'},
                       ],
              }
    def __init__(self, request):
        super(EmpSelect, self).__init__()
        #设置sql
        from mosys.sql_utils import  get_sql
        self.grid.sql = get_sql("sqls","emp_select")#sqlUtil.getEmpSelectSql()
         
        #设置 colum 属性
        self.grid.fields["userid"]["width"]=10
        self.grid.fields["badgenumber"]["width"]=100
        self.grid.fields["name"]["width"]=100
        self.grid.fields["DeptName"]["width"]=120
        self.grid.fields["code"]["width"]=100
        
        self.grid.fields["userid"]["hide"] = True
        self.grid.fields["DeptID"]["hide"] = True
        
    def MakeData(self,request,**arg):
        #添加数据
        self.ParseLike(request)
        deptids = GetAuthoIDs(request.user,1)    
        if deptids:
            self.grid.sql += " and DeptID in (%s)"%deptids
        pass