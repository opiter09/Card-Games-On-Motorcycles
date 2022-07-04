strengthString = "Strength"
vitalityString = "Vitality"

from ursina import *
from cardCode.bigCardTable import bigTable

import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

import cardCode.cardButtons as cardButtons
buttons = cardButtons.myGlobals()

breaksNumber = 0
def makeTooltipText(i, j, entry, theString, change):
    if (change == True):
        text = shared["player" + str(i) + theString][str(j - 1)]["Name"] + "     " + entry["cost"] + "\n"
    else:
        if (j > len(shared["player" + str(i) + theString])):
            return ""
        text = shared["player" + str(i) + theString][j - 1] + "     " + entry["cost"] + "\n"

    if (entry["type"] == "Comrade"):
        if (change == False):
            text = text + globals()["strengthString"] + ": " + str(entry["strength"]) + "  " + globals()["vitalityString"] + ": " + str(entry["vitality"]) + "\n"
        else:
            totalStrengthChange = shared["player" + str(i) + theString][str(j - 1)]["StrengthChange"] + shared["player" + str(i) + theString][str(j - 1)]["TempStrengthChange"]
            totalVitalityChange = shared["player" + str(i) + theString][str(j - 1)]["VitalityChange"] + shared["player" + str(i) + theString][str(j - 1)]["TempVitalityChange"]
            text = text + globals()["strengthString"] + ": " + str(entry["strength"]) + " + " + str(totalStrengthChange)
            text = text + "  " + globals()["vitalityString"] + ": " + str(entry["vitality"]) + " + " + str(totalVitalityChange) + "\n"
    else:
        text = text + globals()["strengthString"] + ": " + "N/A" + "  " + globals()["vitalityString"] + ": " + "N/A" + "\n"

    if (change == True):
        globals()["breaksNumber"] = len(shared["player" + str(i) + theString][str(j - 1)]["Counters"])
        for key in shared["player" + str(i) + theString][str(j - 1)]["Counters"]:
            text = text + key + ": " + str(shared["player" + str(i) + theString][str(j - 1)]["Counters"][key]) + "\n"
    else:
        globals()["breaksNumber"] = 0
    globals()["breaksNumber"] = globals()["breaksNumber"] + (max(0, len(entry["effects"]) - 1) / 2.5)

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
            sizeFactor = (effectsLength / 90) + (globals()["breaksNumber"] / 2)
            if (i == 1):
                buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.7 - sizeFactor,
                    ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -6.1 - sizeFactor,
                    ignore = True, background = False, color = color.white)
        else:
            if (i == 1):
                buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)           

    for j in [1, 2, 3, 4, 5]:
        if (len(shared["player" + str(i) + "Comrades"][str(j - 1)]) > 0):
            entry = bigTable[shared["player" + str(i) + "Comrades"][str(j - 1)]["Name"]]
            text = makeTooltipText(i, j, entry, "Comrades", True)
            effectsLength = 0
            for k in range(len(entry["effects"])):
                effectsLength = effectsLength + len(entry["effects"][k])
            sizeFactor = (effectsLength / 90) + (globals()["breaksNumber"] / 2)
            if (i == 1):
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.7 - sizeFactor,
                    ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -6.1 - sizeFactor,
                    ignore = True, background = False, color = color.white)
        else:
            if (i == 1):
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)

    for j in [1, 2, 3]:
        if (len(shared["player" + str(i) + "Auxiliaries"][str(j - 1)]) > 0):
            entry = bigTable[shared["player" + str(i) + "Auxiliaries"][str(j - 1)]["Name"]]
            text = makeTooltipText(i, j, entry, "Auxiliaries", True)
            effectsLength = 0
            for k in range(len(entry["effects"])):
                effectsLength = effectsLength + len(entry["effects"][k])
            sizeFactor = (effectsLength / 90) + (globals()["breaksNumber"] / 2)
            if (i == 1):
                buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.7 - sizeFactor,
                    ignore = True, background = False, color = color.white)
            else:
                buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -6.1 - sizeFactor,
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
        sizeFactor = (effectsLength / 90) + (globals()["breaksNumber"] / 2)
        if (i == 1):
            buttons["p" + str(i) + "discardButton"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.7 - sizeFactor,
                ignore = True, background = False, color = color.white)
        else:
            buttons["p" + str(i) + "discardButton"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -6.1 - sizeFactor,
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
                sizeFactor = (effectsLength / 90) + (globals()["breaksNumber"] / 2)
                if (i == 1):
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.world_x = -17.5
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.world_y = -2.7 - sizeFactor
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.wordwrap = 40
                else:
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.world_x = 5.5
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.world_y = -6.1 - sizeFactor
                    buttons["p" + str(i) + "hand" + str(j) + "Button"].tooltip.wordwrap = 40

        for j in [1, 2, 3, 4, 5]:
            if (len(shared["player" + str(i) + "Comrades"][str(j - 1)]) > 0):
                entry = bigTable[shared["player" + str(i) + "Comrades"][str(j - 1)]["Name"]]
                text = makeTooltipText(i, j, entry, "Comrades", True)
                effectsLength = 0
                for k in range(len(entry["effects"])):
                    effectsLength = effectsLength + len(entry["effects"][k])
                sizeFactor = (effectsLength / 90) + (globals()["breaksNumber"] / 2)
                if (i == 1):
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.world_x = -17.5
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.world_y = -2.7 - sizeFactor
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.wordwrap = 40
                else:
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.world_x = 5.5
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.world_y = -6.1 - sizeFactor
                    buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.wordwrap = 40
            else:
                buttons["p" + str(i) + "comrade" + str(j) + "Button"].tooltip.text = ""

        for j in [1, 2, 3]:
            if (len(shared["player" + str(i) + "Auxiliaries"][str(j - 1)]) > 0):
                entry = bigTable[shared["player" + str(i) + "Auxiliaries"][str(j - 1)]["Name"]]
                text = makeTooltipText(i, j, entry, "Auxiliaries", True)
                effectsLength = 0
                for k in range(len(entry["effects"])):
                    effectsLength = effectsLength + len(entry["effects"][k])
                sizeFactor = (effectsLength / 90) + (globals()["breaksNumber"] / 2)
                if (i == 1):
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.world_x = -17.5
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.world_y = -2.7 - sizeFactor
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.wordwrap = 40
                else:
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.text = text
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.world_x = 5.5
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.world_y = -6.1 - sizeFactor
                    buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.wordwrap = 40
            else:
                buttons["p" + str(i) + "auxiliary" + str(j) + "Button"].tooltip.text = ""

        if (len(shared["player" + str(i) + "Discard"]) > 0):
            entry = bigTable[shared["player" + str(i) + "Discard"][0]]
            text = makeTooltipText(i, 1, entry, "Discard", False)
            effectsLength = 0
            for k in range(len(entry["effects"])):
                effectsLength = effectsLength + len(entry["effects"][k])
            sizeFactor = (effectsLength / 90) + (globals()["breaksNumber"] / 2)
            if (i == 1):
                buttons["p" + str(i) + "discardButton"].tooltip.text = text
                buttons["p" + str(i) + "discardButton"].tooltip.world_x = -17.5
                buttons["p" + str(i) + "discardButton"].tooltip.world_y = -2.7 - sizeFactor
                buttons["p" + str(i) + "discardButton"].tooltip.wordwrap = 40
            else:
                buttons["p" + str(i) + "discardButton"].tooltip.text = text
                buttons["p" + str(i) + "discardButton"].tooltip.world_x = 5.5
                buttons["p" + str(i) + "discardButton"].tooltip.world_y = -6.1 - sizeFactor
                buttons["p" + str(i) + "discardButton"].tooltip.wordwrap = 40        