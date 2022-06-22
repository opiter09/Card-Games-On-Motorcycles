from ursina import *
import cardCode.sharedVariables as sharedVariables

lifeOne = Text(text = str(sharedVariables.p1Life), origin = (29.5, 16.75), color = color.black)
lifeTwo = Text(text = str(sharedVariables.p2Life), origin = (-29.4, 3), color = color.black)
manaStringOne = "S " + str(sharedVariables.p1Stone) + "  P " + str(sharedVariables.p1Plant) + "  M " + str(sharedVariables.p1Metal) + "  A " + \
    str(sharedVariables.p1Animal) + "  E " + str(sharedVariables.p1Extraterrestrial)
manaOne = Text(text = manaStringOne, origin = (2, 13.75), color = color.white)
manaStringTwo = "S " + str(sharedVariables.p2Stone) + "  P " + str(sharedVariables.p2Plant) + "  M " + str(sharedVariables.p2Metal) + "  A " + \
    str(sharedVariables.p2Animal) + "  E " + str(sharedVariables.p2Extraterrestrial)
manaTwo = Text(text = manaStringTwo, origin = (-2, 6), color = color.white)
mousePos = Text(text = str(mouse.position.getX()) + ", " + str(mouse.position.getY()))

def updateText():
    global lifeOne
    global lifeTwo
    global manaOne
    global ManaTwo
    global mousePos
    
    lifeOne.text = str(sharedVariables.p1Life)
    lifeTwo.text = str(sharedVariables.p2Life)
    manaStringOne = "S " + str(sharedVariables.p1Stone) + "  P " + str(sharedVariables.p1Plant) + "  M " + str(sharedVariables.p1Metal) + "  A " + \
        str(sharedVariables.p1Animal) + "  E " + str(sharedVariables.p1Extraterrestrial)
    manaOne.text = manaStringOne
    manaStringTwo = "S " + str(sharedVariables.p2Stone) + "  P " + str(sharedVariables.p2Plant) + "  M " + str(sharedVariables.p2Metal) + "  A " + \
        str(sharedVariables.p2Animal) + "  E " + str(sharedVariables.p2Extraterrestrial)
    manaTwo.text = manaStringTwo
    mousePos.text = str(mouse.position.getX()) + ", " + str(mouse.position.getY())
    mousePos.text = str(mouse.position.getX()) + ", " + str(mouse.position.getY())