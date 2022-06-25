from ursina import *
from cardCode.bigCardTable import bigTable
import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

for i in [1, 2]:
    for j in [1, 2, 3, 4, 5, 6]:
        if (j <= len(shared["player" + str(i) + "Hand"])):
            entry = bigTable[shared["player" + str(i) + "Hand"][j - 1]]
            text = shared["player" + str(i) + "Hand"][j - 1] + "     " + entry["cost"] + "\n"
            text = text + "Strength: " + str(entry["strength"]) + "  Vitality: " + str(entry["vitality"])
            text = text + "\n" + entry["type"]
            if (entry["type"] == "Comrade"):
                text = text + "~" + entry["subType"]
            effectsLength = 0
            for k in range(len(entry["effects"])):
                text = text + "\n" + entry["effects"][k]
                effectsLength = effectsLength + len(entry["effects"][k])
            if (i == 1):
                sizeFactor = effectsLength / 79.15
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.19 - (j / 10), -0.42))
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = -17.5, world_y = -2.3 - sizeFactor, ignore = True, background = False)
            else:
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (0.19 + (j / 10), -0.07))
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"].tooltip = Tooltip(text, scale = 0.95, world_x = 5.5, world_y = -5.6 - sizeFactor, ignore = True, background = False)            