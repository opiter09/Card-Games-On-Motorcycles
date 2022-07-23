from ursina import *

import cardCode.sahredVariables as sharedVariables
shared = sharedVariables.myGlobals()

import cardCode.cardParser as cardParser
from cardCode.bigCardTable import bigTable

def emptyTheStack():
    global bigTable
    global shared

    if (len(shared["theStack"]) == 0):
        shared["resolveNow"] = 0
        return
        
    if (len(shared["theStack"][-1]["target"]) == 0):
        if (len(shared["currentTargetConditions"]) == 0):
            shared["currentTargetConditions"] = cardParser.targetConditions(shared["theStack"][-1])
        return