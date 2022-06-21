from ursina import *
from setUpSprites import *
import json

f = open("player1.json")
player1Deck = json.load(f)
#print(player1Deck[str(1)])
f.close()

f = open("player2.json")
player2Deck = json.load(f)
#print(player1Deck[str(1)])
f.close()


def cardsUpdate():
    pass
    
def cardsInput(key):
    pass
