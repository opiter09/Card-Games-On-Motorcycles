from ursina import *
import cardCode.buttonTooltips as buttonTooltips

import cardCode.cardButtons as cardButtons
buttons = cardButtons.myGlobals()

for i in [1, 2]:
    for j in [1, 2, 3, 4, 5, 6]:
        buttons["p" + str(i) + "hand" + str(j) + "Button"].mouse_enter = buttonTooltips.updateTooltips()
    for j in [1, 2, 3, 4, 5]:
        buttons["p" + str(i) + "comrade" + str(j) + "Button"].mouse_enter = buttonTooltips.updateTooltips()
    for j in [1, 2, 3]:
        buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].mouse_enter = buttonTooltips.updateTooltips()
    buttons["p" + str(i) + "discardButton"].mouse_enter = buttonTooltips.updateTooltips()