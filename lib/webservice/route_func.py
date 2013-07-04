# -*- coding: utf-8 -*-
from http_server_api import *
from ladon_port import get_charset, parse_environ, generate_service

EnvelopeDebug = True

def ServiceInstanceView(request,sinst,interface):
    from ladon.interfaces import name_to_interface
    from ladon.server.dispatcher import Dispatcher
    from ladon.server.customresponse import CustomResponse
    from ladon.tools.multiparthandler import MultiPartReader, MultiPartWriter
    try:
        '''检验请求的协议是否合法 soap/jsonwsp'''
        ifclass = name_to_interface(interface)
        if ifclass:
            charset = get_charset(request.environ,default='UTF-8')
            dispatcher = Dispatcher(sinst,ifclass,charset)#获得此服务调度器
            if dispatcher and dispatcher.iface:
                if request.path.endswith('description/') or request.path.endswith('description'):
                    '''描述视图'''
                    content_type = dispatcher.iface.description_content_type()
                    service_url = 'http://%s%s'%(request.environ["HTTP_HOST"],request.path.replace('/description/','').replace('/description',''))
                    m_content = dispatcher.iface.description(service_url,charset)
                    return HttpResponse(m_content,content_type=content_type)
                else:
                    '''执行视图'''
                    if request.method=="POST":
                        content_type = dispatcher.iface.response_content_type()
    #                    request_data = request.raw_post_data
                        environ = request.environ
                        
                        content_length = int(environ.get('CONTENT_LENGTH','0'))
                        multipart,boundary = parse_environ(environ)
                        if multipart and boundary:
                            ''' 文件上传 '''
                            mph = MultiPartReader(20000,boundary.encode(charset),environ['wsgi.input'],content_length)
                            mph.read_chunk()
                            while not mph.eos:
                                mph.read_chunk()
                            encapsulated_charset = get_charset(mph.interface_request_headers,default=None)
                            request_data = mph.interface_request
                            if encapsulated_charset:
                                # If a specific charset is/usr/local/bin/rdesktop specified for the interface request multipart
                                # let this charset superseed the charset globally specified for the request.
                                dispatcher.response_encoding = encapsulated_charset
                            
                            environ['attachments'] = mph.attachments
                            environ['attachments_by_id'] = mph.attachments_by_id
                        else:
                            request_data = environ['wsgi.input'].read(content_length)#################################################request.raw_post_data
                        if EnvelopeDebug:
                            print '>>>receive envelope: \n'
                            print request_data
                            print '<<<'

                        response_part = dispatcher.dispatch_request(request_data,environ)#解析、返回信封

                        if EnvelopeDebug:
                            print '>>>return envelope: \n'
                            print response_part
                            print '<<<'
                        if isinstance(response_part,CustomResponse):
                            ''' 返回自定义视图 '''
                            response_headers = response_part.response_headers()
                            response = HttpResponse(response_part.response_data(),content_type=content_type)
                            for k,v in response_headers:
                                response._iterator[k.lower()] = (k,v)
                            return response
                        elif len(environ['response_attachments'].attachments_by_cid): #返回文件的标记 response_attachments
                            ''' 文件下载 '''
                            # Attachments present - Send multipart response
                            import tempfile
                            response_temp_fname = tempfile.mktemp()
                            temp_buffer = open(response_temp_fname,'wb')
                            mpw = MultiPartWriter(temp_buffer)
                            mpw.add_attachment(response_part,'%s, charset=%s' % (content_type,charset),'rpc-part')
                            for cid,a in environ['response_attachments'].attachments_by_cid.items():
                                mpw.add_attachment(a,'application/octet-stram',cid,a.headers)
                            mpw.done()
                            temp_buffer.close()
                            content_length = str(os.stat(response_temp_fname).st_size)
                            output = open(response_temp_fname,'rb')
                            if sys.version_info[0]==2:
                                content_type = "multipart/related; boundary=" + mpw.boundary
                            elif sys.version_info[0]>=3:
                                content_type = "multipart/related; boundary=" + str(mpw.boundary,'iso-8859-1')
                                    
                            if hasattr(output,'read'):
                                # File-like object
                                block_size = 4096
                                if 'wsgi.file_wrapper' in environ:
                                    return environ['wsgi.file_wrapper'](output, block_size)
                                else:
                                    return HttpResponse(iter(lambda: output.read(block_size), ''),content_type=content_type)
                            
                        else:
                            ''' 返回文本内容 '''
                            # No attachments - Send normal response
                            return HttpResponse(response_part,content_type=content_type)
                        if 'attachments_by_id' in environ:
                            for a_id,a_info in environ['attachments_by_id'].items():
                                os.unlink(a_info['path'])
                    else:
                        return getJSResponse(u'Requests for %s interface must be posted' %interface)
            else:   
                return  getJSResponse(u'There is something error in The interface "%s"' % interface)
        else:
            return  getJSResponse(u'The interface name "%s" has not been defined' % interface)
    except:
        import traceback
        traceback.print_exc()
        return HTTPError(500,u'An Error occured while processing the request') 

