from ursina import *

board = Sprite("sprites/board", filtering = False, position = (1000, 0, 0), collider = None)

check = None
def callOEA():
    global check
    if (check != None):
        print("It just works!")

p1discard = Sprite("sprites/deckDiscardRectangle", filtering = False, position = (998, -1.87, -0.01))
p1spellTrap1 = Sprite("sprites/zoneRectangle", filtering = False, position = (999, -1.85, -0.01))
p1spellTrap2 = Sprite("sprites/zoneRectangle", filtering = False, position = (1000, -1.85, -0.01))
p1spellTrap3 = Sprite("sprites/zoneRectangle", filtering = False, position = (1001, -1.85, -0.01))
p1deck = Sprite("sprites/deckDiscardRectangle", filtering = False, position = (1002, -1.87, -0.01))
p1pile = Sprite("sprites/deckPile", filtering = False, position = (1002.01, -1.875, -0.01))

p1monster1 = Sprite("sprites/zoneRectangle", filtering = False, position = (998, -0.6, -0.01))
p1monster2 = Sprite("sprites/zoneRectangle", filtering = False, position = (999, -0.6, -0.01))
p1monster3 = Sprite("sprites/zoneRectangle", filtering = False, position = (1000, -0.6, -0.01))
p1monster4 = Sprite("sprites/zoneRectangle", filtering = False, position = (1001, -0.6, -0.01))
p1monster5 = Sprite("sprites/zoneRectangle", filtering = False, position = (1002, -0.6, -0.01))

p1hand1 = Sprite("sprites/cardFront", filtering = False, position = (997, -1.87, 0))
p1hand2 = Sprite("sprites/cardFront", filtering = False, position = (996.1, -1.87, 0))
p1hand3 = Sprite("sprites/cardFront", filtering = False, position = (995.2, -1.87, 0))
p1hand4 = Sprite("sprites/cardFront", filtering = False, position = (994.3, -1.87, 0))
p1hand5 = Sprite("sprites/cardFront", filtering = False, position = (993.4, -1.87, 0), enabled = False)
p1hand6 = Sprite("sprites/cardFront", filtering = False, position = (992.5, -1.87, 0), enabled = False)

p1discardCard = Sprite("sprites/cardFront", filtering = False, position = (998, -1.87, -0.01), enabled = False)
p1spellTrap1Card = Sprite("sprites/cardFront", filtering = False, position = (999, -1.85, -0.01), enabled = False)
p1spellTrap2Card = Sprite("sprites/cardFront", filtering = False, position = (1000, -1.85, -0.01), enabled = False)
p1spellTrap3Card = Sprite("sprites/cardFront", filtering = False, position = (1001, -1.85, -0.01), enabled = False)

p1monster1Card = Sprite("sprites/cardFront", filtering = False, position = (998, -0.6, -0.01), enabled = False)
p1monster2Card = Sprite("sprites/cardFront", filtering = False, position = (999, -0.6, -0.01), enabled = False)
p1monster3Card = Sprite("sprites/cardFront", filtering = False, position = (1000, -0.6, -0.01), enabled = False)
p1monster4Card = Sprite("sprites/cardFront", filtering = False, position = (1001, -0.6, -0.01), enabled = False)
p1monster5Card = Sprite("sprites/cardFront", filtering = False, position = (1002, -0.6, -0.01), enabled = False)

p1lifeCircle = Entity(model = "circle", position = (991.65, -1.87, 0), scale = 0.8, color = color.turquoise)
p1manaBox = Entity(model = "quad", position = (995.3, -1, 0), color = color.gray, scale = (3, 0.5))

p2deck = Sprite("sprites/deckDiscardRectangle", filtering = False, position = (998, 1.965, -0.01))
p2pile = Sprite("sprites/deckPile", filtering = False, position = (998.01, 1.955, -0.01))
p2spellTrap1 = Sprite("sprites/zoneRectangle", filtering = False, position = (999, 1.95, -0.01))
p2spellTrap2 = Sprite("sprites/zoneRectangle", filtering = False, position = (1000, 1.95, -0.01))
p2spellTrap3 = Sprite("sprites/zoneRectangle", filtering = False, position = (1001, 1.95, -0.01))
p2discard = Sprite("sprites/deckDiscardRectangle", filtering = False, position = (1002, 1.965, -0.01))

p2monster1 = Sprite("sprites/zoneRectangle", filtering = False, position = (998, 0.7, -0.01))
p2monster2 = Sprite("sprites/zoneRectangle", filtering = False, position = (999, 0.7, -0.01))
p2monster3 = Sprite("sprites/zoneRectangle", filtering = False, position = (1000, 0.7, -0.01))
p2monster4 = Sprite("sprites/zoneRectangle", filtering = False, position = (1001, 0.7, -0.01))
p2monster5 = Sprite("sprites/zoneRectangle", filtering = False, position = (1002, 0.7, -0.01))

p2hand1 = Sprite("sprites/cardFront", filtering = False, position = (1003, 1.965, 0))
p2hand2 = Sprite("sprites/cardFront", filtering = False, position = (1003.9, 1.965, 0))
p2hand3 = Sprite("sprites/cardFront", filtering = False, position = (1004.8, 1.965, 0))
p2hand4 = Sprite("sprites/cardFront", filtering = False, position = (1005.7, 1.965, 0))
p2hand5 = Sprite("sprites/cardFront", filtering = False, position = (1006.6, 1.965, 0), enabled = False)
p2hand6 = Sprite("sprites/cardFront", filtering = False, position = (1007.5, 1.965, 0), enabled = False)

p2spellTrap1Card = Sprite("sprites/cardFront", filtering = False, position = (999, 1.95, -0.01), enabled = False)
p2spellTrap2Card = Sprite("sprites/cardFront", filtering = False, position = (1000, 1.95, -0.01), enabled = False)
p2spellTrap3Card = Sprite("sprites/cardFront", filtering = False, position = (1001, 1.95, -0.01), enabled = False)
p2discardCard = Sprite("sprites/cardFront", filtering = False, position = (1002, 1.965, -0.01), enabled = False)

p2monster1Card = Sprite("sprites/cardFront", filtering = False, position = (998, 0.7, -0.01), enabled = False)
p2monster2Card = Sprite("sprites/cardFront", filtering = False, position = (999, 0.7, -0.01), enabled = False)
p2monster3Card = Sprite("sprites/cardFront", filtering = False, position = (1000, 0.7, -0.01), enabled = False)
p2monster4Card = Sprite("sprites/cardFront", filtering = False, position = (1001, 0.7, -0.01), enabled = False)
p2monster5Card = Sprite("sprites/cardFront", filtering = False, position = (1002, 0.7, -0.01), enabled = False)

p2lifeCircle = Entity(model = "circle", position = (1008.35, 1.965, 0), scale = 0.8, color = color.turquoise)
p2manaBox = Entity(model = "quad", position = (1004.75, 1.15, 0), color = color.gray, scale = (3, 0.5))

base.camera3 = base.makeCamera(base.win, displayRegion = (0, 1, 0, 0.5))
base.camera3.reparentTo(board)
base.camera3.lookAt(board)
base.camera3.setPos(0, 0, -2)
base.camera3.node().getLens().setNearFar(1.9, 2.1)
base.camera3.node().getLens().setAspectRatio(16.0/5.0)

check = 1

def updateSprites():
    pass