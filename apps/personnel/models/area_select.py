# -*- coding: utf-8 -*-
from mosys.custom_model import AppPage,GridModel
from mosys import forms


import model_custom_sql as sqlUtil
from apps.personnel.common import GetAuthoIDs
    
class AreaSelect(GridModel):
    '''
    项目区域选择
    '''
    
    verbose_name=u'项目区域选择'
    app_menu ="personnel"
    menu_index=15
    visible = False
#    template = 'TransInfo_GridModel.html'
    head = [('id',u'id'),('areaid',u'区域名称'),('areaname',u'区域编号')]
    search_form = [
                   ('areaid',forms.CharField(label=u'区域名称')),
                   ('areaname',forms.CharField(label=u'区域编号')),
                   ]
    option = {
            "usepager": True,
#            "title": 'Countries',
            "useRp": True,
            "rp": 20,
            "height":190,
            'checkbox' : True,
            "showTableToggleBtn":False,
            "onToggleCol" : False,
            'sortorder' : "asc",
            "buttons":[
                       {"name": '选择', "bclass": 'select', "onpress" : '$do_select$'},
                       ],
              }
    def __init__(self, request):
        super(AreaSelect, self).__init__()
        #设置sql
        from mosys.sql_utils import  get_sql
        self.grid.sql = get_sql("sqls","area_select")
         
        #设置 colum 属性
        self.grid.fields["id"]["width"]=10
        self.grid.fields["areaid"]["width"]=120
        self.grid.fields["areaname"]["width"]=120
        
        self.grid.fields["id"]["hide"] = True
        
    def MakeData(self,request,**arg):
        #添加数据
        self.ParseLike(request)
        areaids = GetAuthoIDs(request.user,2)    
        if areaids:
            self.grid.sql += " and id in (%s)"%areaids
        pass