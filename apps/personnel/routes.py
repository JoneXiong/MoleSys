# coding = utf-8
from mole import route
from mole import request
from mole import response
from mole import redirect
from mole.template import jinja2_template

@route('/admin/personnel',name='homepage')
def homepage():
    from mocrud.admin import admin
    return jinja2_template('admin/model_grup.html',
#            model_admins=self.get_model_admins(),
        panels=admin.get_panels(),
        model_grup = 'personnel',
        model_admins=admin.get_grup_admins('personnel'),
        **admin.template_helper.get_model_admins()
    )