from ursina import *
import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

def myGlobals():
    return globals()

for i in [1, 2]:
    for j in [1, 2, 3, 4, 5, 6]:
        if (j <= len(shared["player" + str(i) + "Hand"])):
            if (i == 1):
                globals()["p" + str(i) + "hand" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.19 - (j / 10), -0.42))
            else:
                globals()["p" + str(i) + "hand" + str(j) + "Button"] = Button(scale = 0.08, position = (0.19 + (j / 10), -0.07))
        else:
            if (i == 1):
                globals()["p" + str(i) + "hand" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.19 - (j / 10), -0.42), enabled = False)
            else:
                globals()["p" + str(i) + "hand" + str(j) + "Button"] = Button(scale = 0.08, position = (0.19 + (j / 10), -0.07), enabled = False)         

    for j in [1, 2, 3, 4, 5]:
        if (j <= len(shared["player" + str(i) + "Comrades"])):
            if (i == 1):
                globals()["p" + str(i) + "comrade" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.3 + (j / 10), -0.3))
            else:
                globals()["p" + str(i) + "comrade" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.3 + (j / 10), -0.19))
        else:
            if (i == 1):
                globals()["p" + str(i) + "comrade" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.3 + (j / 10), -0.3))
            else:
                globals()["p" + str(i) + "comrade" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.3 + (j / 10), -0.19))

    for j in [1, 2, 3]:
        if (j <= len(shared["player" + str(i) + "Auxiliaries"])):
            if (i == 1):
                globals()["p" + str(i) + "auxiliary" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.3 + ((j + 1) / 10), -0.41))
            else:
                globals()["p" + str(i) + "auxiliary" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.3 + ((j + 1) / 10), -0.07))
        else:
            if (i == 1):
                globals()["p" + str(i) + "auxiliary" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.3 + ((j + 1) / 10), -0.41))
            else:
                globals()["p" + str(i) + "auxiliary" + str(j) + "Button"] = Button(scale = 0.08, position = (-0.3 + ((j + 1) / 10), -0.07))

    if (len(shared["player" + str(i) + "Discard"]) > 0):
        if (i == 1):
            globals()["p" + str(i) + "discardButton"] = Button(scale = 0.08, position = (-0.3 + 0.1, -0.41))
        else:
            globals()["p" + str(i) + "discardButton"] = Button(scale = 0.08, position = (-0.3 + 0.5, -0.07))
    else:
        if (i == 1):
            globals()["p" + str(i) + "discardButton"] = Button(scale = 0.08, position = (-0.3 + 0.1, -0.41), enabled = False)
        else:
            globals()["p" + str(i) + "discardButton"] = Button(scale = 0.08, position = (-0.3 + 0.5, -0.07), enabled = False)
            
def updateButtons():
    for i in [1, 2]:
        for j in [1, 2, 3, 4, 5, 6]:
            if (j <= len(shared["player" + str(i) + "Hand"])):
                globals()["p" + str(i) + "hand" + str(j) + "Button"].enabled = True
            else:
                globals()["p" + str(i) + "hand" + str(j) + "Button"].enabled = False

        if (len(shared["player" + str(i) + "Discard"]) > 0):
            globals()["p" + str(i) + "discardButton"].enabled = True  
        else:
            globals()["p" + str(i) + "discardButton"].enabled = False        