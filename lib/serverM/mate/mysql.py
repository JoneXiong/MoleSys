#-*- coding: utf-8 -*-
#
# Copyright (c) 2012, VPSMate development team
# All rights reserved.
#
# VPSMate is distributed under the terms of the (new) BSD License.
# The full license can be found in 'LICENSE.txt'.

"""Package for mysql operations.
"""

import os

if __name__ == '__main__':
    import sys
    root_path = os.path.abspath(os.path.dirname(__file__)+'../')
    sys.path.append(root_path)

import pexpect
import shlex
import re


def updatepwd(pwd, oldpwd):
    """Update password of root.
    """
    try:
        cmd = shlex.split('mysqladmin -uroot password "%s" -p' % pwd)
    except:
        return False

    child = pexpect.spawn(cmd[0], cmd[1:])
    i = child.expect(['Enter password', pexpect.EOF])
    if i == 1:
        if child.isalive(): child.wait()
        return False

    child.sendline(oldpwd)
    i = child.expect(['error', pexpect.EOF])
    if child.isalive(): return child.wait() == 0
    return i != 0

def _mysql(pwd):
    """Open a mysql client and auth login.
    """
    cmd = shlex.split('mysql -uroot -p')
    child = pexpect.spawn(cmd[0], cmd[1:])
    if not _auth(child, pwd): return False
    return child

def _auth(child, pwd):
    """Auth a mysql client login.
    """
    i = child.expect(['Enter password', pexpect.EOF])
    if i == 1:
        if child.isalive(): child.wait()
        return False

    child.sendline(pwd)
    i = child.expect(['mysql>', pexpect.EOF])
    if i == 1:
        if child.isalive(): child.wait()
        return False
    return True

def _exit(child):
    """Exit a mysql client.
    """
    child.sendline('exit')
    if child.isalive(): child.wait()

def _sql(child, sql, returnoutput=False):
    """Execute SQL statement in interactive mode.
    """
    child.sendline(sql)
    i = child.expect(['ERROR', 'mysql>', pexpect.EOF])
    if i == 0 or i == 3:
        _exit(child)
        return False
    if returnoutput:
        return child.before
    else:
        return True
    
def fupdatepwd(pwd):
    """Force update password of root.

    MySQL server should first enter rescue mode.
    """
    child = pexpect.spawn('mysql')
    i = child.expect(['mysql>', pexpect.EOF])
    if i == 1:
        if child.isalive(): child.wait()
        return False
    if not _sql(child, 'UPDATE mysql.user SET Password=PASSWORD("%s") WHERE User="root";' % re.escape(pwd)): return False
    if not _sql(child, 'FLUSH PRIVILEGES;'): return False
    if not _sql(child, 'exit;'): return False
    return True

def show_databases(pwd):
    """Show database list.
    """
    child = _mysql(pwd)
    if not child: return False

    output = _sql(child, 'SHOW DATABASES;', True)
    if not output: return False
    _exit(child)

    lines = output.split('\n')[4:]
    dbs = [line.strip().strip('|').strip() for line in lines if line.startswith('|')]
    dbs = [db for db in dbs if db not in ('information_schema', 'performance_schema', 'mysql')]
    return dbs

def create_database(pwd, name):
    """Create a new database.
    """
    child = _mysql(pwd)
    if not child: return False
    if not _sql(child, 'CREATE DATABASE %s;' % re.escape(name)): return False
    _exit(child)
    return True

def drop_database(pwd, name):
    """Drop a database.
    """
    child = _mysql(pwd)
    if not child: return False
    if not _sql(child, 'DROP DATABASE %s;' % re.escape(name)): return False
    _exit(child)
    return True


if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    
    #pp.pprint(show_databases('admin'))
    pp.pprint(create_database('admin', 'abcd'))
    pp.pprint(drop_database('admin', 'abcd'))