#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from mosys.custom_model import AppPage,GridModel
from apps.personnel.widgets import FormatDateTimeFieldWidget,MultySelectFieldWidget

from mosys import forms


class OrderAttReport(GridModel):
    '''
    出勤明细
    '''
    from django.utils.translation import ugettext as _
    verbose_name=u'出勤明细'
    app_menu ="att"
    menu_index=20
    visible = False
#    template = 'order_report.html'
    head = [('id',u'id'),('userid',u'userid'),('DeptID',u'DeptID'),('name',u'姓名'),('badgenumber',u'身份证号'),
            ('DeptName',u'组织名称'), ('attdate',u'考勤日期'),('attTimes',u'出勤时长'),
            ('attdays',u'出勤工作日'),('overtimes',u'加班时间'), ('leaveimes',u'请假时长'),
            ('stopWorkTimes',u'停工时长'),
            ]
    option = {
            "usepager": True,
            "useRp": True,
            "rp": 20,
            "height":300,
            'checkbox' : False,
            "showTableToggleBtn":False,
            "onToggleCol" : False,
              }
    def __init__(self, request):
        super(OrderAttReport, self).__init__()
        #设置sql
        from mosys.sql_utils import  get_sql
        self.grid.sql = get_sql("attResult","OrderAttReport")
        #设置 colum 属性
        self.grid.fields["name"]["width"]=100
        self.grid.fields["badgenumber"]["width"]=150
        self.grid.fields["DeptName"]["width"]=100
        self.grid.fields["attdate"]["width"]=80
        self.grid.fields["attTimes"]["width"]=50
        self.grid.fields["attdays"]["width"]=70
        self.grid.fields["overtimes"]["width"]=50
        self.grid.fields["leaveimes"]["width"]=50
        self.grid.fields["stopWorkTimes"]["width"]=50
        
        self.grid.fields["attTimes"]["sortable"]=True
        self.grid.fields["attdays"]["sortable"]=True

   
    def MakeData(self,request,**arg):
        #添加数据
        UserID_id = request.params.get("userid", '')
        if UserID_id:
            self.grid.sql += " and u.userid in (%s)"%UserID_id
            
        deptids = GetAuthoIDs(request.user,1)
        defaultdeptid = request.params.get("DeptID", '')
        if defaultdeptid:
            self.grid.sql += " and d.DeptID in (%s)"%defaultdeptid
        elif deptids:
            self.grid.sql += " and d.DeptID in (%s)"%deptids
            
        badgenumber =  request.params.get("badgenumber", '')
        if badgenumber:
            self.grid.sql += " and u.badgenumber like ('%%%%%s%%%%')"%badgenumber
        startDate = request.params.get("startDate", '')
        endDate = request.params.get("endDate", '')
        if startDate:
            startDate = datetime.datetime.strptime(startDate,'%Y-%m-%d')
            self.grid.sql += " and ar.attdate >= '%s'"%startDate
        if endDate:
            endDate = datetime.datetime.strptime((endDate+" 23:59:59"),'%Y-%m-%d %H:%M:%S')
            self.grid.sql += " and ar.attdate <= '%s'"%endDate
        pass
    
