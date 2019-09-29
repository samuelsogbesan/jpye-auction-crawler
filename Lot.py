class Lot:
    def __init__(self):
        self.items = []

    def addItem(self,item):
        self.items.append(item)
        
    def lot(self):
        string = ""
        for item in self.items:
            string += item + " "