maintenanceString = "At the beginning of your Maintenance Phase"
eitherMaintenanceString = "At the beginning of each player's Maintenance Phase"

from ursina import *

import cardCode.sharedVariables as sharedVariables
shared = sharedVariables.myGlobals()

def maintenanceTriggers(playerIndex):
    global shared

    for i in [1, 2]:
        for j in [1, 2, 3, 4, 5]:
            
        