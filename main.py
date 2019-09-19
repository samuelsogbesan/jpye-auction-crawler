import requests
from Token import Token
import re

class Item:
    def __init__(self,lot,lotNo,lotTitle,price,timeRemaining):
        self.lot = lot
        self.lotNo = lotNo
        self.price = 0
        self.lotTitle = lotTitle
        self.timeRemaining = timeRemaining

    def __str__(self):
        print(self.lot, " ", self.lotNo,": ",self.lotTitle,", £"+self.price," at ",self.timeRemaining," remaining")
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
        try:
            self.content = requests.get(self.url).text
            self.tokens = self.tokenise()
        except Exception:
            print("The url supplied was invalid.")
            exit(-1)

        self.lots = []

    def tokenise(self):
        tokens = []

        #use regex to break it down into list of <tag>DATA</tag> tokens or <tag> (self closing) tags
        #assumes no stand-alone text in html
        
        return tokens

    def getContent(self):
        return self.content
    
    def __doc__(self):
        
        docString = """A Parser for the John Pye & Sons auction site.
            Designed to make searching more customisable for Items on John Pye
        """
        return docString


t = Parser("https://www.johnpyeauctions.co.uk/lot_list.asp?saleid=7512&siteid=2&h=0&pageno=2")

print(t.getContent())

