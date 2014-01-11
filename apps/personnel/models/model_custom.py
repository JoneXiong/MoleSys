#! /usr/bin/env python
# -*- coding: utf-8 -*-
#from django.db import models

from mosys.custom_model import AppPage,GridModel
from apps.personnel.widgets import FormatDateTimeFieldWidget,MultySelectFieldWidget
import model_custom_sql as sqlUtil

from mosys import forms

#from apps import dbpool
#connection = dbpool.connection()

class TransInfo(GridModel):
    '''
    人员调动
    '''
    
    verbose_name=u'人员调动'
    icon_class = "menu_interact"
    app_menu ="personnel"
    menu_grup = 'aboutEmp'
    menu_index=2
    visible = True
    template = 'TransInfo_GridModel.html'
    head = [
            ('userid',u'userid'),('defaultdeptid',u'defaultdeptid'),('name',u'姓名'),
            ('badgenumber',u'身份证号码'),('DeptName',u'组织名称'),('code',u'组织代码'),
            ('areaname',u'项目区域'),('areaid',u'areaid'),('pname',u'职位'),('pid',u'pid')
        ]
    search_form = [
                   ('defaultdeptid',forms.CharField(label=u'组织', initial='jone',widget=MultySelectFieldWidget(attrs= {'url':'/page/personnel/DeptSelect/?pure'}) )  ),
                   ('areaid',forms.CharField(label=u'项目区域',widget=MultySelectFieldWidget(attrs= {'url':'/page/personnel/AreaSelect/?pure'}) )  ),
                   ('pid',forms.CharField(label=u'职位',widget=MultySelectFieldWidget(attrs= {'url':'/page/personnel/PositionSelect/?pure'}) )  ),
                   ('name',forms.CharField(label=u'姓名')),
                   ('badgenumber',forms.CharField(label=u'身份证号码'))
                   ]
    option = {
            "usepager": True,
#            "title": 'Countries',
            "useRp": True,
            "rp": 20,
            "height":280,
            'checkbox' : True,
            "showTableToggleBtn":True,
            "buttons":[
#                       {"name": '导出', "bclass": 'add', "onpress" : '$do_export$'},
                       {"name": '调整组织', "bclass": 'dept_chg', "onpress" : '$do_deptchange$'},
                       {"name": '调整项目区域', "bclass": 'area_chg', "onpress" : '$do_areachange$'},
                       {"name": '调整职位', "bclass": 'pos_chg', "onpress" : '$do_positionchange$'},
                       {"name": '组织调动记录', "bclass": 'dept_chg', "onpress" : '$record_deptchange$'},
                       {"name": '项目区域调动记录', "bclass": 'area_chg', "onpress" : '$record_areachange$'},
                       {"name": '职位调动记录', "bclass": 'pos_chg', "onpress" : '$record_positionchange$'},
                       ],
            "searchitems" : [
                {'display': '身份证号码', 'name' : 'badgenumber', 'isdefault': True},
                {'display': '姓名', 'name' : 'name'},
                {'display': '所在组织', 'name' : 'DeptName'},
                ],
              }
    def __init__(self, request):
        super(TransInfo, self) .__init__()
        #设置sql
        self.grid.sql = sqlUtil.getTransInfoSql()
         
        #设置 colum 属性
        self.grid.fields["userid"]["width"]=10
        self.grid.fields["defaultdeptid"]["width"]=10
        self.grid.fields["name"]["width"]=100
        self.grid.fields["badgenumber"]["width"]=100
        self.grid.fields["DeptName"]["width"]=100
        self.grid.fields["code"]["width"]=100
        self.grid.fields["areaname"]["width"]=300
        self.grid.fields["areaid"]["width"]=10
        self.grid.fields["pname"]["width"]=300
        self.grid.fields["pid"]["width"]=10
        
        self.grid.fields["userid"]["hide"] = True
        self.grid.fields["defaultdeptid"]["hide"] = True
        self.grid.fields["areaid"]["hide"] = True
        self.grid.fields["pid"]["hide"] = True

    def MakeData(self,request,**arg):        
       #添加数据
        def GetIds(sql):
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return [str(row[0]) for row in rows]
        
        emp_ids = []
        areaid = request.params.get("areaid", '')
        if areaid:
            emp_ids +=  GetIds("select employee_id from userinfo_attarea where area_id in (%s)"%areaid)
        pid = request.params.get("pid", '')
        if pid:
            emp_ids +=  GetIds("select employee_id  from userinfo_position where position_id in (%s)"%pid)
        if emp_ids:
            m_emp = ','.join(set(emp_ids))
            self.grid.sql += " and userid in (%s)"%m_emp
        else:
            if areaid or pid:
                self.grid.sql += " and 1=2 "
                
        #deptids = GetAuthoIDs(request.user,1)    
        defaultdeptid = request.params.get("defaultdeptid", '')
        if defaultdeptid:
            self.grid.sql += " and defaultdeptid in (%s)"%defaultdeptid
