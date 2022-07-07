from ursina import *
import collections

import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

import cardCode.cardSprites as cardSprites
import cardCode.cardText as cardText
import cardCode.cardButtons as cardButtons
import cardCode.buttonTooltips as buttonTooltips
import cardCode.buttonMouseEvents as buttonMouseEvents

check = 0
check2 = 0
for i in [1, 2]:
    if (len(shared["player" + str(i) + "OriginalDeck"]) != 40):
        check2 = 1
    counting = collections.Counter(shared["player" + str(i) + "OriginalDeck"])
    for k in counting.values():
        if (k > 2):
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
        #application.quit()
    elif (check2 != 0) and (check2 < 2):
        check2 = check2 + 0.007
    
    for i in [1, 2]:
        if (shared["player" + str(i) + "Phase"] == "Relaxation") and (shared["turnCount"] > 0) and (doOnce == 0):
            doOnce = 1
            Audio("cardCode/sounds/beginTurn.wav")

            if (shared["turnCount"] > 0.5):
                shared["turnCount"] = shared["turnCount"] + 1
                if (len(shared["player" + str(i) + "Hand"]) == 6):
                    shared["player" + str(i) + "Discard"].insert(0, shared["player" + str(i) + "Hand"][0])
                    shared["player" + str(i) + "Hand"] = shared["player" + str(i) + "Hand"][1:6]
                if (len(shared["player" + str(i) + "Deck"]) == 0):
                    #eventual losing code
                    pass
                shared["player" + str(i) + "Hand"].insert(7, shared["player" + str(i) + "Deck"][0])
                shared["player" + str(i) + "Deck"].pop(0)
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
                
    cardText.updateText()
    cardSprites.updateSprites()
    cardButtons.updateButtons()
    
def cardsInput(key):
    pass
