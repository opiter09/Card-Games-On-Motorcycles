from ursina import *
import cardCode.cardSprites as cardSprites
import cardCode.sharedVariables as sharedVariables

import cardCode.cardText as cardText

def cardsUpdate():
    cardText.updateText()
    cardSprites.updateSprites()
    
def cardsInput(key):
    pass
