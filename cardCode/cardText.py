from ursina import *
import cardCode.sharedVariables as sharedVariables

lifeOne = Text(text = str(sharedVariables.player1Life), origin = (29.5, 16.75), color = color.black)
lifeTwo = Text(text = str(sharedVariables.player2Life), origin = (-29.4, 3), color = color.black)

manaStringOne = "S " + str(sharedVariables.player1Stone) + " | P " + str(sharedVariables.player1Plant) + " | M " + str(sharedVariables.player1Metal) + " | A " + \
    str(sharedVariables.player1Animal) + " | C " + str(sharedVariables.player1Cosmic)
manaOne = Text(text = manaStringOne, origin = (1.615, 13.75), color = color.white)
manaStringTwo = "S " + str(sharedVariables.player2Stone) + " | P " + str(sharedVariables.player2Plant) + " | M " + str(sharedVariables.player2Metal) + " | A " + \
    str(sharedVariables.player2Animal) + " | C " + str(sharedVariables.player2Cosmic)
manaTwo = Text(text = manaStringTwo, origin = (-1.63, 6), color = color.white)

deckSizeOne = Text(text = str(len(sharedVariables.player1Deck)), origin = (-7, 16.75), color = color.blue)
discardSizeOne = Text(text = str(len(sharedVariables.player1Discard)), origin = (15, 16.75), color = color.blue)
deckSizeTwo = Text(text = str(len(sharedVariables.player2Deck)), origin = (7, 3), color = color.blue)
discardSizeTwo = Text(text = str(len(sharedVariables.player2Discard)), origin = (-14, 3), color = color.blue)

def updateText():
    globals()["lifeOne"].text = str(sharedVariables.player1Life)
    globals()["lifeTwo"].text = str(sharedVariables.player2Life)

    manaStringOne = "S " + str(sharedVariables.player1Stone) + " | P " + str(sharedVariables.player1Plant) + " | M " + str(sharedVariables.player1Metal) + " | A " + \
        str(sharedVariables.player1Animal) + " | C " + str(sharedVariables.player1Cosmic)
    globals()["manaOne"].text = manaStringOne
    manaStringTwo = "S " + str(sharedVariables.player2Stone) + " | P " + str(sharedVariables.player2Plant) + " | M " + str(sharedVariables.player2Metal) + " | A " + \
        str(sharedVariables.player2Animal) + " | C " + str(sharedVariables.player2Cosmic)
    globals()["manaTwo"].text = manaStringTwo
    
    globals()["deckSizeOne"].text = str(len(sharedVariables.player1Deck))
    globals()["discardSizeOne"].text = str(len(sharedVariables.player1Discard))
    globals()["deckSizeTwo"].text = str(len(sharedVariables.player2Deck))
    globals()["discardSizeTwo"].text = str(len(sharedVariables.player2Discard))