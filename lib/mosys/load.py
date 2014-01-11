# -*- coding: utf-8 -*-

def getAppPages():
    pass

APP_PAGES = []
SYS_MENUS = {}
SYS_MODELS = []
FORM_ACTIONS = {}

def ModelScan():
    import mosys
    from importlib import import_module
    from custom_model import AppPage,FormAction
    for app in mosys.apps.apps_list:
        app = app[0]
        app_name = '%s.%s'%(mosys.apps.__name__,app)
        try:
            app_models = import_module('.models', app_name)
        except ImportError:
            import traceback
            traceback.print_exc()
        
        SYS_MENUS[app] = {'_default_grup':[]}
        FORM_ACTIONS[app] = {}
        app_global = import_module('%s.%s'%(mosys.apps.__name__,app))
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
                            SYS_MENUS[app][m.menu_grup].append( (m.verbose_name, '/page/%s/%s/'%(app,m.__name__), m.icon_class, '') )
                    else:
                        SYS_MENUS[app]['_default_grup'].append( (m.verbose_name, '/page/%s/%s/'%(app,m.__name__), m.icon_class, '') )
                if issubclass(m, FormAction):
                    model_name = m.model_name
                    if FORM_ACTIONS[app].has_key(model_name):
                        if m.visible:
                            FORM_ACTIONS[app][model_name].append( (m.__name__, m) )
                    else:
                        FORM_ACTIONS[app][model_name] = []
                        if m.visible:
                            FORM_ACTIONS[app][model_name].append( (m.__name__, m) )
                elif len(m.__bases__)>0 and m.__bases__[0].__name__ in ('CrudModel','BaseModel','Model') and m.__name__ not in ['Model','CrudModel','BaseModel']:
                    if hasattr(m,"load"):
                        if not m.load:
                            continue
                    SYS_MODELS.append( ('%s.%s'%(app,m.__name__), m) )
                    from mocrud.admin import ModelAdmin,admin
                    m_admin = None
                    if hasattr(m,"Admin"):
                        if issubclass(m.Admin, ModelAdmin):
                            m_admin = m.Admin
                    if m_admin==None:
                        m.Admin = m_admin = ModelAdmin
                        admin.register(app,m)
                    else:
                        admin.register(app,m,m_admin)
                    o_admin = admin[m]    
                    if SYS_MENUS[app].has_key(m_admin.menu_grup):
                        if m_admin.visible:
                            SYS_MENUS[app][m_admin.menu_grup].append( (o_admin.get_display_name(), '/admin/%s/'%(o_admin.get_admin_name()), m_admin.icon_class, o_admin.get_admin_name()) )
                    else:
                        SYS_MENUS[app]['_default_grup'].append( (o_admin.get_display_name(), '/admin/%s/'%(o_admin.get_admin_name()), m_admin.icon_class, o_admin.get_admin_name()) )
            except TypeError:
                pass
    if len(SYS_MODELS)>0:
        from mocrud.admin import admin
        admin.setup()
    print '>>> APP_PAGES--------------',APP_PAGES
    print '>>> SYS_MENUS-------------',SYS_MENUS
    print '>>> SYS_MODELS------------',SYS_MODELS
    
    
def GetModel(app_label, model_name):
    pass

def GetPage(app_label, page_name):
    pass