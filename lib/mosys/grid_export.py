#coding=utf-8
import datetime
import sys
import os

def ExportGrid(request, grid_data, data_key=None):
    '''
    Grid导出
    '''
    format = request.GET.get('format','.xls')
    if not (request.method=="GET" and format and (format  in ('.xls','.pdf','.csv'))):
        return u'不支持的输出格式'
    try:
        emitter = EXCELEmitter()
        return emitter.render_data(request,grid_data)
    except UnicodeError:
        import traceback;traceback.print_exc();
        return u'编码出错，请另作选择'
    
class EXCELEmitter(object):
    """
    Excel emitter
    """
    def render_data(self, request,grid_data):
        from mole import redirect
        import xlwt
        title=request.GET.get("reportname",'')
        sheet_name=u"%s_%s"%('Sheet', datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        
        file_path = "./tmpfile"
        if not os.path.exists(file_path):
            os.makedirs(file_path)
            
        fields=grid_data[0]
        del grid_data[0]

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(sheet_name)
        
        fnt = xlwt.Font()
        fnt.name = 'Arial'
        #fnt.colour_index = 4
        #fnt.bold = True
        
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        
        align = xlwt.Alignment()
        align.horz = xlwt.Alignment.HORZ_CENTER
        align.vert = xlwt.Alignment.VERT_CENTER
        
        style = xlwt.XFStyle()
        style.font = fnt
        style.borders = borders
        style.alignment = align
        
        row_index=0
        for row in grid_data:
            col_index=0
            for col in fields:
                ws.write(row_index,col_index, row[col], style)
                ws.col(col_index).width=0x0d00+2000
                col_index+=1
            row_index+=1
        filename="%(d1)s_%(d2)s.xls"%{
            "d1":u"%s"%title,
            "d2":datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        }
        
        wb.save(u"%s/%s"%(file_path, filename))
        f="/tmpfile/"+filename
        return redirect(f.encode("utf-8"))
