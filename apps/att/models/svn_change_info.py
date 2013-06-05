# -*- coding: utf-8 -*-

from mosys.custom_model import AppPage,GridModel

from mosys import forms

class ChangeInfo(GridModel):
    '''
    更改日志
    '''
    verbose_name=u'更改日志'
    app_menu ="att"
    menu_grup = 'att_report'
    icon_class = "menu_monitor"
    menu_index=15
    visible = True
#    template = 'TransInfo_GridModel.html'
    head = [('version',u'提交版本'),('author',u'提交人'),('time',u'提交日期'),('file',u'文件名'),('path',u'文件目录'),('desc',u'修改原因')]
    search_form = [
                   ('author',forms.CharField(label=u'提交人', initial='jone')),
#                   ('start', models.DateTimeField(verbose_name=u'开始日期')),
#                   ('end', models.DateTimeField(verbose_name=u'结束日期')),
                   ]
    option = {
            "usepager": False,
#            "title": 'Countries',
            "useRp": True,
            "rp": 20,
            "height":380,
            'checkbox' : True,
            "showTableToggleBtn":True,
#            'sortname' : "DeptName",
#            'sortorder' : "asc",
            "buttons":[{"name": '导出xls', "bclass": 'export_xls', "onpress" : '$do_export$'}],
#            "searchitems" : [
#                {'display': '人员编号', 'name' : 'badgenumber', 'isdefault': True},
#                {'display': '姓名', 'name' : 'name'},
#                {'display': '所在部门', 'name' : 'DeptName'},
#                ],
              }
    def __init__(self, request):
        super(ChangeInfo, self) .__init__()
        #设置sql
        
        #设置 colum 属性
        self.grid.fields["version"]["width"]=80
        self.grid.fields["author"]["width"]=80
        self.grid.fields["time"]["width"]=150
        self.grid.fields["file"]["width"]=240
        self.grid.fields["path"]["width"]=300
        self.grid.fields["desc"]["width"]=400
        
   
    def MakeData(self,request,**arg):
       #添加数据
        m_list = ParseSvnInfo()
        m_author = request.POST.get('author', '')
        self.grid.InitItems()
        for e in m_list:
            r = self.grid.NewItem()
            r["version"] = e["version"]
            r["author"] = e["author"]
            if m_author:
                if r["author"]!=m_author:
                    continue
            r["time"] = e["time"]
            r["desc"] = '%s'%e["desc"]
            for m in e["action"]:
                r["file"] = '%s: %s'%(m[0],m[2])
                r["path"]= m[1]
                self.grid.AddItem(r)
        self.Paging(1)
        pass
    
    
    
def ParseSvnInfo():
    m_file = open("info.txt")
    lines = m_file.readlines()
    
    m_list = []
    i = 0
    m_len = len(lines)
    while(i<m_len):
        m_content = lines[i]
        if len(m_content)==0:
            continue
        record = {}
        record["version"] = m_content.replace('版本: ','').strip()#m_content[8:].strip()
        i = i + 1
        record["author"] = lines[i].replace('作者: ','').strip()#lines[i][8:].strip()
        i = i + 1
        record["time"] = lines[i].replace('日期: ','').strip()#lines[i][8:].strip()
        i = i + 2
        desc = ""
        while(not lines[i].startswith('----')):
            desc += '\n'+lines[i]
            i = i+1
        record["desc"] = desc.strip()
        i = i+1
        action = []
        while(len(lines[i].strip())!=0):
            #action += '\n'+lines[i]
            m_tmp = lines[i].split(":")
            p_split = m_tmp[1].rindex('/')+1
            action.append((m_tmp[0].strip(),m_tmp[1][:p_split].strip(),m_tmp[1][p_split:].strip()))
            i = i+1
        record["action"] = action
        m_list.append(record)
        i = i+1
    return m_list