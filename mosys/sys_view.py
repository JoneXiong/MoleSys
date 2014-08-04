# -*- coding: utf-8 -*-

def get_app_nemus(app_label):
    import mosys
    from load import SYS_MENUS
    from importlib import import_module
    if SYS_MENUS.has_key(app_label):
        app_menu = SYS_MENUS[app_label]
        app_global = import_module('%s.%s'%(mosys.apps.__name__, app_label) )
        ret_data = []
        if hasattr(app_global,'menus'):
            init_menu = app_global.menus
            for e in init_menu:
                if app_menu.has_key(e[0]):
                    ret_data.append( (e[1],e[2],app_menu[e[0]]) )
        m_default_grup = app_menu['_default_grup']
        if len(m_default_grup):
            ret_data.append( (u'其他', 'grup_configure',m_default_grup) )
        return ret_data
    else:
        return None