#-*- coding: utf-8 -*-
'''
公共ini配置文件模块
'''

import os
from ConfigParser import ConfigParser

class Config(object):
    
    def __init__(self, inifile='data/config.ini'):
        self.inifile = inifile
        self.cfg = ConfigParser()
        if os.path.exists(inifile):
            self.cfg.read(inifile)

        # initialize configurations
        default_configs = {
            'server': {
                'ip': '*',
                'port': '8888',
                'lastcheckupdate': 0,
                'updateinfo': ''
            },
            'auth': {
                'username': 'admin',
                'password': '',     # empty password never validated
                'passwordcheck': 'yes',
            },
            'runtime': {
                'mode': '',
                'loginlock': 'off',
                'loginfails': 0,
                'loginlockexpire': 0,
            },
            'file': {
                'lastdir': '/root',
                'lastfile': '',
            },
        }
        needupdate = False
        for sec, secdata in default_configs.iteritems():
            if not self.cfg.has_section(sec):
                self.cfg.add_section(sec)
                needupdate = True
            for opt, val in secdata.iteritems():
                if not self.cfg.has_option(sec, opt):
                    self.cfg.set(sec, opt, val)
                    needupdate = True
        
        # update ini file
        if needupdate:
            self.update()
    
    def update(self):
        try:
            inifp = open(self.inifile, 'w')
            self.cfg.write(inifp)
            inifp.close()
            return True
        except:
            return False
    
    def has_option(self, section, option):
        return self.cfg.has_option(section, option)
    
    def get(self, section, option):
        return self.cfg.get(section, option)
    
    def getboolean(self, section, option):
        return self.cfg.getboolean(section, option)
    
    def getint(self, section, option):
        return self.cfg.getint(section, option)
    
    def has_section(self, section):
        return self.cfg.has_section(section)
    
    def add_section(self, section):
        return self.cfg.add_section(section)

    def set(self, section, option, value):
        try:
            self.cfg.set(section, option, value)
        except:
            return False
        return self.update()