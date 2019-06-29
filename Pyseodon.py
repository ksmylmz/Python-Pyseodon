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
    _controller = controller()

