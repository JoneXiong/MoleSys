# coding = utf-8
from mole import route
from mole import request
from mole import redirect

@route('/login')
def login():
    from mosys.mole_api import JTemplate
    return JTemplate("login")

@route('/logout')
def logout():
    from mosys.mole_api import get_current_session
    session = get_current_session()
    del session['username']
    redirect('/login')

@route('/login_check',method='POST')
def login_check():
    from mosys.mole_api import request, get_current_session
    uname =  request.POST.get("username")
    pwd =  request.POST.get("password")
    ret = " "
    if uname == "admin" and pwd =="admin" :
        session = get_current_session()
        session['username'] = 'admin'
        ret = "OK"
    return "%s"%ret