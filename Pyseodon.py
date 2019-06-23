from controller import controller
import requests
import urllib.request
from bs4 import BeautifulSoup
import sys



def catch_exceptions(t, val, tb):
    QtWidgets.QMessageBox.critical(None,
                                   "An exception was raised",
                                   "Exception type: {}".format(t))
    old_hook(t, val, tb)

old_hook = sys.excepthook
sys.excepthook = catch_exceptions

    
if __name__ == '__main__':
    

    
    #headers     
    headers = { "header_name": "headers_value" }
    params = {  "param_name": "param_value" }
    path = ""
   # path = "https://www.beethoven.com.tr/"
    
    #getrequest     
    #_request = requests.get(path, params=params, headers=headers)



    _controller = controller()
    #_controller.routes()



"""
#path ="https://www.w3schools.com/python/python_dictionaries.asp"
#path ="https://www.lensoptik.com.tr/"
#path = "http://www.ufoweb.net"
#path = "https://www.garantibbva.com.tr/tr"
path = "https://www.ddfs.com/"
#path = "https://wp.pts.net/"
#Content-Encoding"""