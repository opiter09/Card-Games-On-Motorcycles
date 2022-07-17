tokenText = "Token"

from ursina import *
from cardCode.bigCardTable import bigTable
import configparser

def shareCartDeck(direction):
    global tokenText
    config = configparser.ConfigParser()
    config.read("../o_o.ini")

    global bigTable
    cardNames = []
    for k in list(bigTable.cardNames()):
        cardNames.insert(10000, bigTable[k]["Name"])
    theList = []
    
    if (direction == "normal"):
        for item in config["Main"].cardNames():
            if (item.lower().startswith("switch") == False) and (item.lower() != "playername"):
                bytE = int(config["Main"][item]).to_bytes(2, "big")
                partOne = cardNames[bytE[0]]
                if (partOne.endswith(tokenText) == True):
                    partOne = cardNames[bytE[0] + 1]
                partTwo = cardNames[bytE[1]]
                if (partTwo.endswith(tokenText) == True):
                    partTwo = cardNames[bytE[1] + 1]                
                theList.insert(10000, partOne)
                theList.insert(10000, partOne)
                theList.insert(10000, partTwo)
                theList.insert(10000, partTwo)
            elif (item.lower() == "playername"):
                theString = item
                while (len(theString) < 7):
                    if (len(theString) == 0):
                        theString = "TheVoid"
                    else:
                        theString = theString + theString.swapcase()
                theString = theString[0:7]
                for i in range(7):
                    name = cardNames[int.from_bytes(theString[i].encode("utf-8"), "big")]
                    if (name.endswith(tokenText) == True):
                        name = cardNames[int.from_bytes(theString[i].encode("utf-8"), "big") + 1]
                    theList.insert(10000, name)
                    theList.insert(10000, name)
            elif (item.lower() == "switch0"):
                bits = []
                for i in range(8):
                    if (config.getboolean("Main", "Switch" + str(i)) == True):
                        bits.insert(10000, 1)
                    else:
                        bits.insert(10000, 0)
                oneByte = sum(b * 2 ** x for b, x in zip(bits[::-1], range(len(bits))))
                name = cardNames[oneByte]
                if (name.endswith(tokenText) == True):
                    name = cardNames[oneByte + 1]
                theList.insert(10000, name)
                theList.insert(10000, name)
    elif (direction == "reverse"):
        for item in config["Main"].cardNames():
            if (item.lower().startswith("switch") == False) and (item.lower() != "playername"):
                bytE = int(config["Main"][item]).to_bytes(2, "big")
                partOne = cardNames[bytE[0] ^ ((2 ** 8) - 1)]
                if (partOne.endswith(tokenText) == True):
                    partOne = cardNames[(bytE[0] ^ ((2 ** 8) - 1)) + 1]
                partTwo = cardNames[bytE[1] ^ ((2 ** 8) - 1)]
                if (partTwo.endswith(tokenText) == True):
                    partTwo = cardNames[(bytE[1] ^ ((2 ** 8) - 1)) + 1]   
                theList.insert(10000, partOne)
                theList.insert(10000, partOne)
                theList.insert(10000, partTwo)
                theList.insert(10000, partTwo)
            elif (item.lower() == "playername"):
                theString = item
                while (len(theString) < 7):
                    if (len(theString) == 0):
                        theString = "TheVoid"
                    else:
                        theString = theString + theString.swapcase()
                theString = theString[0:7]
                for i in range(7):
                    name = cardNames[int.from_bytes(theString[i].encode("utf-8"), "big") ^ ((2 ** 8) - 1)]
                    if (name.endswith(tokenText) == True):
                        name = cardNames[(int.from_bytes(theString[i].encode("utf-8"), "big") ^ ((2 ** 8) - 1)) + 1]
                    theList.insert(10000, name)
                    theList.insert(10000, name)
            elif (item.lower() == "switch0"):
                bits = []
                for i in range(8):
                    if (config.getboolean("Main", "Switch" + str(i)) == True):
                        bits.insert(10000, 0)
                    else:
                        bits.insert(10000, 1)
                oneByte = sum(b * 2 ** x for b, x in zip(bits[::-1], range(len(bits))))
                name = cardNames[oneByte]
                if (name.endswith(tokenText) == True):
                    name = cardNames[oneByte + 1]
                theList.insert(10000, name)
                theList.insert(10000, name)
    return theList