#        elif deptids:
#            self.grid.sql += " and defaultdeptid in (%s)"%deptids
            
        name = request.params.get('name', '')
        if name:
            self.grid.sql += " and name like '%%%%%s%%%%'"%name
        badgenumber = request.params.get('badgenumber', '')
        if badgenumber:
            self.grid.sql += " and badgenumber like '%%%%%s%%%%'"%badgenumber
        pass
    
    


    
#class DeptSelectWindow(DeptSelect):
#    '''
#    window选择组织
#    '''
#    verbose_name=u' 选择组织'
#    app_menu ="personnel"
#    menu_index=15
#    visible = False
#    template = 'grid_model_window.html'
#    
    
#class AreaSelectWindow(AreaSelect):
#    '''
#    window选择项目区域
#    '''
#    verbose_name=u' 选择项目区域'
#    app_menu ="personnel"
#    menu_index=15
#    visible = False
#    template = 'grid_model_window.html'
#    
class PositionSelect(GridModel):
    '''
    职位选择
    '''
    
    verbose_name=u'职位选择'
    app_menu ="personnel"
    menu_index=15
    visible = False
#    template = 'TransInfo_GridModel.html'
    head = [('id',u'id'),('pname',u'职位名称'),('pcode',u'职位编号'),('dname',u'组织名称'),('dcode',u'组织代码'),('DeptID',u'组织ID')]
    search_form = [
                   ('pname',forms.CharField(label=u'职位名称')),
                   ('pcode',forms.CharField(label=u'职位编号')),
                   ('dname',forms.CharField(label=u'组织名称')),
                   ('dcode',forms.CharField(label=u'组织代码')),
                   ]
    option = {
            "usepager": True,
#            "title": 'Countries',
            "useRp": True,
            "rp": 20,
            "height":165,
            'checkbox' : True,
            "showTableToggleBtn":False,
            "onToggleCol" : False,
            "buttons":[
                       {"name": '选择', "bclass": 'select', "onpress" : '$do_select$'},
                       ],
              }
    def __init__(self, request):
        super(PositionSelect, self).__init__()
        #设置sql
        self.grid.sql = sqlUtil.getPositionSelectSql()
         
        #设置 colum 属性
        self.grid.fields["id"]["width"]=10
        self.grid.fields["pcode"]["width"]=120
        self.grid.fields["dname"]["width"]=120
        self.grid.fields["dcode"]["width"]=120
        self.grid.fields["dname"]["width"]=120
        
        self.grid.fields["id"]["hide"] = True
        self.grid.fields["DeptID"]["hide"] = True
        
    def MakeData(self,request,**arg):
        #添加数据
        self.ParseLike(request)
        deptids = GetAuthoIDs(request.user,1)    
        if deptids:
            self.grid.sql += " and DeptID in (%s)"%deptids
        pass
    
from dept_select import DeptSelect    
class DeptChange(DeptSelect):
    '''
    调整组织
    '''
    verbose_name=u' 调整组织'
    icon_class = "menu_pathing"
    app_menu ="personnel"
    menu_index=15
    visible = False
    template = 'dept_change.html'
    option = {
            "buttons":[],
            'checkbox' : True,
              }
 
from area_select import AreaSelect
class AreaChange(AreaSelect):
    '''
    调整项目区域
    '''
    
    verbose_name=u'调整项目区域'
    icon_class = "menu_monitor"
    app_menu ="personnel"
    menu_index=15
    visible = False
    template = 'area_change.html'
    option = {
            "buttons":[],
            'checkbox' : True,
              }
    
class PositionChange(PositionSelect):
    '''
    调整职位
    '''
    
    verbose_name=u'调整职位'
    icon_class = "menu_green"
    app_menu ="personnel"
    menu_index=15
    visible = False
    template = 'position_change.html'
    option = {
            "buttons":[],
            'checkbox' : True,
              }
    
