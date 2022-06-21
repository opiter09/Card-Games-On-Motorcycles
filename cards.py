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

p1Life = 15
p2Life = 15

def cardsUpdate():
    one = Text(text = str(p1Life), origin = (29.5, 16.75), color = color.black)
    two = Text(text = str(p2Life), origin = (-29.4, 3), color = color.black)
    pass
    
def cardsInput(key):
    pass
