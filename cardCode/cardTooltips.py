from ursina import *
from cardCode.bigCardTable import bigTable
import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

for i in [1, 2]:
    for j in [1, 2, 3, 4, 5, 6]:
        if (j <= len(shared["player" + str(i) + "Hand"])):
            entry = bigTable[shared["player" + str(i) + "Hand"][j - 1]]
            text = shared["player" + str(i) + "Hand"][j - 1] + "     " + entry["cost"] + "\n"
            if (entry["type"] == "Comrade"):
                text = text + "Strength: " + str(entry["strength"]) + "  Vitality: " + str(entry["vitality"]) + "\n"
            text = text + entry["type"]
            if (entry["type"] == "Comrade"):
                text = text + "~" + entry["subType"]
            effectsLength = 0
            for k in range(len(entry["effects"])):
                text = text + "\n" + entry["effects"][k]
                effectsLength = effectsLength + len(entry["effects"][k])
            if (i == 1):
                sizeFactor = effectsLength / 79.15
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.19 - (j / 10), -0.42))
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.3 - sizeFactor,
                    ignore = True, background = False, color = color.white)
            else:
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (0.19 + (j / 10), -0.07))
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -5.6 - sizeFactor,
                    ignore = True, background = False, color = color.white)
        else:
            if (i == 1):
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.19 - (j / 10), -0.42), enabled = False)
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
            else:
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (0.19 + (j / 10), -0.07), enabled = False)
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)           

    for j in [1, 2, 3, 4, 5]:
        if (j <= len(shared["player" + str(i) + "Comrades"])):
            entry = bigTable[shared["player" + str(i) + "Comrades"][str(j - 1)]["Name"]]
            text = shared["player" + str(i) + "Comrades"][str(j - 1)]["Name"] + "     " + entry["cost"] + "\n"
            if (entry["type"] == "Comrade"):
                text = text + "Strength: " + str(entry["strength"]) + "  Vitality: " + str(entry["vitality"]) + "\n"
            text = text + entry["type"]
            if (entry["type"] == "Comrade"):
                text = text + "~" + entry["subType"]
            effectsLength = 0
            for k in range(len(entry["effects"])):
                text = text + "\n" + entry["effects"][k]
                effectsLength = effectsLength + len(entry["effects"][k])
            if (i == 1):
                sizeFactor = effectsLength / 79.15
                globals()["p" + str(i) + "comrade" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.3 + (j / 10), -0.3))
                globals()["p" + str(i) + "comrade" + str(j) + "Tooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.3 - sizeFactor,
                    ignore = True, background = False, color = color.white)
            else:
                globals()["p" + str(i) + "comrade" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.3 + (j / 10), -0.19))
                globals()["p" + str(i) + "comrade" + str(j) + "Tooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -5.6 - sizeFactor,
                    ignore = True, background = False, color = color.white)
        else:
            if (i == 1):
                globals()["p" + str(i) + "comrade" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.3 + (j / 10), -0.3), enabled = False)
                globals()["p" + str(i) + "comrade" + str(j) + "Tooltip"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
            else:
                globals()["p" + str(i) + "comrade" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.3 + (j / 10), -0.19), enabled = False)
                globals()["p" + str(i) + "comrade" + str(j) + "Tooltip"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)

    for j in [1, 2, 3]:
        if (j <= len(shared["player" + str(i) + "Auxiliaries"])):
            entry = bigTable[shared["player" + str(i) + "Auxiliaries"][str(j - 1)]["Name"]]
            text = shared["player" + str(i) + "Auxiliaries"][str(j - 1)]["Name"] + "     " + entry["cost"] + "\n"
            if (entry["type"] == "Comrade"):
                text = text + "Strength: " + str(entry["strength"]) + "  Vitality: " + str(entry["vitality"]) + "\n"
            text = text + entry["type"]
            if (entry["type"] == "Comrade"):
                text = text + "~" + entry["subType"]
            effectsLength = 0
            for k in range(len(entry["effects"])):
                text = text + "\n" + entry["effects"][k]
                effectsLength = effectsLength + len(entry["effects"][k])
            if (i == 1):
                sizeFactor = effectsLength / 79.15
                globals()["p" + str(i) + "auxiliary" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.3 + ((j + 1) / 10), -0.41))
                globals()["p" + str(i) + "auxiliary" + str(j) + "Tooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.3 - sizeFactor,
                    ignore = True, background = False, color = color.white)
            else:
                globals()["p" + str(i) + "auxiliary" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.3 + ((j + 1) / 10), -0.07))
                globals()["p" + str(i) + "auxiliary" + str(j) + "Tooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -5.6 - sizeFactor,
                    ignore = True, background = False, color = color.white)
        else:
            if (i == 1):
                globals()["p" + str(i) + "auxiliary" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.3 + ((j + 1) / 10), -0.41), enabled = False)
                globals()["p" + str(i) + "auxiliary" + str(j) + "Tooltip"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
            else:
                globals()["p" + str(i) + "auxiliary" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.3 + ((j + 1) / 10), -0.07), enabled = False)
                globals()["p" + str(i) + "auxiliary" + str(j) + "Tooltip"].tooltip = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)

    if (len(shared["player" + str(i) + "Discard"]) > 0):
        entry = bigTable[shared["player" + str(i) + "Discard"][0]]
        text = shared["player" + str(i) + "Discard"][0] + "     " + entry["cost"] + "\n"
        if (entry["type"] == "Comrade"):
            text = text + "Strength: " + str(entry["strength"]) + "  Vitality: " + str(entry["vitality"]) + "\n"
        text = text + entry["type"]
        if (entry["type"] == "Comrade"):
            text = text + "~" + entry["subType"]
        effectsLength = 0
        for k in range(len(entry["effects"])):
            text = text + "\n" + entry["effects"][k]
            effectsLength = effectsLength + len(entry["effects"][k])
        if (i == 1):
            sizeFactor = effectsLength / 79.15
            globals()["p" + str(i) + "discardTooltip"] = Button(scale = 0.08, position = (-0.3 + 0.1, -0.41))
            globals()["p" + str(i) + "discardTooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.3 - sizeFactor,
                ignore = True, background = False, color = color.white)
        else:
            globals()["p" + str(i) + "discardTooltip"] = Button(scale = 0.08, position = (-0.3 + 0.5, -0.07))
            globals()["p" + str(i) + "discardTooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -5.6 - sizeFactor,
                ignore = True, background = False, color = color.white)
    else:
        if (i == 1):
            globals()["p" + str(i) + "discardTooltip"] = Button(scale = 0.08, position = (-0.3 + 0.1, -0.41), enabled = False)
            globals()["p" + str(i) + "discardTooltip"] = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)
        else:
            globals()["p" + str(i) + "discardTooltip"] = Button(scale = 0.08, position = (-0.3 + 0.5, -0.07), enabled = False)
            globals()["p" + str(i) + "discardTooltip"] = Tooltip("", scale = 0.95, ignore = True, background = False, color = color.white)        