class SumAttReport(GridModel):
    '''
    出勤汇总
    '''
    from django.utils.translation import ugettext as _
    verbose_name=u'出勤报表'
    icon_class = "menu_pathing"
    menu_grup = 'att_report'
    app_menu ="att"
    menu_index=20
    visible = True
    template = 'attResult_report.html'
    head = [('userid',u'userid'),('DeptID',u'DeptID'),('name',u'姓名'),('badgenumber',u'工号'),
            ('DeptName',u'组织名称'),('attTimes_sum',u'应到'),
            ('attDays_sum',u'实到'),('overtimes_sum',u'加班时间'), ('leaveimes_sum',u'出勤时长'),
            ('stopWorkTimes_sum',u'应到时长'), ('completionRate',u'出勤率'),
            ]
    search_form = [
                   ('userid',forms.CharField(label=u'人员',widget=MultySelectFieldWidget(attrs= {'url':'/page/personnel/EmpSelect/?pure'}) )  ),
                   ('DeptID',forms.CharField(label=u'组织',widget=MultySelectFieldWidget(attrs= {'url':'/page/personnel/DeptSelect/?pure'}) )  ),
                   ('badgenumber',forms.CharField(label=u'工号')),
                   ('startDate', forms.DateTimeField(label=u'开始日期',widget =FormatDateTimeFieldWidget(attrs= {'format':'yyyy-MM-dd','readonly':'true'}),initial=datetime.datetime.now().strftime('%Y-%m-01'))),
                   ('endDate', forms.DateTimeField(label=u'结束日期',widget =FormatDateTimeFieldWidget(attrs= {'format':'yyyy-MM-dd','readonly':'true'}),initial=datetime.datetime.now().strftime('%Y-%m-%d'))),
                   ]
    option = {
            "usepager": True,
            "useRp": True,
            "rp": 20,
            "height":290,
            'checkbox' : False,
            "showTableToggleBtn":False,
            "onToggleCol" : False,
            "buttons":[{"name": '导出xls', "bclass": 'export_xls', "onpress" : '$do_export$'}],
              }
    def __init__(self, request):
        super(SumAttReport, self).__init__()
        #设置sql
        from mosys.sql_utils import  get_sql
        self.grid.sql = get_sql("attResult","SumAttReport")

        def fooRate(r,val):
            """
            出勤率
            """
            if int(r[5])==0:
                rate = "100%"
            else:
                rate = float(r[6])/float(r[5])
                return u"<font color=red>%10.2f</font>"%rate
            return rate    
            
        def fooName(r,val):
            """
            姓名转化
            """
            val_id = r[0]
            return '<a href="javascript:showDetail(%s);" title="">%s</a>'%(val_id,val)
        
        #设置 colum 属性
        self.grid.fields["name"]["width"]=100
        self.grid.fields["badgenumber"]["width"]=150
        self.grid.fields["DeptName"]["width"]=100
        self.grid.fields["attTimes_sum"]["width"]=80
        self.grid.fields["attDays_sum"]["width"]=80
        self.grid.fields["overtimes_sum"]["width"]=80
        self.grid.fields["leaveimes_sum"]["width"]=80
        self.grid.fields["stopWorkTimes_sum"]["width"]=80
        self.grid.fields["completionRate"]["width"]=150
        
        self.grid.fields["attTimes_sum"]["sortable"]=True
        self.grid.fields["attDays_sum"]["sortable"]=True
        self.grid.colum_trans["completionRate"] = fooRate
        self.grid.colum_trans["name"] = fooName
        
        self.SetHide("userid")
        self.SetHide("DeptID")
   
    def MakeData(self,request,**arg):
        #添加数据
        self.grid.sql = self.grid.sql.replace("group by u.userid,u.name,u.badgenumber,d.DeptName,d.DeptID","")
        UserID_id = request.params.get("userid", '')
        if UserID_id:
            self.grid.sql += " and u.userid in (%s)"%UserID_id
            
        deptids = GetAuthoIDs(request.user,1)
        defaultdeptid = request.params.get("DeptID", '')
        if defaultdeptid:
            self.grid.sql += " and d.DeptID in (%s)"%defaultdeptid
        elif deptids:
            self.grid.sql += " and d.DeptID in (%s)"%deptids
            
        badgenumber =  request.params.get("badgenumber", '')
        if badgenumber:
            self.grid.sql += " and u.badgenumber like ('%%%%%s%%%%')"%badgenumber
        startDate = request.params.get("startDate", '')
        endDate = request.params.get("endDate", '')
        if startDate:
            startDate = datetime.datetime.strptime(startDate,'%Y-%m-%d')
            self.grid.sql += " and ar.attdate >= '%s'"%startDate
        if endDate:
            endDate = datetime.datetime.strptime((endDate+" 23:59:59"),'%Y-%m-%d %H:%M:%S')
            self.grid.sql += " and ar.attdate <= '%s'"%endDate
        self.grid.sql+=" group by u.userid,u.name,u.badgenumber,d.DeptName,d.DeptID"
        pass
    
    
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