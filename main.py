import requests
import re

class Item:
    def __init__(self,data):
        self.data = data
        self.lot = ""
        self.lotNo = ""
        self.price = ""
        self.lotTitle = ""
        self.timeRemaining = ""
        self.parseData()

    def __str__(self):
        
        return "LOT: " + self.lot + " LOT NO: " + self.lotNo + ", "+self.lotTitle + ", PRICE £" + self.price + " at " + self.timeRemaining + " remaining"

    def parseData(self):
        tag= "h5"
        regex = """(?P<tag>{})(?P<data>.*?)(?P<endTag>/(?P=tag))""".format(tag)
        dataPoints = re.findall(regex,self.data)
        dataStrings = []
        for i in range(0,len(dataPoints)-1):
            dataStrings.append("".join(dataPoints[i]).replace(tag+">","").replace("</"+tag,""))
        try:
            self.lotNo = dataStrings[0]
            self.lotTitle = dataStrings[1]
            self.price = dataStrings[2]
            self.timeRemaining = dataStrings[3]
        except Exception:
            print("The token was invalid")
            return

class Lot:
    def __init__(self):
        self.items = []

    def addItem(self,item):
        self.items.append(item)
        
    def lot(self):
        for item in self.items:
            print(item)

class Parser:
    def __init__(self,url):
        self.url = url
        self.content = ""
        self.tokens = []

        try:
            self.content = requests.get(self.url).text.strip()
            #print(self.content)
            

        except Exception:
            print("The url supplied was invalid.")
            exit(-1)
        self.tokenise()
        self.lots = []


    def tokenIsValid(self,token):
        print(token)
        for bit in token:
            if(bit==""):
                return False
        return True

    def tokenise(self):
        
        #regex = """((?P<tag>[<{1}][^<>]+[>{1}]{1})((\s|\S){0,}(?P=tag)){0,})+"""
        #regex = """([<{1}][^<>]+(?P<tag>[>{1}])((\s|\S){0,}[//]{1}(?P=tag)){0,})+"""
        regex = """(<{1})(?(1)(?P<tag>[\S|\s]+)|)"""
        #regex = """(<{1}(?P<main>tr).{0,}>{1}.{0,}<{1}/(?P=main)[.]{0,}>{1})"""

        regex = r"""(?P<tag>tr)(?P<data>.*?)(?P<endTag>/(?P=tag))"""
        
        strippedContent = self.content.strip().replace("\n","").replace("\t","").replace("\r","")
    
        tokens = re.findall(r"""(?P<tag>tr)(?P<data>.*?)(?P<endTag>/(?P=tag))""",strippedContent)
        print(len(tokens))
        arrToken = []
        for token in tokens:
            if(self.tokenIsValid(token)):
                t = Item(str(token).strip().replace("\n","").replace("\t","").replace("\r",""))
                arrToken.append(t)            
        
        self.tokens = arrToken                              


    def getContent(self):
        return self.content
    def getTokens(self):
        return self.tokens
    def __doc__(self):
        
        docString = """A Parser for the John Pye & Sons auction site.
            Designed to make searching more customisable for Items on John Pye
        """
        return docString

t = Parser("https://www.johnpyeauctions.co.uk/lot_list.asp?saleid=7426&siteid=1")

#print(t.getContent())

for token in t.tokens:
    print(token,"\n")
    
#print(len(t.tokens))
#print(t.tokens[0])