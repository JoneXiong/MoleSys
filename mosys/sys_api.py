# -*- coding: utf-8 -*-
import copy

from load import GetModel as get_model

def register_admin(app_label, model_name, admin_cls):
    from mocrud.admin import admin
    m_model = get_model(app_label, model_name)
    m_model.Admin = admin_cls
    #admin.register(app_label, m_model, admin_cls)
    
def register_op(app_label, model_name, op_cls):
    from mocrud.admin import admin
    m_model = get_model(app_label, model_name)
    m_ops = copy.deepcopy(m_model.Admin.ops)
    m_ops.append(op_cls)
    m_model.Admin.ops = m_ops
#    m_admin = admin._registry[m_model]
#    m_admin.ops.append(op_cls)