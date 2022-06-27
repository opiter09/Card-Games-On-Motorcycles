from ursina import *
import cardCode.buttonTooltips as buttonTooltips

import cardCode.cardButtons as cardButtons
buttons = cardButtons.myGlobals()

def enter():
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
        buttons["p" + str(i) + "hand" + str(j) + "Button"].on_mouse_exit = enter
    for j in [1, 2, 3, 4, 5]:
        buttons["p" + str(i) + "comrade" + str(j) + "Button"].on_mouse_exit = enter
    for j in [1, 2, 3]:
        buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].on_mouse_exit = enter
    buttons["p" + str(i) + "discardButton"].on_mouse_exit = enter