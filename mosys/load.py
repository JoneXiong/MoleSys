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
    # 加载所有model
    for app in mosys.apps.apps_list:
        app = app[0]
        app_name = '%s.%s'%(mosys.apps.__name__,app)
        try:
            app_models = import_module('.models', app_name)
        except ImportError:
            import traceback
            traceback.print_exc()
        for attr in dir(app_models):
            m=app_models.__getattribute__(attr)
            try:
                if len(m.__bases__)>0 and ( m.__bases__[0].__name__ in ('CrudModel','BaseModel','Model') or  ( len(m.__bases__[0].__bases__)>0 and m.__bases__[0].__bases__[0].__name__ in ('CrudModel','BaseModel','Model')  )  ) and m.__name__ not in ['Model','CrudModel','BaseModel']:
                    SYS_MODELS.append( ('%s.%s'%(app,m.__name__), m) )
            except AttributeError:
                pass
            except TypeError:
                pass
    
    for app in mosys.apps.apps_list:
        app = app[0]
        app_name = '%s.%s'%(mosys.apps.__name__,app)
        try:
            app_models = import_module('.models', app_name)
        except ImportError:
            import traceback
            traceback.print_exc()
            
        try:
            app_admins = import_module('.admins', app_name)
            app_ops = import_module('.operates', app_name)
        except ImportError:
            import traceback
            traceback.print_exc()
        
        # app级key值得初始化
        SYS_MENUS[app] = {'_default_grup':[]}
        FORM_ACTIONS[app] = {}
        # 菜单配置处理
        app_global = import_module('%s.%s'%(mosys.apps.__name__,app))
        if hasattr(app_global,'menus'):
            m_menus = app_global.menus
            for e in m_menus:
                SYS_MENUS[app][e[0]] = []
        # 第二次大循环开始        
        for attr in dir(app_models):
            m=app_models.__getattribute__(attr)
            try:
                if issubclass(m, AppPage) and m.__name__ not in ['AppPage','GridModel']:
                    if not m.app_menu:
                        m.app_menu = app
                    APP_PAGES.append( ('%s.%s'%(app,m.__name__), m) )
                    if SYS_MENUS[app].has_key(m.menu_grup):
                        if m.visible:
                            SYS_MENUS[app][m.menu_grup].append( (m.verbose_name, '/page/%s/%s/'%(app,m.__name__), m.icon_class, '', m.menu_index) )
                    else:
                        if m.visible:
                            SYS_MENUS[app]['_default_grup'].append( (m.verbose_name, '/page/%s/%s/'%(app,m.__name__), m.icon_class, '', m.menu_index) )
                if issubclass(m, FormAction):
                    model_name = m.model_name
                    if FORM_ACTIONS[app].has_key(model_name):
                        if m.visible:
                            FORM_ACTIONS[app][model_name].append( (m.__name__, m) )
                    else:
                        FORM_ACTIONS[app][model_name] = []
                        if m.visible:
                            FORM_ACTIONS[app][model_name].append( (m.__name__, m) )
                elif len(m.__bases__)>0 and ( m.__bases__[0].__name__ in ('CrudModel','BaseModel','Model') or  ( len(m.__bases__[0].__bases__)>0 and m.__bases__[0].__bases__[0].__name__ in ('CrudModel','BaseModel','Model')  )  ) and m.__name__ not in ['Model','CrudModel','BaseModel']:
                    if hasattr(m,"load"):
                        if not m.load:
                            continue
                    #SYS_MODELS.append( ('%s.%s'%(app,m.__name__), m) )
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
                            SYS_MENUS[app][m_admin.menu_grup].append( (o_admin.get_display_name(), '/admin/%s/'%(o_admin.get_admin_name()), m_admin.icon_class, o_admin.get_admin_name(), o_admin.menu_index) )
                    else:
                        SYS_MENUS[app]['_default_grup'].append( (o_admin.get_display_name(), '/admin/%s/'%(o_admin.get_admin_name()), m_admin.icon_class, o_admin.get_admin_name(), o_admin.menu_index) )
            except AttributeError:
                pass
            except TypeError:
                pass
#    for app in mosys.apps.apps_list:
#        app = app[0]
#        app_name = '%s.%s'%(mosys.apps.__name__,app)
#        try:
#            app_models = import_module('.admins', app_name)
#            app_models = import_module('.operates', app_name)
#        except ImportError:
#            import traceback
#            traceback.print_exc()
    if len(SYS_MODELS)>0:
        from mocrud.admin import admin
        admin.setup()
        m_pages = admin.get_pages()
        for m in m_pages:
            app = m.app_menu
            if SYS_MENUS.has_key(app):
                if SYS_MENUS[app].has_key(m.menu_grup):
                    if m.visible:
                        SYS_MENUS[app][m.menu_grup].append( (m.verbose_name, '/admin/fp/%s/'%m.__class__.__name__, m.icon_class, m.__class__.__name__, m.menu_index) )
                else:
                    if m.visible:
                        SYS_MENUS[app]['_default_grup'].append( (m.verbose_name, '/admin/fp/%s/'%m.__class__.__name__, m.icon_class, m.__class__.__name__, m.menu_index) )
    
    print '>>> APP_PAGES--------------',APP_PAGES
    print '>>> SYS_MENUS-------------',SYS_MENUS
    print '>>> SYS_MODELS------------',SYS_MODELS
    
    
def GetModel(app_label, model_name):
    all_model_dict = dict(SYS_MODELS)
    m_key = '%s.%s'%(app_label, model_name)
    return all_model_dict[m_key]

def GetPage(app_label, page_name):
    pass