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
        
        return  "LOT NO: " + str(self.lotNo) + ", '"+self.lotTitle + "', PRICE £" + str(self.price) + ", " + self.timeRemaining + (" remaining" if self.timeRemaining!="Ended" else "")

    def parseData(self):
        tag= "h5"
        
        regex = """<(?P<tag>{})>(?P<data>.*?)(?P<endTag>/(?P=tag)|img)""".format(tag)
        dataPoints = re.findall(regex,self.data)
        dataStrings = []
        for i in range(0,len(dataPoints)):
            dataStrings.append("".join(dataPoints[i]).replace(tag+">","").replace("</"+tag,"").replace(tag,"").replace("<img",""))
        try:
            self.lotNo = int(dataStrings[0])
            self.lotTitle = dataStrings[1]
            self.price = float(dataStrings[2][7:])
            self.timeRemaining = dataStrings[3]            
        except Exception: #If the data is in the wrong format
            return False
