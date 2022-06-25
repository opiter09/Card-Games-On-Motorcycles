from ursina import *
from cardCode.bigCardTable import bigTable
import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

for i in [1, 2]:
    for j in [1, 2, 3, 4, 5, 6]:
        if (j <= len(shared["player" + str(i) + "Hand"])):
            entry = bigTable[shared["player" + str(i) + "Hand"][j - 1]]
            text = shared["player" + str(i) + "Hand"][j - 1] + "     " + entry["cost"] + "\n" + entry["type"]
            if (entry["type"] == "Comrade"):
                text = text + "~" + entry["subType"]
            for k in range(len(entry["effects"])):
                text = text + "\n" + entry["effects"][k]

            if (i == 1):
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (-0.19 - (j / 10), -0.42))
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"].tooltip = Tooltip(text, origin = (4.5, 0.55), ignore = True, background = False)
            else:
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"] = Button(scale = 0.08, position = (0.19 + (j / 10), -0.07))
                globals()["p" + str(i) + "hand" + str(j) + "Tooltip"].tooltip = Tooltip(text, origin = (-2.3, 1.1), ignore = True, background = False)            