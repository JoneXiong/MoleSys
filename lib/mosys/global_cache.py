# -*- coding: utf-8 -*-

from django.core.cache import cache

class CacheData(object):
    def __init__(self, key):
        ''''''
        self.key = key
        self.value = None
        
    def action_init(self):
        self.get()
        
    def refresh(self):
        '''刷新数据'''
        m_data = self.predata()
        cache.set(self.key, m_data, 60*60*24*7)
        return m_data
        
    def get(self):
        '''获取数据'''
        m_data = cache.get(self.key)
        if m_data:
            self.value = m_data
            return m_data
        else:
            self.value = self.refresh()
            return self.value
    data = property(get)
        
    def predata(self):
        '''准备数据'''
        pass
        
class NumRun(CacheData):
    
    def __init__(self):
        super(NumRun, self).__init__("C_NUM_RUN")
        
    def predata(self):
        '''返回" {班次ID : [周期单位, 周期数]}
        {id:[Units,Cyle]}    '''
        from get_run import get_emp_num_run
        return get_emp_num_run()
C_NUM_RUN = NumRun()

class AttRule(CacheData):
    
    def __init__(self):
        super(AttRule, self).__init__("C_ATT_RULE")
        
    def predata(self):
        from mysite.att.att_param import LoadAttRule
        return LoadAttRule()
C_ATT_RULE = AttRule()

JBD_DATA ={}