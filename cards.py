from ursina import *

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

def createCamera(self, dispRegion):
    theCamera = base.makeCamera(base.win, displayRegion = dispRegion)
    theCamera.setPos(0, 0, -10)
    return theCamera

board = Sprite("cardSprites/board", filtering = False, position = (1000, 0, 0))

p1discard = Sprite("cardSprites/deckDiscardRectangle", filtering = False, position = (998, -1.87, -0.01))
p1st1 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (999, -1.85, -0.01))
p1st2 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1000, -1.85, -0.01))
p1st3 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1001, -1.85, -0.01))
p1deck= Sprite("cardSprites/deckDiscardRectangle", filtering = False, position = (1002, -1.87, -0.01))

p1m1 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (998, -0.6, -0.01))
p1m2 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (999, -0.6, -0.01))
p1m3 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1000, -0.6, -0.01))
p1m4 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1001, -0.6, -0.01))
p1m5 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1002, -0.6, -0.01))

p2deck = Sprite("cardSprites/deckDiscardRectangle", filtering = False, position = (998, 1.965, -0.01))
p2st1 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (999, 1.95, -0.01))
p2st2 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1000, 1.95, -0.01))
p2st3 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1001, 1.95, -0.01))
p2discard = Sprite("cardSprites/deckDiscardRectangle", filtering = False, position = (1002, 1.965, -0.01))

p2m1 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (998, 0.7, -0.01))
p2m2 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (999, 0.7, -0.01))
p2m3 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1000, 0.7, -0.01))
p2m4 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1001, 0.7, -0.01))
p2m5 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1002, 0.7, -0.01))

#Sprite("cardSprites/cardFront", filtering = False, position = (992.5, -1.87, 0))
#Sprite("cardSprites/cardFront", filtering = False, position = (993.4, -1.87, 0))
#Sprite("cardSprites/cardFront", filtering = False, position = (994.3, -1.87, 0))
#Sprite("cardSprites/cardFront", filtering = False, position = (995.2, -1.87, 0))
#Sprite("cardSprites/cardFront", filtering = False, position = (996.1, -1.87, 0))
#Sprite("cardSprites/cardFront", filtering = False, position = (997, -1.87, 0))
p1Life = Entity(model = "circle", position = (991.65, -1.87, 0), scale = 0.8, color = color.turquoise)

base.camera3 = createCamera(base, (0, 1, 0, 0.5))
base.camera3.reparentTo(board)
base.camera3.lookAt(board)
base.camera3.setPos(0, 0, -2)
base.camera3.node().getLens().setNearFar(1.9, 2.1)
base.camera3.node().getLens().setAspectRatio(16.0/5.0)