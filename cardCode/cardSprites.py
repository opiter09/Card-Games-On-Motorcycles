from ursina import *
import cardCode.sharedVariables as sharedVariables

board = Sprite("sprites/board", filtering = False, position = (1000, 0, 0), collider = None)


p1discard = Sprite("sprites/deckDiscardRectangle", filtering = False, position = (998, -1.87, -0.01))
p1auxiliary1 = Sprite("sprites/zoneRectangle", filtering = False, position = (999, -1.85, -0.01))
p1auxiliary2 = Sprite("sprites/zoneRectangle", filtering = False, position = (1000, -1.85, -0.01))
p1auxiliary3 = Sprite("sprites/zoneRectangle", filtering = False, position = (1001, -1.85, -0.01))
p1deck = Sprite("sprites/deckDiscardRectangle", filtering = False, position = (1002, -1.87, -0.01))
p1pile = Sprite("sprites/deckPile", filtering = False, position = (1002.01, -1.875, -0.01))

p1comrade1 = Sprite("sprites/zoneRectangle", filtering = False, position = (998, -0.6, -0.01))
p1comrade2 = Sprite("sprites/zoneRectangle", filtering = False, position = (999, -0.6, -0.01))
p1comrade3 = Sprite("sprites/zoneRectangle", filtering = False, position = (1000, -0.6, -0.01))
p1comrade4 = Sprite("sprites/zoneRectangle", filtering = False, position = (1001, -0.6, -0.01))
p1comrade5 = Sprite("sprites/zoneRectangle", filtering = False, position = (1002, -0.6, -0.01))

p1hand1 = Sprite("sprites/cardFront", filtering = False, position = (997, -1.87, 0))
p1hand2 = Sprite("sprites/cardFront", filtering = False, position = (996.1, -1.87, 0))
p1hand3 = Sprite("sprites/cardFront", filtering = False, position = (995.2, -1.87, 0))
p1hand4 = Sprite("sprites/cardFront", filtering = False, position = (994.3, -1.87, 0))
p1hand5 = Sprite("sprites/cardFront", filtering = False, position = (993.4, -1.87, 0), enabled = False)
p1hand6 = Sprite("sprites/cardFront", filtering = False, position = (992.5, -1.87, 0), enabled = False)

p1discardCard = Sprite("sprites/cardFront", filtering = False, position = (998, -1.87, -0.01), enabled = False)
p1auxiliary1Card = Sprite("sprites/cardFront", filtering = False, position = (999, -1.85, -0.01), enabled = False)
p1auxiliary2Card = Sprite("sprites/cardFront", filtering = False, position = (1000, -1.85, -0.01), enabled = False)
p1auxiliary3Card = Sprite("sprites/cardFront", filtering = False, position = (1001, -1.85, -0.01), enabled = False)

p1comrade1Card = Sprite("sprites/cardFront", filtering = False, position = (998, -0.6, -0.01), enabled = False)
p1comrade2Card = Sprite("sprites/cardFront", filtering = False, position = (999, -0.6, -0.01), enabled = False)
p1comrade3Card = Sprite("sprites/cardFront", filtering = False, position = (1000, -0.6, -0.01), enabled = False)
p1comrade4Card = Sprite("sprites/cardFront", filtering = False, position = (1001, -0.6, -0.01), enabled = False)
p1comrade5Card = Sprite("sprites/cardFront", filtering = False, position = (1002, -0.6, -0.01), enabled = False)

p1lifeCircle = Entity(model = "circle", position = (991.65, -1.87, 0), scale = 0.8, color = color.turquoise)
p1manaBox = Entity(model = "quad", position = (995.3, -1, 0), color = color.gray, scale = (3, 0.5))

p2deck = Sprite("sprites/deckDiscardRectangle", filtering = False, position = (998, 1.965, -0.01))
p2pile = Sprite("sprites/deckPile", filtering = False, position = (998.01, 1.955, -0.01))
p2auxiliary1 = Sprite("sprites/zoneRectangle", filtering = False, position = (999, 1.95, -0.01))
p2auxiliary2 = Sprite("sprites/zoneRectangle", filtering = False, position = (1000, 1.95, -0.01))
p2auxiliary3 = Sprite("sprites/zoneRectangle", filtering = False, position = (1001, 1.95, -0.01))
p2discard = Sprite("sprites/deckDiscardRectangle", filtering = False, position = (1002, 1.965, -0.01))

p2comrade1 = Sprite("sprites/zoneRectangle", filtering = False, position = (998, 0.7, -0.01))
p2comrade2 = Sprite("sprites/zoneRectangle", filtering = False, position = (999, 0.7, -0.01))
p2comrade3 = Sprite("sprites/zoneRectangle", filtering = False, position = (1000, 0.7, -0.01))
p2comrade4 = Sprite("sprites/zoneRectangle", filtering = False, position = (1001, 0.7, -0.01))
p2comrade5 = Sprite("sprites/zoneRectangle", filtering = False, position = (1002, 0.7, -0.01))

