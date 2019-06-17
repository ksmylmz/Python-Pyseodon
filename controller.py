import requests
import urllib.request
import random
import time
from _operator import length_hint






class controller():
    
    model=None
    template = None
    path = ""
    r = None
    
    def __init__(self,model,template,path):
        self.model=model
        self.template=template
        self.path= path
        
        
        

        
    def checkMeta(self):

        metaDescription = self.model.betweenContent("meta","name","description",70,320)
        metakey = self.model.betweenContent("meta","name","keywords",0,300)
        metaTitle = self.model.betweenContent("meta","name","title",10,70)
        
        if metaTitle=="meta->title :this tag not found!":
            metaTitle = self.model.betweenText("title",10,70)
            
        _result = metaDescription+"<br/>"+metakey+"<br/>"+metaTitle  
             
        self.template.setResult(_result)
    


    
    
    def checkHtags(self):
        h= self.model.countAndListbyTagName("h"+str(i))
        print("H"+str(i)+" : "+str(h["length"])+" tags")
        result=""
        for items in h["taglist"]:
            result+=items+"\n"
        self.template.setResult(result)
    
    
    def chkImgAlt(self):
        altless = self.model.checkImgAlt()
        result=" there is "+len(altless)+" img tag without alt properties\n"
        for img in altless:
            result+=img+"\n"
        self.template.setResult(result)
        
    
    def chkBroken(self):
        brokenlist = self.model.checkBrokenlinks(path)
        result=" there is "+len(brokenlist)+" img tag without alt properties\n"
        for b in brokenlist:
            result+=b+"\n"
    
    def unfrendly(self):
        unfrendlylist = self.model.checkFrendlyUrl()
        result=" there is "+len(unfrendlylist)+" img tag without alt properties\n"
        for b in unfrendlylist:
            result+=b+"\n"
        self.template.setResult(result)
        
            
            
    def chkAnalytics(self):
        if self.model.checkAnalytic() : 
            self.template.setResult("Analtics tag implemented")
        else:
            self.template.setResult("Analytics tag not found")
        
    def chkMobil(self):
        if self.model.checkResponsive():
            self.template.setResult("Your web site is responsive ")
        else:
            self.template.setResult("Your web site is unresponsive")
        
        
    def chkFlash(self):
        if self.model.checkFlash():
            self.template.setResult("Flash tag dedected")
        else:
            self.template.setResult("flash tag not found")
    
    def checkiframe(self):
        if self.model.checkFlash():
            self.template.setResult("iframe dedected")
        else:
            self.template.setResult("iframe tag not found")
        
    def chkFavico(self):
        if self.model.checkfavicon():
            self.template.setResult("you have a  favicon")
        else:
            self.template.setResult("favicon tag not found")
        
    def chkPerformance(self):
        startTime = time.time()
        sizes  = self.model.checkSizes()
        stopTime = time.time()
        measureTime =stopTime-startTime
        #print(time.ctime(startTime),time.ctime(stopTime))
        load =  "pageLoad Time :"+str(measureTime)
        # sizes = {"img":img,"css":style+css,"script":script,"html":html}
        result="";
        result+="Image size : "+sizes["img"]+" MB \n"
        result+="Css size : "+sizes["css"]+" MB \n"
        result+="Javascript size : "+sizes["script"]+" MB \n"
        result+="Html Code Size : "+sizes["html"]+" MB  \n"
        result+="Total size : "+sizes["img"]+sizes["css"]+sizes["script"]+sizes["html"]+" MB \n"
        result+="<hr>"
        result+="Page Load time : "+load+"seconds"
        self.template.setResult(result)
        
    def checkGzip(self):
        try:
            result =  self.model._request.headers["Content-Encoding"]+" is active"
            self.template.setResult(result)
        except KeyError:
            self.template.setResult("There is no any compression configration at your server")
        
    def chkScriptUnMinify(self):
        result  = " Unminify Scripts:\n"
        for i in  self.model.checkSourcesForMinify("script","src",path):
            result+=i+" \n"
        self.template.setResult(result)
        
    def chkCssUnMinify(self):
        result  = " Unminify Css:\n"
        for i in  self.model.checkSourcesForMinify("script","src",path):
            result+=i+" \n"
        self.template.setResult(result)
            
            
                    
                



    def routes(self):
        #routes
       # btnMetaTags,btnHtags,btnImgAlt,btnBroken,btnUnfrendly,btnAnalytics,btnMobil,cgkFlash,
       # btnIframe,btnFavico,btnPerformance,checkGzip,btnScriptUnMinify,btnCssUnMinify
        self.template.btnMetaTags.clicked.connect(lambda:self.checkMeta())
        self.template.btnHtags.clicked.connect(lambda:self.checkHtags())
        self.template.btnImgAlt.clicked.connect(lambda:self.chkImgAlt())
        self.template.btnBroken.clicked.connect(lambda:self.chkBroken())
        self.template.btnUnfrendly.clicked.connect(lambda:self.unfrendly())
        self.template.btnAnalytics.clicked.connect(lambda:self.chkAnalytics())
        self.template.btnMobil.clicked.connect(lambda:self.chkMobil())
        self.template.cgkFlash.clicked.connect(lambda:self.chkFlash())
        self.template.btnIframe.clicked.connect(lambda:self.checkiframe())
        self.template.btnFavico.clicked.connect(lambda:self.chkFavico())
        self.template.btnPerformance.clicked.connect(lambda:self.chkPerformance())
        self.template.checkGzip.clicked.connect(lambda:self.checkGzip())
        self.template.btnScriptUnMinify.clicked.connect(lambda:self.chkScriptUnMinify()())
        self.template.btnCssUnMinify.clicked.connect(lambda:self.chkCssUnMinify())

        
        
        
        
        
        

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