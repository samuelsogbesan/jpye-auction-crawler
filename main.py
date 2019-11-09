import requests
import re
from Item import Item
from Lot import Lot
from Parser import Parser

def main():
    t = Parser("https://www.johnpyeauctions.co.uk/lot_list.asp?saleid=7750&siteid=1")

    for token in t.tokens:
        print(token,"\n")
        
    for token in t.search("avermedia"):
        print(str(token))
main()