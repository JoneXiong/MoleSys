# -*- coding: utf-8 -*-

from mosys import forms

def flatatt(attrs):
    """
    Convert a dictionary of attributes to a single string.
    The returned string will contain a leading space followed by key="value",
    XML-style pairs.  It is assumed that the keys do not need to be XML-escaped.
    If the passed dictionary is empty, then return an empty string.
    """
    return u''.join([u' %s="%s"' % (k, v) for k, v in attrs.items()])

def mark_safe(content):
    return content

class FormatDateTimeFieldWidget(forms.TextInput):
    """
    A DateTime Widget that has some admin-specific styling.
    """
    def __init__(self, attrs={}):

        super(FormatDateTimeFieldWidget, self).__init__(attrs=attrs)
            
    def render(self, name, data, attrs=None):
        self.attrs.update(attrs)
        final_attrs=self.attrs
        final_attrs['name'] = name
        if data:
            _value = str(data)
        else:
            _value = ""
        ret_str = u'''
            <input %s value="%s" class="date" type="text" />
            '''%(flatatt(final_attrs),_value)
        return mark_safe(ret_str)
    
class EmpSelectFieldWidget(forms.TextInput):
    """
    A DateTime Widget that has some admin-specific styling.
    """
    def __init__(self, attrs={}):

        super(EmpSelectFieldWidget, self).__init__(attrs=attrs)
            
    def render(self, name, data, attrs=None):
        self.attrs.update(attrs)
        final_attrs=self.attrs
        final_attrs['name'] = name
        if data:
            _value = str(data)
        else:
            _value = ""
        ret_str = u'''
            <input %s  class="required"  value="" type="hidden">
            <div style="float:left">
                <div style="float:left"><input name="%s_orgName"  value="%s" type="text" readonly="readonly" /></div>
                <span style="float:left"><a class="btnLook" href="/page/personnel/EmpSelect/?pure&fieldname=UserID" lookupGroup="org">选择人员</a></span>
            </div>
            '''%(flatatt(final_attrs), final_attrs['name'], _value)
        return mark_safe(ret_str)
    
class MultySelectFieldWidget(forms.TextInput):
    """
    A DateTime Widget that has some admin-specific styling.
    """
    def __init__(self, attrs={}):

        super(MultySelectFieldWidget, self).__init__(attrs=attrs)
            
    def render(self, name, data, attrs=None):
        self.attrs.update(attrs)
        final_attrs=self.attrs.copy()
        m_url = final_attrs.pop("url")
        final_attrs['name'] = name
        if data:
            _value = str(data)
        else:
            _value = ""
        ret_str = u'''
            <input %s  class="required"  value="" type="hidden">
            <div style="float:left">
                <div style="float:left"><input name="%s_orgName"  value="%s" type="text" readonly="readonly" /></div>
                <span style="float:left"><a class="btnLook" href="%s&fieldname=%s" width="900" lookupGroup="org">选择</a></span>
            </div>
            '''%(flatatt(final_attrs), name, _value, m_url, name)
        return mark_safe(ret_str)