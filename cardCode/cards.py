from ursina import *
import collections
import os.path

import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

import cardCode.cardSprites as cardSprites
import cardCode.cardText as cardText
import cardCode.cardButtons as cardButtons
import cardCode.buttonTooltips as buttonTooltips
import cardCode.buttonMouseEvents as buttonMouseEvents
import cardCode.effectFunctions as effectFunctions
import cardCode.effectResolution as effectResolution

check = 0
check2 = 0
for i in [1, 2]:
    if (len(shared["player" + str(i) + "OriginalDeck"]) != 40) and (os.path.exists("../o_o.ini") == False):
        check2 = 1
    counting = collections.Counter(shared["player" + str(i) + "OriginalDeck"])
    for k in counting.values():
        if (k > 2) and (os.path.exists("../o_o.ini") == False):
            check = 1
if (check == 1):
    Text(text = "ILLEGAL DECK DETECTED. ONLY 2 COPIES OF A CARD ARE ALLOWED.", color = color.red, origin = (0, -10))
if (check2 == 1):
    Text(text = "ILLEGAL DECK DETECTED. DECKS MUST HAVE EXACTLY 40 CARDS.", color = color.red, origin = (0, -9))

doOnce = 0
def cardsUpdate():
    global check
    global check2
    global doOnce
    global shared

    if (check >= 2):
        check = 0
        check2 = 0
        #application.quit()
    elif (check != 0) and (check < 2):
        check = check + 0.007

    if (check2 >= 2):
        check = 0
        check2 = 0
        application.quit()
    elif (check2 != 0) and (check2 < 2):
        check2 = check2 + 0.007
    
    if (shared["player1Life"] > 99):
        shared["player1Life"] = 99
    if (shared["player2Life"] > 99):
        shared["player2Life"] = 99

    if (shared["player1Life"] < 0):
        shared["player1Life"] = 0
    if (shared["player2Life"] < 0):
        shared["player2Life"] = 0

    for i in [1, 2]:
        if (shared["player" + str(i) + "Life"] == 0) and (check2 == 0):
            other = { "1": "2", "2": "1" }
            WindowPanel(title = "", text = "Player " + other[str(i)] + " wins!", text_color = color.magenta)
            check2 = 1

        if (shared["player" + str(i) + "Phase"] == "Relaxation") and (shared["turnCount"] > 0) and (doOnce == 0):
            doOnce = 1
            Audio("cardCode/sounds/beginTurn.wav")

            if (shared["turnCount"] > 0.5):
                effectFunctions.drawCards(1, i)
                buttonTooltips.updateTooltips()
            else:
                shared["turnCount"] = 1
                
            for j in [1, 2, 3, 4, 5]:
                if (len(shared["player" + str(i) + "Comrades"][str(j - 1)]) > 0):
                    shared["player" + str(i) + "Comrades"][str(j - 1)]["Contracted"] = "False"
            for j in [1, 2, 3]:
                if (len(shared["player" + str(i) + "Auxiliaries"][str(j - 1)]) > 0):
                    shared["player" + str(i) + "Auxiliaries"][str(j - 1)]["Contracted"] = "False"
            
            for j in ["Stone", "Plant", "Metal", "Animal", "Cosmic"]:
                shared["player" + str(i) + "Current" + j] = shared["player" + str(i) + j]

            if (i == 1):
                cardText.myGlobals()["pickOne"].visible = True
            else:
                cardText.myGlobals()["pickTwo"].visible = True
                
        if (shared["player" + str(i) + "Phase"] == "Maintenance") or (shared["player" + str(i) + "Phase"] == "Main2"):
            doOnce = 0

    effectResolution.emptyTheStack()
    cardText.updateText()
    cardSprites.updateSprites()
    cardButtons.updateButtons()
    
def cardsInput(key):
    global shared

    if (key == "space"):
        if (shared["player1Active"] == True):
            shared["player1Active"] = False
            shared["resolveNow"] = shared["resolveNow"] + 1
            if (shared["resolveNow"] < 2):
                shared["player2Active"] = True
                return

        if (shared["player2Active"] == True):
            shared["player2Active"] = False
            shared["resolveNow"] = shared["resolveNow"] + 1
            if (shared["resolveNow"] < 2):
                shared["player1Active"] = True
                return
                
