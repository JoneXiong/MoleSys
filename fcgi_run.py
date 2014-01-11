# -*- coding: utf-8 -*-
import sys

from server import app,run
       
if __name__  == "__main__":
    try:
        ipaddress=sys.argv[1]
        port=int(sys.argv[2])
    except:
        ipaddress = '0.0.0.0'
        port = 81313
    run(app=app,server='flup',host=ipaddress, port=port)
