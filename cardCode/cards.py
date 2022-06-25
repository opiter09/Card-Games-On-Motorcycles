from ursina import *

import cardCode.sharedVariables as sharedVariables

import cardCode.cardSprites as cardSprites
import cardCode.cardText as cardText
import cardCode.cardTooltips as cardTooltips

def cardsUpdate():
    cardText.updateText()
    cardSprites.updateSprites()
    
def cardsInput(key):
    pass
