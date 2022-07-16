from ursina import *
import cardCode.buttonTooltips as buttonTooltips
import cardCode.cardText as cardText

import cardCode.cardButtons as cardButtons
buttons = cardButtons.myGlobals()

import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

import cardCode.cardParser as cardParser

def test(param):
    print(param)

def exitUpdate():
    buttonTooltips.updateTooltips()
    for i in [1, 2]:
        for j in [1, 2, 3, 4, 5, 6]:
            buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.enabled = False
        for j in [1, 2, 3, 4, 5]:
            buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.enabled = False
        for j in [1, 2, 3]:
            buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.enabled = False
        buttons["p" + str(i) + "discardButton"].tooltip.enabled = False

for i in [1, 2]:
    for j in [1, 2, 3, 4, 5, 6]:
        buttons["p" + str(i) + "hand" + str(j) + "Button"].on_mouse_exit = exitUpdate
    for j in [1, 2, 3, 4, 5]:
        buttons["p" + str(i) + "comrade" + str(j) + "Button"].on_mouse_exit = exitUpdate
    for j in [1, 2, 3]:
        buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].on_mouse_exit = exitUpdate
    buttons["p" + str(i) + "discardButton"].on_mouse_exit = exitUpdate


def handClick(player, slot):
    pass
    
def comradesClick(player, slot):
    pass
    
def auxiliariesClick(player, slot):
    pass
    
def discardClick(player):
    pass
    
def influenceClick(player, classification):
    if (player == 1) and (cardText.myGlobals()["pickOne"].visible == True):
        if (shared["player1Stone"] + shared["player1Plant"] + shared["player1Metal"] + shared["player1Animal"] + shared["player1Cosmic"] < 9):
            shared["player1" + classification] = shared["player1" + classification] + 1
            shared["player1Current" + classification] = shared["player1Current" + classification] + 1
        cardText.myGlobals()["pickOne"].visible = False
        shared["player1Phase"] = "Maintenance"
        cardParser.maintenanceTriggers(1)
    elif (player == 2) and (cardText.myGlobals()["pickTwo"].visible == True):
        if (shared["player2Stone"] + shared["player2Plant"] + shared["player2Metal"] + shared["player2Animal"] + shared["player2Cosmic"] < 9):
            shared["player2" + classification] = shared["player2" + classification] + 1
            shared["player2Current" + classification] = shared["player2Current" + classification] + 1
        cardText.myGlobals()["pickTwo"].visible = False
        shared["player2Phase"] = "Maintenance"
        cardParser.maintenanceTriggers(2)

buttons["p1hand1Button"].on_double_click = Func(lambda: handClick(1, 1))
buttons["p1hand2Button"].on_double_click = Func(lambda: handClick(1, 2))
buttons["p1hand3Button"].on_double_click = Func(lambda: handClick(1, 3))
buttons["p1hand4Button"].on_double_click = Func(lambda: handClick(1, 4))
buttons["p1hand5Button"].on_double_click = Func(lambda: handClick(1, 5))
buttons["p1hand6Button"].on_double_click = Func(lambda: handClick(1, 6))

buttons["p2hand1Button"].on_double_click = Func(lambda: handClick(2, 1))
buttons["p2hand2Button"].on_double_click = Func(lambda: handClick(2, 2))
buttons["p2hand3Button"].on_double_click = Func(lambda: handClick(2, 3))
buttons["p2hand4Button"].on_double_click = Func(lambda: handClick(2, 4))
buttons["p2hand5Button"].on_double_click = Func(lambda: handClick(2, 5))
buttons["p2hand6Button"].on_double_click = Func(lambda: handClick(2, 6))

buttons["p1comrade1Button"].on_double_click = Func(lambda: comradesClick(1, 1))
buttons["p1comrade2Button"].on_double_click = Func(lambda: comradesClick(1, 2))
buttons["p1comrade3Button"].on_double_click = Func(lambda: comradesClick(1, 3))
buttons["p1comrade4Button"].on_double_click = Func(lambda: comradesClick(1, 4))
buttons["p1comrade5Button"].on_double_click = Func(lambda: comradesClick(1, 5))

buttons["p2comrade1Button"].on_double_click = Func(lambda: comradesClick(2, 1))
buttons["p2comrade2Button"].on_double_click = Func(lambda: comradesClick(2, 2))
buttons["p2comrade3Button"].on_double_click = Func(lambda: comradesClick(2, 3))
buttons["p2comrade4Button"].on_double_click = Func(lambda: comradesClick(2, 4))
buttons["p2comrade5Button"].on_double_click = Func(lambda: comradesClick(2, 5))

buttons["p1auxiliary1Button"].on_double_click = Func(lambda: auxiliariesClick(1, 1))
buttons["p1auxiliary2Button"].on_double_click = Func(lambda: auxiliariesClick(1, 2))
buttons["p1auxiliary3Button"].on_double_click = Func(lambda: auxiliariesClick(1, 3))

buttons["p2auxiliary1Button"].on_double_click = Func(lambda: auxiliariesClick(2, 1))
buttons["p2auxiliary2Button"].on_double_click = Func(lambda: auxiliariesClick(2, 2))
buttons["p2auxiliary3Button"].on_double_click = Func(lambda: auxiliariesClick(2, 3))

buttons["p1discardButton"].on_double_click = Func(lambda: discardClick(1))
buttons["p2discardButton"].on_double_click = Func(lambda: discardClick(2))

buttons["p1stoneButton"].on_double_click = Func(lambda: influenceClick(1, "Stone"))
buttons["p1plantButton"].on_double_click = Func(lambda: influenceClick(1, "Plant"))
buttons["p1metalButton"].on_double_click = Func(lambda: influenceClick(1, "Metal"))
buttons["p1animalButton"].on_double_click = Func(lambda: influenceClick(1, "Animal"))
buttons["p1cosmicButton"].on_double_click = Func(lambda: influenceClick(1, "Cosmic"))

buttons["p2stoneButton"].on_double_click = Func(lambda: influenceClick(2, "Stone"))
buttons["p2plantButton"].on_double_click = Func(lambda: influenceClick(2, "Plant"))
buttons["p2metalButton"].on_double_click = Func(lambda: influenceClick(2, "Metal"))
buttons["p2animalButton"].on_double_click = Func(lambda: influenceClick(2, "Animal"))
buttons["p2cosmicButton"].on_double_click = Func(lambda: influenceClick(2, "Cosmic"))