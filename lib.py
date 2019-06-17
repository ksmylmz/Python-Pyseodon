from bs4 import BeautifulSoup


class lib:
    content  = None
    
    def __init__(self,content):

        self.content = BeautifulSoup(content,"html.parser")


    def getAllTags(self,tagname):
        tags = self.content.find_all("img","html.parser")
        return tags


    def getbyProp(self,tag,prop,val):
        tags = self.content.find_all(tag,{prop:val},"html.parser")
        return tags
    
    def getbyTagname(self,_tag):
        tag = self.content.find(_tag)
        return tag
    
    def getTagsByName(self,_tag):
        tags = self.content.find_all(_tag)
        return tags


    
    def checkResult(self,result,tagname,val):
        if len(result)==0:
            return tagname+"->"+val+" :this tag not found!"
        elif len(result)>1:
            return tagname+"->"+val+" :More than one, same tag! "
        else:
            return 0

    def getNodeText (self,node,tag):
        nodeTag  = BeautifulSoup(node)
        print(nodeTag.find(tag).text)
        return "adas"
    
    def checkDimType(self,tag):
        print(tag)
        """
        if tag["style"] is not None:
            return "style"
        elif tag["class"] is not None:
            return "class"
        elif tag["class"] is not None:
            return "width"
        else:
            return 0"""
            

    
              



        
