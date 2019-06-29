from lib import lib

import requests as rq
from symbol import except_clause
from select import select
from click.termui import style





class model(lib):
    taglog = None
    
    def __init__(self,_request):
        lib.__init__(self,_request)

       

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
         if tags is not None:
             result  = {"length":len(tags),"taglist":tags}
         else:
            result=""
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
            try:               
                if "javascript" in link["href"]: continue
                if link["href"][0]=="#": continue
                if "mailto:" in link["href"]: continue
                path =link["href"]  if "http:" in link["href"] or "https:" in link["href"]  else baseurl+"/"+link["href"]
                try:
                    response = rq.get(path)
                except rq.exceptions.RequestException:
                    broken.append(path)
            except KeyError:
                continue
                             
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
                    return {"result":1,"tag" :fcontent}
                else:
                    continue
            except KeyError:
                continue
        return  {"result":0}    
    
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
                            
                    if tagname=="link" and "css" not in src: 
                        continue
                    if tagname=="style":
                        filesize+= len(str(tag))
                        continue
                    
                    self.taglog += "\n" + str(tag) 
                    try:
                        filesize+=len(rq.get(tag[prop]).content)
                    except rq.exceptions.RequestException:
                        continue
                    
                except KeyError:
                   self.taglog += "\n" + str(tag)
                   filesize+=len(str(tag))
                   
        return filesize/1024/1024
    
    def checkSizes(self):
        
        self.taglog=""
        
        img = round(self.checkSize("img","src"),2),
        style = round(self.checkSize("style","type"))
        script = self.checkSize("script","src")
        css = round(self.checkSize("link","href"),2)
        html = round(len(str(self.content))/1024/1024,2)
        print(img,style,script,css,html)
        totalsize = round(img[0]+style+script+css+html,2)
        sizes = {"img":img,"css":style+css,"script":script,"html":html,"totalsize":totalsize,"taglog":self.taglog}
        return sizes;
    
    def checkSourcesForMinify(self,tagname,prop,baseurl):
        tags= self.getTagsByName(tagname)
        unminified=[]    
        if len(tags)>0:
            for tag in tags:
                try:

                    src =tag[prop]  if "http:" in tag[prop] or "https:" in tag[prop]  else baseurl+"/"+tag[prop]
                    if tagname=="link" and "css" not in src: continue 
                     
                    try:
                        _content = str(rq.get(src).content)
                    except rq.exceptions.RequestException:
                        continue
                    
                    if len(_content.split("/r"))>1 or len(_content.split("/n"))>1:
                        unminified.append(src)    
                except KeyError:
                   continue
        return unminified
    
    
    def checkInline(self):
        tagsList = ['a', 'abbr', 'acronym', 'address', 'applet', 'area', 'article', 'aside', 'audio', 'b', 'base', 'basefont', 'bdi', 'bdo', 'big', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'center', 'cite', 'code', 'col', 'colgroup', 'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 'dir', 'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'font', 'footer', 'form', 'frame', 'frameset', 'h1','h2','h3','h4','h5','h6', 'head', 'header', 'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li', 'link', 'main', 'map', 'mark', 'meta', 'meter', 'nav', 'noframes', 'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param', 'picture', 'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source', 'span', 'strike', 'strong', 'style', 'sub', 'summary', 'sup', 'svg', 'table', 'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'track', 'tt', 'u', 'ul', 'var', 'video', 'wbr']
        tagStrList="";
        tagCount = 0
        for i in tagsList:
            tags= self.getTagsByName(i)
            
            for t in tags:
                if self.issetKey(t,"style"):
                    tagStrList+=str(t)+"<\n>"
                    tagCount+=1
                else:
                    continue
        
        
        return {"tagcount":tagCount,"tagStrList":tagStrList}
                
            
        
        
                      
        

                  
        
           

  

    





