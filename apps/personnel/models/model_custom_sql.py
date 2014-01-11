# -*- coding: utf-8 -*-
"""
    用于存放模型所需要的sql语句的工具类,方法命名规则为   get****Sql (****表示模型名字)
"""
def getTransInfoSql():
    return  '''
                SELECT   
                      u.userid,u.defaultdeptid, u.name,u.badgenumber,d.code,d.DeptName, 
                    (SELECT areaname 
                        FROM ( 
                            SELECT  areaname + ',' 
                                FROM (
                                    SELECT DISTINCT areaname 
                                        FROM personnel_area a,userinfo_attarea ua
                                        where ua.area_id=a.id and ua.employee_id=u.userid
                                    ) AS SUM_COL 
                                FOR XML PATH('') 
                            )as SUM_AREA(areaname)
                    ) as areaname,
                    (SELECT areaid 
                        FROM ( 
                            SELECT  cast(id AS varchar(10))+',' 
                                FROM (
                                    SELECT DISTINCT a.id 
                                        FROM personnel_area a,userinfo_attarea ua
                                        where ua.area_id=a.id and ua.employee_id=u.userid
                                    ) AS SUM_COL 
                                FOR XML PATH('') 
                            )as SUM_AREA(areaid)
                    ) as areaid,
                    (select name
                        from (
                            select name+','
                                from (
                                    select DISTINCT pp.name
                                        from personnel_positions pp,userinfo_position up
                                        where u.userid = up.employee_id and pp.id = up.position_id
                                    )as    SUM_COL    
                                FOR XML PATH('') 
                            ) as SUM_POSITIONS(name)
                    )as pname,
                    (select pid
                        from (
                            select cast(id AS varchar(10))+','
                                from (
                                    select DISTINCT pp.id
                                        from personnel_positions pp,userinfo_position up
                                        where u.userid = up.employee_id and pp.id = up.position_id
                                    )as  SUM_COL    
                                FOR XML PATH('') 
                            ) as SUM_POSITIONS(pid)
                    )as pid
                from userinfo u ,  departments d 
                where u.defaultdeptid= d.DeptId 
            '''
            
def getEmpSelectSql():
    return '''
                select u.userid,u.badgenumber,u.name,d.DeptName,d.code,d.DeptID
                    from userinfo u
                    left join departments  d on d.DeptID=u.defaultdeptid
                    where u.status=0
            '''
            
            
def  getDeptSelectSql():
    return '''
               select DeptID,code,DeptName from departments 
                    where status=0
            '''  
            
def getAreaSelectSql():   
    return '''
                select id,areaid,areaname from personnel_area
                    where status = 0 
            '''  
def  getPositionSelectSql():
    return  '''
                select pp.id as id,pp.name as pname,pp.code as pcode,d.DeptName as dname, d.code as dcode,d.DeptID as DeptID
                    from personnel_positions as pp
                    left join departments as d on d.DeptID = pp.DeptID_id
                    where pp.status=0
            '''
            
def getChangeRecordSql():
    return '''
               select pe.id,pe.UserID_id,u.badgenumber,u.name,
                        changeType, pe.oldvalue,pe.newvalue,currStatus,
                        applicationTime,changereason,checkTime,remark,u.defaultdeptid
                    from personnel_empdiaodong pe,userinfo u
                    where pe.UserID_id=u.userid
            '''
            
def getChangeRecordCheckSql():
    return '''
               select pe.id,pe.UserID_id,u.badgenumber,u.name,
                        changeType, pe.oldvalue,pe.newvalue,currStatus,
                        applicationTime,changereason,checkTime,remark,u.defaultdeptid
                    from personnel_empdiaodong pe,userinfo u
                    where pe.UserID_id=u.userid
                        and pe.currStatus=1
            '''
def getEmpTransCheckSql():
    return '''
                select pe.id,u.badgenumber,u.name,d.DeptName,d.code,target,
                        pe.applicationTime from personnel_empupdate pe
                    left join userinfo u on  u.userid = pe.userid
                    left join departments d on u.defaultdeptid = d.DeptID
                    where pe.currStatus=1
            '''