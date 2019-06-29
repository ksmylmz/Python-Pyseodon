from template import _mainView
from model import model
import requests
import urllib.request
import random
import time
from _operator import length_hint
from logging import _startTime
from threading import Thread
from asyncio.tasks import sleep



class controller():
    
    model=None
    template = None
    path = ""
    r = None
    

    
    def __init__(self):
        self.template= _mainView()
        self.template.btnsearchBox.clicked.connect(lambda:self.initRequest())
        
        self.template.showWindow()
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
        result=""
        message=""
        for i in range(1,8):        
            h= self.model.countAndListbyTagName("h"+str(i))
            if h != "":
                message+="H"+str(i)+" : "+str(h["length"])+" tags<br>"
                for items in h["taglist"]:
                    #print(items)
                    result+=str(items)+"\n"
                result+="\n\n\n"
        self.template.setResult(message)        
        self.template.appendConsole(result)       
    
    
    def chkImgAlt(self):
        altless = self.model.checkImgAlt()
        message=" there is "+str(len(altless))+" img tag has no alt attribute<br/>"
        result=""
        for img in altless:
            try:
                result+=img["src"]+"\n"
            except KeyError:
                continue
        self.template.setResult(message)
        self.template.appendConsole(result)
        
    
    def thCheckBroken(self):
        brokenlist = self.model.checkBrokenlinks(self.path)
        result=" there is "+str(len(brokenlist))+"  broken links<br/>"
        for b in brokenlist:
            result+=b+"\n"
        self.template.setResult(result)

    
    def chkBroken(self):
        self.template.setResult("loading...")
        _thread  =Thread(target = self.thCheckBroken)
        _thread.start()
        
        

        
            
    def unfrendly(self):
        unfrendlylist = self.model.checkFrendlyUrl()
        message=" there is "+str(len(unfrendlylist))+" unfrendly urls"
        result = ""
        for b in unfrendlylist:
            result+=b+"\n"
        self.template.setResult(message)
        self.template.appendConsole(result)
        
            
            
    def chkAnalytics(self):
        chk = self.model.checkAnalytic()
        if chk["result"] : 
            self.template.setResult("Analtics tag implemented")
            self.template.appendConsole(chk["tag"])
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
        startTime = time.process_time()
        sizes  = self.model.checkSizes()
        stopTime = time.time()
        measureTime =time.process_time()-startTime
        #print(time.ctime(startTime),time.ctime(stopTime))
        load =  str(measureTime)
        result="";
        result+="Image size : "+str(sizes["img"])+" MB <br>"
        result+="Css size : "+str(sizes["css"])+" MB <br>"
        result+="Javascript size : "+str(sizes["script"])+" MB <br>"
        result+="Html Code Size : "+str(sizes["html"])+" MB <br>"
        result+="Total size : "+str(sizes["totalsize"])+" MB"+self.model.rateRes(0,4," MB ",sizes["totalsize"])+" <br>"
        result+="<hr>"
        result+="Page Load time : "+load+" seconds"+self.model.rateRes(4,8," seconds",measureTime)
        self.template.setResult(result)
        self.template.appendConsole(sizes["taglog"])
        
    def th_chkPerformance(self):
        self.template.setResult("loading...")
        th =Thread(target=self.chkPerformance)
        th.start()
        
    def checkGzip(self):
        try:
            result =  self.model._request.headers["Content-Encoding"]+" is active"
            self.template.setResult(result)
        except KeyError:
            self.template.setResult("There is no any compression configration at your server")
        
    
    def thChkUmS(self):
        result  = " Unminify Scripts:<br>"
        for i in  self.model.checkSourcesForMinify("script","src",self.path):
            result+="<a href='"+i+"' >"+i+"</a><br>"

        self.template.setResult(result)
    
    def chkScriptUnMinify(self):
        self.template.setResult("loading...")
        th = Thread(target=self.thChkUmS)
        th.start()
        
    def chkInlineStyle(self):
        result  = self.model.checkInline()
        self.template.setResult(str(result["tagcount"])+" tag dedected, has the inline css! ")
        self.template.appendConsole(result["tagStrList"])
        
        
        
    def thChkUmCss(self):
        result  = " Unminify Css:<br>"
        for i in  self.model.checkSourcesForMinify("script","src",self.path):
            result+="<a href='"+i+"' >"+i+"</a><br>"

        self.template.setResult(result)        
        
            
    def chkCssUnMinify(self):
        self.template.setResult("loading...")
        th = Thread(target=self.thChkUmCss)
        th.start()
        
        
    def clearConsole(self):
        self.template.console.setPlainText("")
        self.template.setResult("")
        
           
                    
                



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
        self.template.btnPerformance.clicked.connect(lambda:self.th_chkPerformance())
        self.template.checkGzip.clicked.connect(lambda:self.checkGzip())
        self.template.btnScriptUnMinify.clicked.connect(lambda:self.chkScriptUnMinify())
        self.template.btnCssUnMinify.clicked.connect(lambda:self.chkCssUnMinify())
        self.template.btninlineCss.clicked.connect(lambda:self.chkInlineStyle())
        self.template.clearConsole.clicked.connect(lambda:self.clearConsole())

        
        
   
    def initRequest(self):
        headers = { "header_name": "headers_value" }
        params = {  "param_name": "param_value" }
        path = self.template.searchBox.text()
        
        if path!="":
            try:
                _request = requests.get(path, params=params, headers=headers)
                self.model = model(_request)
                self.routes()
                self.template.setResult("Connection Success")
            except requests.exceptions.RequestException:
                self.template.setResult("Unsuccesful request. Please check your Url!")
        else:
            self.template.setResult("Missing Url for scan!")

      