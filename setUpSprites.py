from ursina import *

board = Sprite("cardSprites/board", filtering = False, position = (1000, 0, 0), collider = None)

check = None
def callOEA():
    global check
    if (check != None):
        print("It just works!")

p1discard = Sprite("cardSprites/deckDiscardRectangle", filtering = False, position = (998, -1.87, -0.01))
p1st1 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (999, -1.85, -0.01))
p1st2 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1000, -1.85, -0.01))
p1st3 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1001, -1.85, -0.01))
p1deck = Sprite("cardSprites/deckDiscardRectangle", filtering = False, position = (1002, -1.87, -0.01))
p1pile = Sprite("cardSprites/deckPile", filtering = False, position = (1002.01, -1.875, -0.01))

p1m1 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (998, -0.6, -0.01))
p1m2 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (999, -0.6, -0.01))
p1m3 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1000, -0.6, -0.01))
p1m4 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1001, -0.6, -0.01))
p1m5 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1002, -0.6, -0.01))

p1hand1 = Sprite("cardSprites/cardFront", filtering = False, position = (997, -1.87, 0))
p1hand2 = Sprite("cardSprites/cardFront", filtering = False, position = (996.1, -1.87, 0))
p1hand3 = Sprite("cardSprites/cardFront", filtering = False, position = (995.2, -1.87, 0))
p1hand4 = Sprite("cardSprites/cardFront", filtering = False, position = (994.3, -1.87, 0))
p1hand5 = Sprite("cardSprites/cardFront", filtering = False, position = (993.4, -1.87, 0), enabled = False)
p1hand6 = Sprite("cardSprites/cardFront", filtering = False, position = (992.5, -1.87, 0), enabled = False)

p1discardCard = Sprite("cardSprites/cardFront", filtering = False, position = (998, -1.87, -0.01), enabled = False)
p1st1Card = Sprite("cardSprites/cardFront", filtering = False, position = (999, -1.85, -0.01), enabled = False)
p1st2Card = Sprite("cardSprites/cardFront", filtering = False, position = (1000, -1.85, -0.01), enabled = False)
p1st3Card = Sprite("cardSprites/cardFront", filtering = False, position = (1001, -1.85, -0.01), enabled = False)

p1m1Card = Sprite("cardSprites/cardFront", filtering = False, position = (998, -0.6, -0.01), enabled = False)
p1m2Card = Sprite("cardSprites/cardFront", filtering = False, position = (999, -0.6, -0.01), enabled = False)
p1m3Card = Sprite("cardSprites/cardFront", filtering = False, position = (1000, -0.6, -0.01), enabled = False)
p1m4Card = Sprite("cardSprites/cardFront", filtering = False, position = (1001, -0.6, -0.01), enabled = False)
p1m5Card = Sprite("cardSprites/cardFront", filtering = False, position = (1002, -0.6, -0.01), enabled = False)

p1LifeCircle = Entity(model = "circle", position = (991.65, -1.87, 0), scale = 0.8, color = color.turquoise)
p1ManaBox = Entity(model = "quad", position = (995.3, -1, 0), color = color.gray, scale = (3, 0.5))

p2deck = Sprite("cardSprites/deckDiscardRectangle", filtering = False, position = (998, 1.965, -0.01))
p2pile = Sprite("cardSprites/deckPile", filtering = False, position = (998.01, 1.955, -0.01))
p2st1 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (999, 1.95, -0.01))
p2st2 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1000, 1.95, -0.01))
p2st3 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1001, 1.95, -0.01))
p2discard = Sprite("cardSprites/deckDiscardRectangle", filtering = False, position = (1002, 1.965, -0.01))

p2m1 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (998, 0.7, -0.01))
p2m2 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (999, 0.7, -0.01))
p2m3 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1000, 0.7, -0.01))
p2m4 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1001, 0.7, -0.01))
p2m5 = Sprite("cardSprites/zoneRectangle", filtering = False, position = (1002, 0.7, -0.01))

p2hand1 = Sprite("cardSprites/cardFront", filtering = False, position = (1003, 1.965, 0))
p2hand2 = Sprite("cardSprites/cardFront", filtering = False, position = (1003.9, 1.965, 0))
p2hand3 = Sprite("cardSprites/cardFront", filtering = False, position = (1004.8, 1.965, 0))
p2hand4 = Sprite("cardSprites/cardFront", filtering = False, position = (1005.7, 1.965, 0))
p2hand5 = Sprite("cardSprites/cardFront", filtering = False, position = (1006.6, 1.965, 0), enabled = False)
p2hand6 = Sprite("cardSprites/cardFront", filtering = False, position = (1007.5, 1.965, 0), enabled = False)

p2st1Card = Sprite("cardSprites/cardFront", filtering = False, position = (999, 1.95, -0.01), enabled = False)
p2st2Card = Sprite("cardSprites/cardFront", filtering = False, position = (1000, 1.95, -0.01), enabled = False)
p2st3Card = Sprite("cardSprites/cardFront", filtering = False, position = (1001, 1.95, -0.01), enabled = False)
p2discardCard = Sprite("cardSprites/cardFront", filtering = False, position = (1002, 1.965, -0.01), enabled = False)

p2m1Card = Sprite("cardSprites/cardFront", filtering = False, position = (998, 0.7, -0.01), enabled = False)
p2m2Card = Sprite("cardSprites/cardFront", filtering = False, position = (999, 0.7, -0.01), enabled = False)
p2m3Card = Sprite("cardSprites/cardFront", filtering = False, position = (1000, 0.7, -0.01), enabled = False)
p2m4Card = Sprite("cardSprites/cardFront", filtering = False, position = (1001, 0.7, -0.01), enabled = False)
p2m5Card = Sprite("cardSprites/cardFront", filtering = False, position = (1002, 0.7, -0.01), enabled = False)

p2LifeCircle = Entity(model = "circle", position = (1008.35, 1.965, 0), scale = 0.8, color = color.turquoise)
p2ManaBox = Entity(model = "quad", position = (1004.75, 1.15, 0), color = color.gray, scale = (3, 0.5))

base.camera3 = base.makeCamera(base.win, displayRegion = (0, 1, 0, 0.5))
base.camera3.reparentTo(board)
base.camera3.lookAt(board)
base.camera3.setPos(0, 0, -2)
base.camera3.node().getLens().setNearFar(1.9, 2.1)
base.camera3.node().getLens().setAspectRatio(16.0/5.0)

check = 1