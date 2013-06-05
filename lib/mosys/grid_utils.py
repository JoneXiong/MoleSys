# coding=utf-8
import datetime
class GridBase(object):
    '''
    Grid分页，排序和查询工具类
    '''
    def __init__(self,dic,pagesize=30):
        self.current_page = 1
        self.pagesize = pagesize
        
        self.dic = dic
        
        self.sql = None
        self.sql_count = None
        self.sql_data = None
        self.sql_order = None
        self.blank = False
        
        self.__fieldcaptions= [e[1] for e in self.dic]
        self.__fieldnames =  [e[0] for e in self.dic]
        self.colum_trans ={}
        self.fields = {}
        for e in self.dic:
            self.fields[e[0]] = {'name':e[0],'display':e[1]}
            
        self.CalculateItem = {}
        self.CalculateItems = None
        self.PagedItems = None
        self._begin = None
        self._end = None
        self.result = {}
        self.ReItemObj()
        
    def InitItems(self):
        self.CalculateItems = []
        
    def NewItem(self):
        for e in self.CalculateItem.keys():
            self.CalculateItem[e]=''
        return self.CalculateItem
       
    def AddItem(self,obj):
        self.CalculateItems.append(obj.copy())
        
    def ReItemObj(self,dic = None):
        if dic:
            self.dic = dic
            self.__fieldcaptions= [e[1] for e in self.dic]
            self.__fieldnames =  [e[0] for e in self.dic]            
        for e in self.__fieldnames:
            self.CalculateItem[e]=None
            
    def SaveTmp(self):
        pass
    
    def Export(self):
        pass
    
    def _ExecSql(self,sql):
        '''
        执行sql语言
        '''
        from sql_utils import p_query
        return p_query(sql)
#        from django.db import  connection
#        cursor = connection.cursor()
#        print sql
#        cursor.execute(sql)
#        return cursor.fetchall()
    
    
    def _GetCount(self):
        ret = 0
        if self.CalculateItems==None:
            if self.sql:
                if not self.sql_count:
                    self.sql_count = 'select count(1) from (%s) as m'%self.sql
                ''' 查询sql语句得到记录数 '''
                rows = self._ExecSql(self.sql_count)
                ret = rows[0][0]
                pass
        else:
            ret = len(self.CalculateItems)
        return ret
    
    def _GetData(self,hide_index=None):
        if self.blank:
            return []
        if self.PagedItems==None:
            if self.CalculateItems==None:
                if not self.sql_data:
                    if self.pagesize==0:
                        self.sql_data = self.sql_order
                    else:
                        self.sql_data = 'select * from (%s) t where t.r>%s and t.r<=%s'%(self.sql_order,self._begin,self._end)
    #                    self.sql_data = 'select  a.*,row_number() as r from (%s) as a where r>=%s and r<=%s '%(self.sql,self._begin,self._end)#
    #                    self.sql_data = 'select top %s t.* from (%s) t where t.row not in (select top %s a.row from (%s) a order by a.row) order by t.row'%(self.pagesize,self.sql,self._begin,self.sql)
    #                    self.sql_data = '%s LIMIT %s,%s  '%(self.sql,self._begin,self.pagesize)
                ''' 查询sql语句得到记录数 '''
                rows = self._ExecSql(self.sql_data)
                self.PagedItems = []
                for r in rows:
                    _item = self.NewItem().copy()
                    i = 0
                    for e in self.__fieldnames:
                        
                        if hide_index and (i in hide_index):
                            del _item[e]
                        else:
                            if r[i]:
                                if self.colum_trans.has_key(e):
                                    _item[e] = self.colum_trans[e](r,r[i])
                                else:
                                    if type(r[i])==datetime.datetime:
                                        _item[e] = r[i].strftime('%Y-%m-%d %H:%M:%S')
                                    else:
                                        _item[e] = r[i]
                            else:
                                _item[e] = ''
                        i +=1
                    self.PagedItems.append(_item.copy())
            else:
                self.PagedItems = self.CalculateItems
        return self.PagedItems
    
    def paging(self,item_count=None,offset=None,pagesize=None):
        '''
        实现标准的分页功能
        @param    item_count    记录总数
        @param    offset    当前页
        @param    pagesize 每页记录数
        @return    返回起止记录号、分页信息字典
        '''
        if not item_count:
            item_count = self._GetCount()
        if not offset:
            offset = self .current_page
        if pagesize==None:
            pagesize = self.pagesize
        
        if pagesize==0:
            offset = 1
            self._begin = 0
            self._end = item_count
        else:
            limit = pagesize
            if item_count % limit==0:
                page_count =item_count/limit
            else:
                page_count =int(item_count/limit)+1                        
            if offset>page_count and page_count:offset=page_count
    #        Result['item_count']=item_count
    
    #        Result['limit']=limit
    #        Result['from']=(offset-1)*limit+1
    #        Result['page_count']=page_count
            self._begin = (offset-1)*limit
            self._end = offset*limit
        Result = {}
        Result['total']=item_count
        Result['page']=offset
        if self.CalculateItems!=None:
            self.PagedItems = self.CalculateItems[self._begin:self._end]
        self.result.update(Result)
        
    def ItemData(self):
        for e in self.CalculateItems:
            print e
    def ItemCount(self):
        return  len(self.CalculateItems)
    def GetDatas(self):
        dd = []
        
    def ParseArg(self, **arg):
        '''
        内置的处理查询和排序的操作
        '''
        try:
            if arg.has_key("query"):
                if not self.sql_count:
                    self.sql_count = 'select count(1) from (%s) a'%self.sql
                self.sql ="select * target_from (%s) a where %s like '%s' "%(self.sql,arg["qtype"],'%%'+arg["query"]+'%%')
            else:
                if not self.sql_count:
                    self.sql_count = 'select count(1) from (%s) a'%self.sql
                self.sql ="select * target_from (%s) a "%self.sql
                
            if arg.has_key("sortname"):
                self.sql_order = self.sql.replace('target_from', ',row_number() over (order by %s %s) as r from'%(arg["sortname"],arg["sortorder"]))
            else:
                self.sql_order = self.sql.replace('target_from', ',row_number() over (order by %s desc) as r from'%self.__fieldnames[0])
        except:
            pass
        
    def HeadDic(self,**kargs):
        ret = {}
        ret['colModel'] = [self.fields[e] for e in self.__fieldnames]
        ret.update(kargs)
        return ret
    
    def ResultDic(self,page=1):
#        self.paging(offset=page)
#        self.result['fieldcaptions'] = [e[1] for e in self.dic]
#        self.result['fieldnames'] =  [e[0] for e in self.dic]
#        self.result['disableCols'] = []
#        self.result['tmp_name'] = self.SaveTmp()
        m_data = self._GetData()
        m_rows = []
        for e in m_data:
            m_row = {"id":e[self.__fieldnames[0]]}
            m_row.update(e)
#            _data = []
#            for f in self.__fieldnames:
#                _data.append(e[f])
#            m_row["cell"] = _data
            m_rows.append(m_row)
#        m_rows = [{"id":e.values()[0],"cell":e.values()} for e in m_data]
        self.result['rows'] = m_rows
        return self.result

    def GetFieldNames(self):
        return self.__fieldnames
