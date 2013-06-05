# -*- coding: utf-8 -*-

def getAppPages():
    pass

APP_PAGES = []
SYS_MENUS = {}

def ModelScan():
    import apps
    from importlib import import_module
    from custom_model import AppPage
    for app in apps.apps_list:
        app = app[0]
        app_name = 'apps.%s'%app
        try:
            app_models = import_module('.models', app_name)
        except ImportError:
            import traceback
            traceback.print_exc()
        
        SYS_MENUS[app] = {'_default_grup':[]}
        app_global = import_module('apps.%s'%app)
        if hasattr(app_global,'menus'):
            m_menus = app_global.menus
            for e in m_menus:
                SYS_MENUS[app][e[0]] = []
                
        for attr in dir(app_models):
            m=app_models.__getattribute__(attr)
            try:
                if issubclass(m, AppPage) and m.__name__ not in ['AppPage','GridModel']:
                    APP_PAGES.append( ('%s.%s'%(app,m.__name__), m) )
                    if SYS_MENUS[app].has_key(m.menu_grup):
                        if m.visible:
                            SYS_MENUS[app][m.menu_grup].append( (m.verbose_name, '/page/%s/%s/'%(app,m.__name__), m.icon_class ) )
                    else:
                        SYS_MENUS[app]['_default_grup'].append( (m.verbose_name, '/page/%s/%s/'%(app,m.__name__), m.icon_class ) )
            except TypeError:
                pass