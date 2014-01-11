# -*- coding: utf-8 -*-

from mosys.custom_model import AppPage,GridModel
from mosys import forms
#from ooredis import *

class DeviceReport(GridModel):
    '''
    设备管理
    '''
    verbose_name=u'设备管理'
    app_menu ="att"
    menu_grup = 'att_report'
    icon_class = "menu_monitor"
    template = 'device_report.html'
    menu_index=15
    visible = True
    head = [('sn',u'序列号'),('ipaddress',u'IP地址'),('area',u'区域'),('cmds',u'命令数')]
#    search_form = [
#                   ('sn',forms.CharField(label=u'序列号'))
#                   ]
    option = {
            "usepager": True,
            "useRp": True,
            "rp": 20,
            "height":350,
            'checkbox' : True,
            "showTableToggleBtn":True,
            "buttons":[
                       {"name": '导出xls', "bclass": 'export_xls', "onpress" : '$do_export$'},
                       {"name": '注册设备', "bclass": 'export_xls', "onpress" : '$do_register$'},
                       {"name": '清除考勤照片', "bclass": 'export_xls', "onpress" : '$do_confirm$'},
                       {"name": '清除考勤记录', "bclass": 'export_xls', "onpress" : '$do_confirm$'},
                       {"name": '新增对公短消息', "bclass": 'export_xls', "onpress" : '$do_dgdxx$'},
                       {"name": '重新上传数据', "bclass": 'export_xls', "onpress" : '$reUpload$'},
                       {"name": '重启设备', "bclass": 'export_xls', "onpress" : '$do_confirm$'},
                       {"name": '获取设备信息', "bclass": 'export_xls', "onpress" : '$do_confirm$'},
                       {"name": '同步数据到设备', "bclass": 'export_xls', "onpress" : '$do_confirm$'},
                       {"name": '删除', "bclass": 'export_xls', "onpress" : '$do_confirm$'},
                       ],
              }
    def __init__(self, request):
        super(DeviceReport, self) .__init__()
        self.grid.fields["sn"]["width"]=200
        self.grid.fields["ipaddress"]["width"]=200
        self.grid.fields["area"]["width"]=350
        
        from sync_action import get_area_data
        from mole.mole import json_dumps
        area_data = json_dumps(get_area_data())
        self.AddContext({'area_data':area_data})
        
    
    def MakeData(self,request,**arg):
        #添加数据
        from sync_action import get_device_sn_list,get_device_data_list
        keys_sn = request.params.get('sn',None)
        keys_area = request.params.get('area',None)
        if keys_area:
            sn_list = get_device_sn_list(keys_sn)
        else:
            sn_list = get_device_sn_list(keys_sn)
        self.Paging(arg['offset'],item_count=len(sn_list))
        m_sn = sn_list[self.grid._begin:self.grid._end]
        m_device_data = get_device_data_list(m_sn)
        
        self.grid.InitItems()
        for e in m_device_data:
            r = self.grid.NewItem()
            r["sn"] = e["sn"]
            r["ipaddress"] = e["ipaddress"]
            r["area"] = e["area"]
            r["cmds"] = e["cmds"]
            self.grid.AddItem(r)