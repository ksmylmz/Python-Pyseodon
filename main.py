import requests
from controller import controller
import urllib.request
import random
import time
from _tracemalloc import start
import re



#path ="https://www.w3schools.com/python/python_dictionaries.asp"
#path ="https://www.lensoptik.com.tr/"
#path = "http://www.ufoweb.net"
#path = "https://www.garantibbva.com.tr/tr"
path = "https://www.ddfs.com/"
#path = "https://wp.pts.net/"
#Content-Encoding
headers = {  # headers dict to send in request
  "header_name": "headers_value",
 }

params = {  # params to be encoded in the url
  "param_name": "param_value",
}


r = requests.get(path, params=params, headers=headers)



c = controller(r.content)

#c.saveLinkList()

#metaDescription = c.betweenContent("meta","name","description",70,320)
#print(metaDescription)
#metakey = c.betweenContent("meta","name","keywords",0,300)
#print(metakey)



"""
metTitle = c.betweenContent("meta","name","title",10,70)
if metTitle=="meta->title :this tag not found!":
    metTitle = c.betweenText("title",10,70)
print(metTitle)"""


"""for i in range(1,7):
    h= c.countAndListbyTagName("h"+str(i))
    print("H"+str(i)+" : "+str(h["length"])+" tags")
    
    for items in h["taglist"]:
        print(items,"\n")"""
        
 
"""img without alt 
       
altless = c.checkImgAlt()
for img in altless:
    print(img)
"""
"""" 
images = c.getAllImg()
for img in images:
    if img.get("src") is not None:
        #print(img.get("src"))
        #urllib.request.urlretrieve(img.get("src"),"images/image"+str(random.randint(1,101))+".png")
        c.checkDimType(img)
        if c.checkDimType(img)!=0:
            print(c.checkDimType(img))"""


        
"""brokenlist = c.checkBrokenlinks(path)
print(brokenlist)"""

"""unfrendlylist = c.checkFrendlyUrl()
print(unfrendlylist)"""


"""
if c.checkAnalytic() : 
    print("Analtics tag implemented")
else:
    print("Analytics tag not found")"""


#print(c.checkResponsive())
   
"""
if c.checkResponsive() : 
    print("Analtics tag implemented")
else:
    print("Analytics tag not found")"""

"""
if c.checkFlash():
    print("Flash tag dedected")
else:
    print("flash tag not found")
    
if c.checkFlash():
    print("iframe dedected")
else:
    print("iframe tag not found")
    
 
if c.checkfavicon():
    print("there is favicon")
else:
    print("favicon tag not found")"""
"""    
startTime = time.time()
print(c.checkSizes())
stopTime = time.time()
measureTime =stopTime-startTime
#print(time.ctime(startTime),time.ctime(stopTime))
print("pageLoad Time :"+str(measureTime))
"""


"""
try:
    print(r.headers["Content-Encoding"])
except KeyError:
    print("There is any compression configration at your server")
    
"""

#r2  = requests.get("http://ufoweb.net/assets/esnafy/lib/jquery/dist/jquery.js");
#r2  = requests.get("https://www.ddfs.com/frontend/skin/ddfs/stylesheet/font-awesome-4.7.0/css/font-awesome.min.css");
#_content = str(r2.content)


""""
for i in  c.checkSourcesForMinify("script","src",path):
    print(i)
print("------------------------------------")
for i in  c.checkSourcesForMinify("link","href",path):
    print(i)
 """
 
"""
title 10~70 +
meta description 70 and 320 characters+
count h tags - list g tag text+
check image alt+
broken link+
frendly url+
robot.txt-
sitemap-

check analytics tag+
check responsive+ 
flash check+
check iframe+
check favicon+

count load page time+

check images size, check css size, check js size,check html size,check total size+


js errors-

gzip compesion+

check unsized images-

js css mifycation+


"""