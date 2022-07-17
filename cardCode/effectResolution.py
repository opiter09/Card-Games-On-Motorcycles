from ursina import *

import cardCode.sahredVariables as sharedVariables
shared = sharedVariables.myGlobals()

from cardCode.bigCardTable import bigTable

def emptyTheStack():
    global bigTable
    global shared

    if (len(shared["theStack"]) == 0):
        shared["resolveNow"] = 0
        return
        
    for i in range(len(shared["theStack"])):
        pass