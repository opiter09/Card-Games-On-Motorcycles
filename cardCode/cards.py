from ursina import *
import collections

import cardCode.sharedVariables as sharedVariables

import cardCode.cardSprites as cardSprites
import cardCode.cardText as cardText
import cardCode.buttonTooltips as buttonTooltips

#check = 0
#for i in [1, 2]:
    #counting = collections.Counter(sharedVariables.myGlobals()["player" + str(i) + "Deck"])
    #for k in counting.values():
        #if (k > 2):
            #check = 1
#if (check == 1):
    #Text(text = "ILLEGAL DECK DETECTED. ONLY 2 COPIES OF A CARD ARE ALLOWED.", color = color.red, origin = (0, -10))

def cardsUpdate():
    #global check
    #if (check >= 2):
        #check = 0
        #application.quit()
    #elif (check != 0) and (check < 2):
        #check = check + 0.2

    cardText.updateText()
    cardSprites.updateSprites()
    buttonTooltips.updateTooltips()
    
def cardsInput(key):
    pass
