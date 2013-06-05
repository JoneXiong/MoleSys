# -*- coding: utf-8 -*-

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