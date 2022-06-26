from ursina import *

import cardCode.sharedVariables as sharedVariables

import cardCode.cardSprites as cardSprites
import cardCode.cardText as cardText
import cardCode.buttonTooltips as buttonTooltips

def cardsUpdate():
    cardText.updateText()
    cardSprites.updateSprites()
    buttonTooltips.updateTooltips()
    
def cardsInput(key):
    pass