#@valid_user    
def ServiceList():
    from ladon.ladonizer.collection import global_service_collection
    '''获取请求的service实例'''
    services = global_service_collection().services
    catalog_name = u"Zkeco 通讯接口文档 | 通讯中间件 | 系统对接接口"
    catalog_desc = u'''1. 一个基于PUSH SDK的数据通讯和分发中心<br><br>
    2. 基于这些接口即可现实和Zkeco一样的数据通讯和管理功能,目前Zkeco考勤通讯本身即使用了此作为通讯模块<br><br>
    3. 同时提供 SOAP 和 JSON 的支持，前端即可通过JS来调用,主要用于将代码中的业务逻辑的处理方法发布成web服务接口, JSON调用<a href='/media/demo1.jpg'>Demo</a>,SOAP调用<a href='/media/demo2.jpg'>Demo</a><br><br>
    4. 打开调试模式即可在线在web界面调用接口方法 ( 通过js走Json通道 )<br><br>
    5. 提供在线查看数据通讯中心所有数据的界面 <a href='#'>进入</a> ( finnger: 指纹模块数据目录; face: 面部模块数据目录; emp_pic: 人员照片数据目录; att_rec: 考勤记录; att_pic: 考勤照片 )<br><br>
    6. 数据通讯中心的数据只有 "考勤记录" 需要对接的业务系统转储到数据库, 其他数据本身已经做了结构化存储,由通讯中心自己维护
    '''
    catalog_info = {
        'catalog_name': catalog_name,
        'catalog_desc': catalog_desc,
        'charset': 'utf-8',
        'services': services.values()
    }
    return render_to_response('service_list.html',RequestContext(request,catalog_info))
    
add_route(ServiceList, '/rpc/',method=['GET'])


#@valid_user    
def NamedSoapView(service_name):
    from ladon.ladonizer.collection import global_service_collection
    '''获取请求的service实例�'''
    service_search = global_service_collection().services_by_name(service_name)
    if not len(service_search):
        return  getJSResponse(u'Service "%s" has not been exposed' % service_name)
    else:
        sinst = service_search[0]
        service_info = generate_service(sinst)
        return render_to_response('service_index.html',RequestContext(request,service_info))
    
add_route(NamedSoapView, '/rpc/:service_name/',method=['GET','POST'])


#@valid_user
def NamedServiceView(service_name,interface):
    from ladon.ladonizer.collection import global_service_collection
    '''获取请求的service实例�'''
    service_search = global_service_collection().services_by_name(service_name)
    if not len(service_search):
        return  getJSResponse(u'Service "%s" has not been exposed' % service_name)
    else:
        sinst = service_search[0]
        return ServiceInstanceView(request,sinst,interface)
    
add_route(NamedServiceView, '/rpc/:service_name/:interface',method=['GET','POST'])
add_route(NamedServiceView, '/rpc/:service_name/:interface/description',method=['GET','POST'])