class ChangeRecord(GridModel):
    '''
    调动记录
    '''
    
    WAIT = 1
    PASS = 2
    REFUSE = 3
    #当前状态
    AUDIT_STATUS=(
            (WAIT,u'待审核'),
            (PASS,u'审核通过'),
            (REFUSE,u'拒绝'),
    )
    
    verbose_name=u'调动记录'
    icon_class = "menu_home"
    app_menu ="personnel"
    menu_grup = 'aboutEmp'
    menu_index=3
    visible = True
#    template = 'position_change.html'
    head = [('id',u'id'),('UserID_id',u'UserID_id'),('badgenumber',u'身份证号码'),('name',u'姓名'),('changeType',u'调动类型'),
            ('oldvalue',u'调动前'), ('newvalue',u'调动后'),('currStatus',u'当前状态'),('applicationTime',u'申请时间'),
            ('changereason',u'申请原因'),('checkTime',u'审核时间'),('remark',u'审核备注'),('defaultdeptid',u'defaultdeptid')
            ]
    search_form = [
                   ('UserID_id',forms.CharField(label=u'人员',widget=MultySelectFieldWidget(attrs= {'url':'/page/personnel/EmpSelect/?pure'}) )  ),
                   ('defaultdeptid',forms.CharField(label=u'组织',widget=MultySelectFieldWidget(attrs= {'url':'/page/personnel/DeptSelect/?pure'}) )  ),
                   ('currStatus',forms.ChoiceField(label=u'状态',choices=AUDIT_STATUS, initial=WAIT))
                   ]
    option = {
            "usepager": True,
            "useRp": True,
            "rp": 20,
            "height":340,
            'checkbox' : True,
            "showTableToggleBtn":False,
            "onToggleCol" : False,
              }
    def __init__(self, request):
        super(ChangeRecord, self) .__init__()
        #设置sql
        self.grid.sql = sqlUtil.getChangeRecordSql()
        def getName(sql):
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return ",".join([row[0] for row in rows])
        
        def getValue(types,val): 
            """
            parm:
                type:类型
                val:id值
            return:
                name
            """
            if val=="" or val=="None":
                return ""
            deptSql = """
                select DeptName from departments where DeptID  in (%s)
            """%val
            
            areaSql="""
             select areaname from personnel_area where id in(%s)
            """ %val
            
            positionSql="""
                select name from personnel_positions where id in (%s)
            """%val
            if types==1:
                return getName(deptSql)
            elif types==2:
                return getName(areaSql)
            else:
                return getName(positionSql)
            
        def fooOldvalue(r):
            types = r[4] #调动类型对应sql语句中的第5列,如果sql语句中发生变化,请注意调整该处
            value = r[5] #调动前id值对应sql语句中的第6列,如果sql语句中发生变化,请注意调整该处
            return getValue(types,value)
        def fooNewvalue(r):
            type = r[4] #调动类型对应sql语句中的第5列,如果sql语句中发生变化,请注意调整该处
            value = r[6] #调动后id值对应sql语句中的第7列,如果sql语句中发生变化,请注意调整该处
            return getValue(type,value)
        
        def fooChangeType(r):
            """
                                    调动类型
            1:企业组织机构
            2:项目区域
            3:职位
            """
            val = r[4] #调动类型对应sql语句中的第5列,如果sql语句中发生变化,请注意调整该处
            if val==1:
                return u"企业组织机构"
            elif val==2:
                return u"项目区域"
            else:
                return u"职位"
        def fooCurrStatus(r):
            """
                                        当前状态
                1:待审核
                2:审核通过
                3:拒绝
            """
            val = r[7] #当前状态对应sql语句中的第8列,如果sql语句中发生变化,请注意调整该处
            if val ==1:
                return u"待审核"
            elif val ==2 :
                return u"审核通过"
            else:
                return u"拒绝"
        #设置 colum 属性
        self.grid.fields["id"]["width"]=10
        self.grid.fields["UserID_id"]["width"]=10
        self.grid.fields["badgenumber"]["width"]=100
        self.grid.fields["name"]["width"]=80
        self.grid.fields["changeType"]["width"]=80
        self.grid.fields["oldvalue"]["width"]=180
        self.grid.fields["newvalue"]["width"]=180
        self.grid.fields["applicationTime"]["width"]=120
        self.grid.fields["changereason"]["width"]=150
        self.grid.fields["currStatus"]["width"]=80
        self.grid.fields["checkTime"]["width"]=120
        self.grid.fields["remark"]["width"]=150
    
        self.grid.fields["id"]["hide"] = True
        self.grid.fields["UserID_id"]["hide"] = True
        self.grid.fields["defaultdeptid"]["hide"] = True
        
    
        self.grid.colum_trans["oldvalue"] = fooOldvalue
        self.grid.colum_trans["newvalue"] = fooNewvalue
        self.grid.colum_trans["changeType"] = fooChangeType
        self.grid.colum_trans["currStatus"] = fooCurrStatus
   
    def MakeData(self,request,**arg):
        #添加数据
        UserID_id = request.params.get("UserID_id", '')
        if UserID_id:
            self.grid.sql += " and UserID_id in (%s)"%UserID_id
            
        deptids = GetAuthoIDs(request.user,1)
        defaultdeptid = request.params.get("defaultdeptid", '')
        if defaultdeptid:
            self.grid.sql += " and defaultdeptid in (%s)"%defaultdeptid
        elif deptids:
            self.grid.sql += " and defaultdeptid in (%s)"%deptids
            
        changeType = request.params.get("changeType", '')
        currStatus = request.params.get("currStatus", '')
        if changeType:
            self.grid.sql += " and changeType=%s"%changeType
        if currStatus:
            self.grid.sql += " and currStatus=%s"%currStatus
        pass
    
