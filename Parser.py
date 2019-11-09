import requests
import re
from Item import Item

class Parser:

    def __init__(self,url):
        self.url = url
        self.content = ""
        self.tokens = []
        self.lots = []

        try:
            self.content = requests.get(self.url).text.strip().replace("\n","").replace("\t","").replace("\r","")
        except Exception:
            print("The url supplied was invalid.")
            exit(-1)
        self.tokenise()

    def tokenise(self):
        
        #regex = """((?P<tag>[<{1}][^<>]+[>{1}]{1})((\s|\S){0,}(?P=tag)){0,})+"""
        #regex = """([<{1}][^<>]+(?P<tag>[>{1}])((\s|\S){0,}[//]{1}(?P=tag)){0,})+"""
        #regex = """(<{1})(?(1)(?P<tag>[\S|\s]+)|)"""
        #regex = """(<{1}(?P<main>tr).{0,}>{1}.{0,}<{1}/(?P=main)[.]{0,}>{1})"""
 
        tokens = re.findall(r"""(?P<tag>tr)(?P<data>.*?)(?P<endTag>\/(?P=tag))""",self.content)
        
        arrToken = []
        for token in tokens:
            if(self.tokenIsValid(token)==True):
                t = Item(str(token).strip().replace("\n","").replace("\t","").replace("\r",""))
                arrToken.append(t)            
        
        self.tokens = arrToken                              

    def tokenIsValid(self,token):
        if re.search("""<(?P<tag>h5)>(?P<data>.*?)(?P<endTag>/(?P=tag)|img)""","".join(token)):
            return True
        return False

    def getContent(self):
        return self.content

    def getTokens(self):
        return self.tokens

    def search(self,string):
        validTokens = []
        for token in self.tokens:
            
            if re.search(string,token.lotTitle):
                validTokens.append(token)
        return validTokens

            
    def __doc__(self):
            
        docString = """A Parser for the John Pye & Sons auction site.
            Designed to make searching more customisable for Items on John Pye
        """
        return docString