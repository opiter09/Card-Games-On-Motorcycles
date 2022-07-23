maintenanceString = "At the beginning of your Maintenance Phase"
eitherMaintenanceString = "At the beginning of each player's Maintenance Phase"

from ursina import *

from cardCode.bigCardTable import bigTable

import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

def maintenanceTriggers(playerIndex):
    global shared
    global bigTable

    for i in [1, 2]:
        for j in [1, 2, 3, 4, 5]:
            if (len(shared["player" + str(i) + "Comrades"][str(j)]) > 0):
                entry = bigTable[shared["player" + str(i) + "Comrades"][str(j)]["Name"]]
                effectsList = []
                for k in range(len(entry["effects"])):
                    if (entry["effects"][k].startswith(eitherMaintenanceString) == True):
                        theTable = { "section": "Comrades", "position": j, "player": i, "effect": k, "target": {} }
                        shared["theStack"].insert(10000, theTable)
                    elif (entry["effects"][k].startswith(maintenanceString) == True):
                        if (shared["player" + str(playerIndex) + "Phase"] == "Maintenance"):
                            theTable = { "section": "Comrades", "position": j, "player": i, "effect": k, "target": {} }
                            shared["theStack"].insert(10000, theTable)
                    
        for j in [1, 2, 3]:
            if (len(shared["player" + str(i) + "Auxiliaries"][str(j)]) > 0):
                entry = bigTable[shared["player" + str(i) + "Auxiliaries"][str(j)]["Name"]]
                effectsList = []
                for k in range(len(entry["effects"])):
                    if (entry["effects"][k].startswith(eitherMaintenanceString) == True):
                        theTable = { "section": "Auxiliaries", "position": j, "player": i, "effect": k, "target": {} }
                        shared["theStack"].insert(10000, theTable)
                    elif (entry["effects"][k].startswith(maintenanceString) == True):
                        if (shared["player" + str(playerIndex) + "Phase"] == "Maintenance"):
                            theTable = { "section": "Auxiliaries", "position": j, "player": i, "effect": k, "target": {} }
                            shared["theStack"].insert(10000, theTable)
                    
        if (len(shared["player" + str(i) + "Discard"]) > 0):
            entry = bigTable[shared["player" + str(i) + "Discard"][0]]
            effectsList = []
            for k in range(len(entry["effects"])):
                if (entry["effects"][k].startswith(eitherMaintenanceString) == True):
                    theTable = { "section": "Discard", "position": j, "player": i, "effect": k, "target": {} }
                    shared["theStack"].insert(10000, theTable)
                elif (entry["effects"][k].startswith(maintenanceString) == True):
                    if (shared["player" + str(playerIndex) + "Phase"] == "Maintenance"):
                        theTable = { "section": "Discard", "position": j, "player": i, "effect": k, "target": {} }
                        shared["theStack"].insert(10000, theTable)
                        
    shared["resolveNow"] = 1
    if (playerIndex == 1):
        shared["player1Active"] = False
        shared["player2Active"] = True
    else:
        shared["player1Active"] = True
        shared["player2Active"] = False
                            
                        
        