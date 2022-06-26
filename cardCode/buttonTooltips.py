from ursina import *
from cardCode.bigCardTable import bigTable

import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

import cardCode.cardButtons as cardButtons
buttons = cardButtons.myGlobals()

def makeTooltipText(i, j, entry, theString, change):
    if (j > len(shared["player" + str(i) + theString])):
        return ""
    if (change == True):
        text = shared["player" + str(i) + theString][str(j - 1)]["Name"] + "     " + entry["cost"] + "\n"
    else:
        text = shared["player" + str(i) + theString][j - 1] + "     " + entry["cost"] + "\n"

    if (entry["type"] == "Comrade"):
        if (change == False):
            text = text + "Strength: " + str(entry["strength"]) + "  Vitality: " + str(entry["vitality"]) + "\n"
        else:
            text = text + "Strength: " + str(entry["strength"]) + " + " + str(shared["player" + str(i) + theString][str(j - 1)]["StrengthChange"])
            text = text + "  Vitality: " + str(entry["vitality"]) + " + " + str(shared["player" + str(i) + theString][str(j - 1)]["VitalityChange"]) + "\n"

    text = text + entry["type"]
    if (entry["type"] == "Comrade"):
        text = text + "~" + entry["subType"]
    elif (entry["type"] == "Accent"):
        text = text + "~" + entry["target"]
    for k in range(len(entry["effects"])):
        text = text + "\n" + entry["effects"][k]
    return text

for i in [1, 2]:
    for j in [1, 2, 3, 4, 5, 6]:
        if (j <= len(shared["player" + str(i) + "Hand"])):
            entry = bigTable[shared["player" + str(i) + "Hand"][j - 1]]
            text = makeTooltipText(i, j, entry, "Hand", False)
            effectsLength = 0
            for k in range(len(entry["effects"])):
                effectsLength = effectsLength + len(entry["effects"][k])
            sizeFactor = effectsLength / 79.15
            if (i == 1):
                buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.3 - sizeFactor,
                    ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -5.6 - sizeFactor,
                    ignore = True, background = False, color = color.white)
        else:
            if (i == 1):
                buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)           

    for j in [1, 2, 3, 4, 5]:
        if (j <= len(shared["player" + str(i) + "Comrades"])):
            entry = bigTable[shared["player" + str(i) + "Comrades"][str(j - 1)]["Name"]]
            text = makeTooltipText(i, j, entry, "Comrades", True)
            effectsLength = 0
            for k in range(len(entry["effects"])):
                effectsLength = effectsLength + len(entry["effects"][k])
            sizeFactor = effectsLength / 79.15
            if (i == 1):
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.3 - sizeFactor,
                    ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -5.6 - sizeFactor,
                    ignore = True, background = False, color = color.white)
        else:
            if (i == 1):
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)

    for j in [1, 2, 3]:
        if (j <= len(shared["player" + str(i) + "Auxiliaries"])):
            entry = bigTable[shared["player" + str(i) + "Auxiliaries"][str(j - 1)]["Name"]]
            text = makeTooltipText(i, j, entry, "Auxiliaries", True)
            effectsLength = 0
            for k in range(len(entry["effects"])):
                effectsLength = effectsLength + len(entry["effects"][k])
            sizeFactor = effectsLength / 79.15
            if (i == 1):
                buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.3 - sizeFactor,
                    ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -5.6 - sizeFactor,
                    ignore = True, background = False, color = color.white)
        else:
            if (i == 1):
                buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)

    if (len(shared["player" + str(i) + "Discard"]) > 0):
        entry = bigTable[shared["player" + str(i) + "Discard"][0]]
        text = makeTooltipText(i, j, entry, "Discard", False)
        effectsLength = 0
        for k in range(len(entry["effects"])):
            effectsLength = effectsLength + len(entry["effects"][k])
        sizeFactor = effectsLength / 79.15
        if (i == 1):
            buttons["p" + str(i) + "discardButton"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.3 - sizeFactor,
                ignore = True, background = False, color = color.white)
        else:
            buttons["p" + str(i) + "discardButton"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -5.6 - sizeFactor,
                ignore = True, background = False, color = color.white)
    else:
        if (i == 1):
            buttons["p" + str(i) + "discardButton"] = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
        else:
            buttons["p" + str(i) + "discardButton"] = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)

