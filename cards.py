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

p1Stone = p1Plant = p1Metal = p1Animal = p1Extraterrestrial = 0
p2Stone = p2Plant = p2Metal = p2Animal = p2Extraterrestrial = 0

def cardsUpdate():
    one = Text(text = str(p1Life), origin = (29.5, 16.75), color = color.black)
    two = Text(text = str(p2Life), origin = (-29.4, 3), color = color.black)
    manaStringOne = "S " + str(p1Stone) + "  P " + str(p1Plant) + "  M " + str(p1Metal) + "  A " + str(p1Animal) + "  E " + str(p1Extraterrestrial)
    manaOne = Text(text = manaStringOne, origin = (2, 13.75), color = color.white)
    manaStringTwo = "S " + str(p2Stone) + "  P " + str(p2Plant) + "  M " + str(p2Metal) + "  A " + str(p2Animal) + "  E " + str(p2Extraterrestrial)
    manaTwo = Text(text = manaStringTwo, origin = (-2, 6), color = color.white)
    pass
    
def cardsInput(key):
    pass