p2hand1 = Sprite("sprites/cardFront", filtering = False, position = (1003, 1.965, 0))
p2hand2 = Sprite("sprites/cardFront", filtering = False, position = (1003.9, 1.965, 0))
p2hand3 = Sprite("sprites/cardFront", filtering = False, position = (1004.8, 1.965, 0))
p2hand4 = Sprite("sprites/cardFront", filtering = False, position = (1005.7, 1.965, 0))
p2hand5 = Sprite("sprites/cardFront", filtering = False, position = (1006.6, 1.965, 0), enabled = False)
p2hand6 = Sprite("sprites/cardFront", filtering = False, position = (1007.5, 1.965, 0), enabled = False)

p2auxiliary1Card = Sprite("sprites/cardFront", filtering = False, position = (999, 1.95, -0.01), enabled = False)
p2auxiliary2Card = Sprite("sprites/cardFront", filtering = False, position = (1000, 1.95, -0.01), enabled = False)
p2auxiliary3Card = Sprite("sprites/cardFront", filtering = False, position = (1001, 1.95, -0.01), enabled = False)
p2discardCard = Sprite("sprites/cardFront", filtering = False, position = (1002, 1.965, -0.01), enabled = False)

p2comrade1Card = Sprite("sprites/cardFront", filtering = False, position = (998, 0.7, -0.01), enabled = False)
p2comrade2Card = Sprite("sprites/cardFront", filtering = False, position = (999, 0.7, -0.01), enabled = False)
p2comrade3Card = Sprite("sprites/cardFront", filtering = False, position = (1000, 0.7, -0.01), enabled = False)
p2comrade4Card = Sprite("sprites/cardFront", filtering = False, position = (1001, 0.7, -0.01), enabled = False)
p2comrade5Card = Sprite("sprites/cardFront", filtering = False, position = (1002, 0.7, -0.01), enabled = False)

p2lifeCircle = Entity(model = "circle", position = (1008.35, 1.965, 0), scale = 0.8, color = color.turquoise)
p2manaBox = Entity(model = "quad", position = (1004.75, 1.15, 0), color = color.gray, scale = (3, 0.5))

base.camera3 = base.makeCamera(base.win, displayRegion = (0, 1, 0, 0.5))
base.camera3.reparentTo(board)
base.camera3.lookAt(board)
base.camera3.setPos(0, 0, -2)
base.camera3.node().getLens().setNearFar(1.9, 2.1)
base.camera3.node().getLens().setAspectRatio(16.0/5.0)

def camelCase(spaced):
    split = spaced.split()
    beginning = split[0][0].lower() + split[0][1:1000]
    final = "0"
    for i in split:
        if (final == "0"):
            final = beginning
        else:
            final = final + i
    return final

def updateSprites():    
    sharedGlobals = sharedVariables.myGlobals()
    for i in [1, 2]:
        for j in [1, 2, 3, 4, 5, 6]:
            if (len(sharedGlobals["player" + str(i) + "Hand"]) >= j):
                globals()["p" + str(i) + "hand" + str(j)].texture = "sprites/cardArt/" + camelCase(sharedGlobals["player" + str(i) + "Hand"][j - 1])
                globals()["p" + str(i) + "hand" + str(j)].enabled = True
            else:
                globals()["p" + str(i) + "hand" + str(j)].enabled = False

        for j in [1, 2, 3, 4, 5]:
            if (len(sharedGlobals["player" + str(i) + "Comrades"]) >= j):
                globals()["p" + str(i) + "comrade" + str(j) + "Card"].texture = "sprites/cardArt/" + camelCase(sharedGlobals["player" + str(i) + "Comrades"][j - 1]["Name"])
                globals()["p" + str(i) + "comrade" + str(j) + "Card"].enabled = True
                if (sharedGlobals["player" + str(i) + "Comrades"][j - 1]["Contracted"] == "True"):
                    globals()["p" + str(i) + "comrade" + str(j) + "Card"].rotation_y = 180
                else:
                    globals()["p" + str(i) + "comrade" + str(j) + "Card"].rotation_y = 0
            else:
                globals()["p" + str(i) + "comrade" + str(j) + "Card"].enabled = False

        for j in [1, 2, 3]:
            if (len(sharedGlobals["player" + str(i) + "Auxiliaries"]) >= j):
                globals()["p" + str(i) + "auxiliary" + str(j) + "Card"].texture = "sprites/cardArt/" + camelCase(sharedGlobals["player" + str(i) + "Auxiliaries"][j - 1]["Name"])
                globals()["p" + str(i) + "auxiliary" + str(j) + "Card"].enabled = True
                if (sharedGlobals["player" + str(i) + "Auxiliaries"][j - 1]["Contracted"] == "True"):
                    globals()["p" + str(i) + "comrade" + str(j) + "Card"].rotation_y = 180
                else:
                    globals()["p" + str(i) + "comrade" + str(j) + "Card"].rotation_y = 0
            else:
                globals()["p" + str(i) + "auxiliary" + str(j) + "Card"].enabled = False
                
        if (len(sharedGlobals["player" + str(i) + "Discard"]) > 0):
            globals()["p" + str(i) + "discardCard"].texture = "sprites/cardArt/" + camelCase(sharedGlobals["player" + str(i) + "Discard"][0])
            globals()["p" + str(i) + "discardCard"].enabled = True
        else:
            globals()["p" + str(i) + "discardCard"].enabled = False
            
        if (sharedGlobals["player" + str(i) + "Life"] > 7):
            globals()["p" + str(i) + "lifeCircle"].color = color.turquoise
        else:
            globals()["p" + str(i) + "lifeCircle"].color = color.red       
    