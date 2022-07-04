from ursina import *
import cardCode.sharedVariables as sharedVariables

def myGlobals():
    return globals()

pickOne = Text(text = "Select a type of influence point", origin = (1.25, 12.25), color = color.light_gray, visible = False)
pickTwo = Text(text = "Select a type of influence point", origin = (-1.25, 7.5), color = color.light_gray, visible = False)

lifeOne = Text(text = str(sharedVariables.player1Life), origin = (29.5, 16.75), color = color.black)
lifeTwo = Text(text = str(sharedVariables.player2Life), origin = (-29.4, 3), color = color.black)

manaStringOne = "S " + str(sharedVariables.player1CurrentStone) + " | P " + str(sharedVariables.player1CurrentPlant) + " | M " \
    + str(sharedVariables.player1CurrentMetal) + " | A " + \
    str(sharedVariables.player1CurrentAnimal) + " | C " + str(sharedVariables.player1CurrentCosmic)
manaOne = Text(text = manaStringOne, origin = (1.615, 13.75), color = color.white)
manaStringTwo = "S " + str(sharedVariables.player2CurrentStone) + " | P " + str(sharedVariables.player2CurrentPlant) + " | M " \
    + str(sharedVariables.player2CurrentMetal) + " | A " + \
    str(sharedVariables.player2CurrentAnimal) + " | C " + str(sharedVariables.player2CurrentCosmic)
manaTwo = Text(text = manaStringTwo, origin = (-1.63, 6), color = color.white)

deckSizeOne = Text(text = str(len(sharedVariables.player1Deck)), origin = (-7, 16.75), color = color.blue)
discardSizeOne = Text(text = str(len(sharedVariables.player1Discard)), origin = (15, 16.75), color = color.gold)
deckSizeTwo = Text(text = str(len(sharedVariables.player2Deck)), origin = (7, 3), color = color.blue)
discardSizeTwo = Text(text = str(len(sharedVariables.player2Discard)), origin = (-14, 3), color = color.gold)

def updateText():
    globals()["lifeOne"].text = str(sharedVariables.player1Life)
    globals()["lifeTwo"].text = str(sharedVariables.player2Life)

    manaStringOne = "S " + str(sharedVariables.player1CurrentStone) + " | P " + str(sharedVariables.player1CurrentPlant) + " | M " \
        + str(sharedVariables.player1CurrentMetal) + " | A " + \
        str(sharedVariables.player1CurrentAnimal) + " | C " + str(sharedVariables.player1CurrentCosmic)
    globals()["manaOne"].text = manaStringOne
    manaStringTwo = "S " + str(sharedVariables.player2CurrentStone) + " | P " + str(sharedVariables.player2CurrentPlant) + " | M " \
        + str(sharedVariables.player2CurrentMetal) + " | A " + \
        str(sharedVariables.player2CurrentAnimal) + " | C " + str(sharedVariables.player2CurrentCosmic)
    globals()["manaTwo"].text = manaStringTwo
    
    globals()["deckSizeOne"].text = str(len(sharedVariables.player1Deck))
    globals()["discardSizeOne"].text = str(len(sharedVariables.player1Discard))
    globals()["deckSizeTwo"].text = str(len(sharedVariables.player2Deck))
    globals()["discardSizeTwo"].text = str(len(sharedVariables.player2Discard))