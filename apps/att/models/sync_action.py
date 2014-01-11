# -*- coding: utf-8 -*-

def get_area_data():
    data =[
            {"id":1,"pId":0,"name":"区域名称","t":"区域名称tip","open":True},
            {"id":11,"pId":1,"name":"区域名称1"},
            {"id":12,"pId":1,"name":"区域名称2"},
            {"id":2,"pId":0,"name":"区域","open":True,"click":False},
            {"id":21,"pId":2,"name":"区域1"},
            {"id":22,"pId":2,"name":"区域2"},
            ]
    return data

def get_device_data_list(sn_list=None):
    data =[
            {"sn":"123456789","ipaddress":"127.0.0.1","area":"区域名称","cmds":"20","别名":"门房"},
            {"sn":"123456789","ipaddress":"127.0.0.1","area":"区域名称","cmds":"20","别名":"门房"},
            {"sn":"123456789","ipaddress":"127.0.0.1","area":"区域名称","cmds":"20","别名":"门房"},
            {"sn":"123456789","ipaddress":"127.0.0.1","area":"区域名称","cmds":"20","别名":"门房"},
            {"sn":"123456789","ipaddress":"127.0.0.1","area":"区域名称","cmds":"20","别名":"门房"},
            {"sn":"123456789","ipaddress":"127.0.0.1","area":"区域名称","cmds":"20","别名":"门房"},
            ]
    return data

def get_device_sn_list(keyword=None):
    data =["123456789","123456789","123456789","123456789"]
    return data

#    m_client = get_client()
#    keys = m_client.keys("device:*:data")
#    ret = []
#    from sync_action import get_area_data
#    area_data = json_dumps(get_area_data())
#    for e in keys:
#        data =  Dict(e)
#        sn = e.split(':')[1]
#        m_tar = [sn, data["ipaddress"],data["area"]]
#        oo_cmd = SortedSet("device:%s:update"%sn)
#        m_tar.append(len(oo_cmd))
#        ret.append(m_tar)