class ChangeRecordGrid(ChangeRecord):
    verbose_name=u'人员调动记录'
    visible = False
    search_form = None
    option = {
            "height":400,
              }
    
#class ChangeRecordCheck(ChangeRecord):
#    verbose_name=u'人员审核'
#    menu_index=4
#    visible = False
#    search_form = None
#    template = 'change_record_check_GridModel.html'
#    option = {
#            "height":350,
#            'checkbox' : True,
#            "buttons":[
#                       {"name": '审核', "bclass": 'check', "onpress" : '$do_check$'},
#                       ]
#              }
#
#    def __init__(self):
#        super(ChangeRecordCheck, self) .__init__()
#        #设置sql
#        self.grid.sql = sqlUtil.getChangeRecordCheckSql()
#             
#        def getName(sql):
#            cursor = connection.cursor()
#            cursor.execute(sql)
#            rows = cursor.fetchall()
#            return ",".join([row[0] for row in rows])
#        
#        def getValue(types,val): 
#            """
#            parm:
#                type:类型
#                val:id值
#            return:
#                name
#            """
#            if val=="" or val=="None":
#                return ""
#            deptSql = """
#                select DeptName from departments where DeptID  in (%s)
#            """%val
#            
#            areaSql="""
#             select areaname from personnel_area where id in(%s)
#            """ %val
#            
#            positionSql="""
#                select name from personnel_positions where id in (%s)
#            """%val
#            if types==1:
#                return getName(deptSql)
#            elif types==2:
#                return getName(areaSql)
#            else:
#                return getName(positionSql)
#            
#        def fooOldvalue(r):
#            types = r[4] #调动类型对应sql语句中的第5列,如果sql语句中发生变化,请注意调整该处
#            value = r[5] #调动前id值对应sql语句中的第6列,如果sql语句中发生变化,请注意调整该处
#            return getValue(types,value)
#        def fooNewvalue(r):
#            type = r[4] #调动类型对应sql语句中的第5列,如果sql语句中发生变化,请注意调整该处
#            value = r[6] #调动后id值对应sql语句中的第7列,如果sql语句中发生变化,请注意调整该处
#            return getValue(type,value)
#        
#        def fooChangeType(r):
#            """
#                                    调动类型
#            1:企业组织机构
#            2:项目区域
#            3:职位
#            """
#            val = r[4] #调动类型对应sql语句中的第5列,如果sql语句中发生变化,请注意调整该处
#            if val==1:
#                return u"企业组织机构"
#            elif val==2:
#                return u"项目区域"
#            else:
#                return u"职位"
#        def fooCurrStatus(r):
#            """
#                                        当前状态
#                1:待审核
#                2:审核通过
#                3:拒绝
#            """
#            val = r[7] #当前状态对应sql语句中的第8列,如果sql语句中发生变化,请注意调整该处
#            if val ==1:
#                return u"待审核"
#            elif val ==2 :
#                return u"审核通过"
#            else:
#                return u"拒绝"
#        #设置 colum 属性
#        self.grid.fields["id"]["width"]=10
#        self.grid.fields["UserID_id"]["width"]=10
#        self.grid.fields["badgenumber"]["width"]=80
#        self.grid.fields["name"]["width"]=70
#        self.grid.fields["changeType"]["width"]=80
#        self.grid.fields["oldvalue"]["width"]=180
#        self.grid.fields["newvalue"]["width"]=180
#        self.grid.fields["applicationTime"]["width"]=120
#        self.grid.fields["changereason"]["width"]=150
#        self.grid.fields["currStatus"]["width"]=80
#        self.grid.fields["checkTime"]["width"]=120
#        self.grid.fields["remark"]["width"]=150
#    
#        self.grid.fields["id"]["hide"] = True
#        self.grid.fields["UserID_id"]["hide"] = True
#        self.grid.fields["currStatus"]["hide"] = True
#        self.grid.fields["checkTime"]["hide"] = True
#        self.grid.fields["remark"]["hide"] = True
#        self.grid.fields["defaultdeptid"]["hide"] = True
#        
#    
#        self.grid.colum_trans["oldvalue"] = fooOldvalue
#        self.grid.colum_trans["newvalue"] = fooNewvalue
#        self.grid.colum_trans["changeType"] = fooChangeType
#        self.grid.colum_trans["currStatus"] = fooCurrStatus
#        
#class ChangeCheckDialog(GridModel):
#    '''
#    调动审核对话框
#    '''
#    verbose_name=u' 审核'
#    app_menu ="personnel"
#    menu_index=15
#    visible = False
#    template = 'change_check_dialog.html'
#    
#class EmpTransCheck(GridModel):
#    '''
#    人员审核
#    '''
#    
#    verbose_name=u'人员审核'
#    app_menu ="personnel"
#    menu_index=16
#    visible = False
#    template = 'emp_trans_check_window.html'
#    head = [('id',u'id'),('badgenumber',u'身份证号码'),('name',u'姓名'),('DeptName',u'组织名称'),('code',u'组织代码')
#            ,('target',u'申请内容'),('applicationTime', u'申请时间')]
#    option = {
#            "usepager": True,
#            "useRp": True,
#            "rp": 20,
#            "height":350,
#            'checkbox' : True,
#            "showTableToggleBtn":False,
#            "onToggleCol" : False,
#            "buttons":[
#                       {"name": u'通过', "bclass": 'pass', "onpress" : '$do_pass$'},
#                       {"name": u'拒绝', "bclass": 'refuse', "onpress" : '$do_refuse$'},
#                       ]
#              }
#    def __init__(self):
#        super(EmpTransCheck, self) .__init__()
#        #设置sql
#        self.grid.sql = sqlUtil.getEmpTransCheckSql()
#        def fooTarget(r):
#            """
#                                    申请内容
#            1:新增
#            2:删除
#            """
#            val = r[5] #申请内容对应sql语句中的第6列,如果sql语句中发生变化,请注意调整该处
#            if val==1:
#                return u"新增"
#            elif val==2:
#                return u"删除"
#            else:
#                return u""
#        
#        #设置 colum 属性
#        self.grid.fields["id"]["width"]=10
#        self.grid.fields["badgenumber"]["width"]=80
#        self.grid.fields["name"]["width"]=70
#        self.grid.fields["DeptName"]["width"]=80
#        self.grid.fields["code"]["width"]=80
#        self.grid.fields["target"]["width"]=70
#        self.grid.fields["applicationTime"]["width"]=120
#        self.grid.fields["id"]["hide"] = True
#        
#        self.grid.colum_trans["target"] = fooTarget
#        
#    def MakeData(self,request,**arg):
#        self.ParseLike(request)
#        deptids = GetAuthoIDs(request.user,1)    
#        if deptids:
#            self.grid.sql += " and DeptID in (%s)"%deptids
#       #添加数据
#        pass
#    
#class SendMsgDialog(AppPage):
#    verbose_name=u'发送短信'
#    app_menu ="personnel"
#    menu_index=46
#    visible = False
#    template = 'send_msg.html'

def GetAuthoIDs(user,Type):
    '''
    Type:  1 授权组织 2 授权区域
    '''
    return None
    from mysite.personnel.models.model_deptadmin import  DeptAdmin
    from mysite.personnel.models.model_areaadmin import AreaAdmin
    if  user.is_superuser or user.is_anonymous :
        return None
    area_admin_ids = AreaAdmin.objects.filter(user=user).values_list("area_id",flat=True)
    if Type==1:
        ids =  DeptAdmin.objects.filter(user=user).values_list("dept_id",flat=True)
    if Type==2:
        ids = AreaAdmin.objects.filter(user=user).values_list("area_id",flat=True)
    if ids:
        return ','.join([str(i) for i in ids])
    else:
        return None