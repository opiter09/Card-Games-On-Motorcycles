from ursina import *
import collections

import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

import cardCode.cardSprites as cardSprites
import cardCode.cardText as cardText
import cardCode.cardButtons as cardButtons
import cardCode.buttonTooltips
import cardCode.buttonMouseEvents

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

    cardText.updateText()
    cardSprites.updateSprites()
    cardButtons.updateButtons()
    
    for i in [1, 2]:
        if (shared["player" + str(i) + "Phase"] == "Relaxation"):
            if (doOnce == 0):
                Audio("cardCode/sounds/beginTurn.wav")
                doOnce = 1
            
            
    
def cardsInput(key):
    pass
