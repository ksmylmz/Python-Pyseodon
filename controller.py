from helper import Helper

import requests as rq
from symbol import except_clause
from select import select
from macpath import split



class controller(Helper):
    def __init__(self,content):
        Helper.__init__(self,content)



    def saveLinkList(self):     
        links  = self.getAllTags("a")
        f =open("url.txt","a")
        for link in links:
            line = str(link.get("href"))+"\n"#+link.text()+"
            print(line)
            f.write(line)
            
        f.close()

    def betweenContent(self,tagname,prop,val,min,max):
        tag = self.getbyProp(tagname,prop,val)
        chck = self.checkResult(tag,tagname,val)
        if chck!=0:
            return chck
        else:
            if len(tag[0]["content"])<min:
                return tagname+"->"+val+" : character less than "+str(min)+" X "
            elif len(tag[0]["content"])>max:
                return tagname+"->"+val+" : character more than "+str(max)+" X "
            else:
                return tagname+"->"+val+" : character between "+str(min)+"-"+str(max)+" OK"
            
            
          
    def betweenText(self,tagname,min,max):
        tag = self.getbyTagname(tagname)
        if len(tag.text)<min:
            return tagname+"-> : character less than "+str(min)+" X "
        elif len(tag.text)>max:
            return tagname+"-> : character more than "+str(max)+" X "
        else:
            return tagname+"-> : character between "+str(min)+"-"+str(max)+" OK"
    
    
    def countAndListbyTagName(self,tag):
         tags = self.getTagsByName(tag)
         result  = {"length":len(tags),"taglist":tags}
         return result
     
    def checkImgAlt(self):
        imgs  = self.getTagsByName("img")
        altless  = []
        for img in imgs:
            if img.get("alt") is None:
                altless.append(img)
        return altless
    
    
    def getAllImg(self):
        imgs  = self.getTagsByName("img")
        return imgs
    
    def checkBrokenlinks(self,baseurl):
        broken=[]
        links = self.getTagsByName("a")
        for link in links:
            if "javascript" in link["href"]: continue
            if link["href"][0]=="#": continue
            if "mailto:" in link["href"]: continue
            path =link["href"]  if "http:" in link["href"] or "https:" in link["href"]  else baseurl+"/"+link["href"]
            response = rq.get(path)
            if response.status_code!=200: 
                broken.append(path)             
        return broken
    
    def checkFrendlyUrl(self):
        unfrendly=[]
        links = self.getTagsByName("a")
        for link in links:
            try:
                if "javascript" in link["href"]: continue
                if link["href"][0]=="#": continue
                if "mailto:" in link["href"]: continue
                if "asp" in  link["href"] or "php" in  link["href"] or "html" in  link["href"] or "?" in  link["href"]:
                    unfrendly.append(link["href"])

            except KeyError:
                continue
              
        return unfrendly
    
    def checkAnalytic(self):
        scripts = self.getTagsByName("script")
        for script in scripts:
            try:
                fcontent =str(script)
                if "analytics" in fcontent:
                    return 1
                else:
                    continue
            except KeyError:
                continue
        return 0    
    
    def checkResponsive(self):
        metaTag = self.getbyProp("meta","name","viewport")
        if len(metaTag)>0:
            try:
                if "width=device-width" in metaTag[0]["content"]:   
                    return 1
                else:
                    return 0 
            except KeyError:
                return 0
        else:
             return 0       
    
    def checkFlash(self):
        flashtag = self.getTagsByName("embed") 
        if len(flashtag)>0:
            return 1
        else:
            return 0
        
    def checkiframe(self):
        iframe = self.getTagsByName("iframe") 
        if len(iframe)>0:
            return 1
        else:
            return 0
        
    def checkfavicon(self):
        favicon = self.getbyProp("link","rel","icon")
        if len(favicon)>0:
            return 1                
        else:
             return 0 
         
    def checkSize(self,tagname,prop):
        tags= self.getTagsByName(tagname)
        filesize=0
        
        if len(tags)>0:
            for tag in tags:
                try:
                    src= tag[prop]
                            
                    if tagname=="link" and "css" not in src: continue  
                    filesize+=len(rq.get(tag[prop]).content)
                except KeyError:
                   filesize+=len(str(tag))
                   
        return filesize/1024
    
    def checkSizes(self):
        img = self.checkSize("img","src")
        style = self.checkSize("style","type")
        script = self.checkSize("script","src")
        css = self.checkSize("link","href")
        html = len(str(self.content))/1024
        sizes = {"img":img,"css":style+css,"script":script,"html":html}
        return sizes;
      
                      
        

                  
        
           

  

    