def updateTooltips():
    for i in [1, 2]:
        for j in [1, 2, 3, 4, 5, 6]:
            if (j <= len(shared["player" + str(i) + "Hand"])):
                entry = bigTable[shared["player" + str(i) + "Hand"][j - 1]]
                text = makeTooltipText(i, j, entry, "Hand", False)
                effectsLength = 0
                for k in range(len(entry["effects"])):
                    effectsLength = effectsLength + len(entry["effects"][k])
                sizeFactor = effectsLength / 79.15
                if (i == 1):
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].enabled = True
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.world_x = -17.5
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.world_y = -2.3 - sizeFactor
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.wordwrap = 40
                else:
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].enabled = True
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.world_x = 5.5
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.world_y = -5.6 - sizeFactor
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.wordwrap = 40
            else:
                buttons["p" + str(i) + "hand" + str(j) + "Button"].enabled = False

        for j in [1, 2, 3, 4, 5]:
            if (j <= len(shared["player" + str(i) + "Comrades"])):
                entry = bigTable[shared["player" + str(i) + "Comrades"][str(j - 1)]["Name"]]
                text = makeTooltipText(i, j, entry, "Comrades", True)
                effectsLength = 0
                for k in range(len(entry["effects"])):
                    effectsLength = effectsLength + len(entry["effects"][k])
                sizeFactor = effectsLength / 79.15
                if (i == 1):
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.world_x = -17.5
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.world_y = -2.3 - sizeFactor
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.wordwrap = 40
                else:
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.world_x = 5.5
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.world_y = -5.6 - sizeFactor
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.wordwrap = 40
            else:
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.text = ""

        for j in [1, 2, 3]:
            if (j <= len(shared["player" + str(i) + "Auxiliaries"])):
                entry = bigTable[shared["player" + str(i) + "Auxiliaries"][str(j - 1)]["Name"]]
                text = makeTooltipText(i, j, entry, "Auxiliaries", True)
                effectsLength = 0
                for k in range(len(entry["effects"])):
                    effectsLength = effectsLength + len(entry["effects"][k])
                sizeFactor = effectsLength / 79.15
                if (i == 1):
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.world_x = -17.5
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.world_y = -2.3 - sizeFactor
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.wordwrap = 40
                else:
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.world_x = 5.5
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.world_y = -5.6 - sizeFactor
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.wordwrap = 40
            else:
                buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.text = ""

        if (len(shared["player" + str(i) + "Discard"]) > 0):
            entry = bigTable[shared["player" + str(i) + "Discard"][0]]
            text = makeTooltipText(i, 1, entry, "Discard", False)
            effectsLength = 0
            for k in range(len(entry["effects"])):
                effectsLength = effectsLength + len(entry["effects"][k])
            sizeFactor = effectsLength / 79.15
            if (i == 1):
                buttons["p" + str(i) + "discardButton"].enabled = True
                buttons["p" + str(i) + "discardButton"].tooltip.text = text
                buttons["p" + str(i) + "discardButton"].tooltip.world_x = -17.5
                buttons["p" + str(i) + "discardButton"].tooltip.world_y = -2.3 - sizeFactor
                buttons["p" + str(i) + "discardButton"].tooltip.wordwrap = 40
            else:
                buttons["p" + str(i) + "discardButton"].enabled = True
                buttons["p" + str(i) + "discardButton"].tooltip.text = text
                buttons["p" + str(i) + "discardButton"].tooltip.world_x = 5.5
                buttons["p" + str(i) + "discardButton"].tooltip.world_y = -5.6 - sizeFactor
                buttons["p" + str(i) + "discardButton"].tooltip.wordwrap = 40
        else:
            buttons["p" + str(i) + "discardButton"].enabled = False
            buttons["p" + str(i) + "discardButton"].tooltip.text = ""          