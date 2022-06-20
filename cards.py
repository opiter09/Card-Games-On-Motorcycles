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
base.camera3 = createCamera(base, (0, 0.5, 0, 0.5))
base.camera3.reparentTo(board)
base.camera3.lookAt(board)
base.camera3.setPos(0, 0, -2)
base.camera3.node().getLens().setNearFar(1.9, 2.1)