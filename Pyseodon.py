from template import _mainView
from model import model
from controller import controller
import requests
import urllib.request
from bs4 import BeautifulSoup

    
if __name__ == '__main__':
    
    _template = _mainView()
    
    #headers     
    headers = { "header_name": "headers_value" }
    params = {  "param_name": "param_value" }
    path = "https://www.lensoptik.com.tr/"
    
    #getrequest     
    _request = requests.get(path, params=params, headers=headers)


    #initialize Model    
    _model  =model(_request.content)

    _controller = controller(_model,_template,path)
    _controller.routes()
    _template.showWindow()


"""
#path ="https://www.w3schools.com/python/python_dictionaries.asp"
#path ="https://www.lensoptik.com.tr/"
#path = "http://www.ufoweb.net"
#path = "https://www.garantibbva.com.tr/tr"
path = "https://www.ddfs.com/"
#path = "https://wp.pts.net/"
#Content-Encoding"""