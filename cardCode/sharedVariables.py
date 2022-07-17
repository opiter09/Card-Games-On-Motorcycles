import json
import random

def myGlobals():
    return globals()

player1Phase = ""
player2Phase = ""
firstPlayer = round(random.randint(500, 1000) / 500)
if (firstPlayer == 1):
    player1Phase = "Relaxation"
    player2Phase = "NotMe"
else:
    player1Phase = "NotMe"
    player2Phase = "Relaxation"
turnCount = 0

f = open("player1Deck.json")
p1Deck = json.load(f)
f.close()
player1OriginalDeck = list(p1Deck.values())
player1Deck = player1OriginalDeck
random.shuffle(player1Deck)
player1Hand = player1Deck[0:4]
player1Deck = player1Deck[4:40]

f = open("player2Deck.json")
p2Deck = json.load(f)
f.close()
player2OriginalDeck = list(p2Deck.values())
player2Deck = player2OriginalDeck
random.shuffle(player2Deck)
player2Hand = player2Deck[0:4]
player2Deck = player2Deck[4:40]

player1Comrades = {
    "0": {"Name": "Wheel Runner", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "TempStrengthChange": -1, "TempVitalityChange": -1, "Counters": {}},
    "1": {"Name": "Killer Clown", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "TempStrengthChange": -1, "TempVitalityChange": -1, "Counters": {}},
    "2": {"Name": "Killer Clown", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "TempStrengthChange": -1, "TempVitalityChange": -1, "Counters": {}},
    "3": {},
    "4": {"Name": "Killer Clown", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "TempStrengthChange": -1, "TempVitalityChange": -1, "Counters": {}},
    "5": {}
}
player2Comrades = {
    "0": {"Name": "Wheel Runner", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "TempStrengthChange": -1, "TempVitalityChange": -1, "Counters": {}},
    "1": {"Name": "Killer Clown", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "TempStrengthChange": -1, "TempVitalityChange": -1, "Counters": {}},
    "2": {"Name": "Killer Clown", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "TempStrengthChange": -1, "TempVitalityChange": -1, "Counters": {}},
    "3": {},
    "4": {"Name": "Killer Clown", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "TempStrengthChange": -1, "TempVitalityChange": -1, "Counters": {}},
    "5": {}
}

player1Auxiliaries = {
    "0": {"Name": "Forest Fire", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}},
    "1": {"Name": "Trebuchet", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}},
    "2": {}
}
player2Auxiliaries = {
    "0": {"Name": "Forest Fire", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}},
    "1": {"Name": "Trebuchet", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}},
    "2": {}
}

player1Discard = [ "Killer Clown" ]
player2Discard = [ "Killer Clown" ]

player1Life = 15
player2Life = 15

player1Stone = player1Plant = player1Metal = player1Animal = player1Cosmic = 0
player2Stone = player2Plant = player2Metal = player2Animal = player2Cosmic = 0

player1CurrentStone = player1CurrentPlant = player1CurrentMetal = player1CurrentAnimal = player1CurrentCosmic = 0
player2CurrentStone = player2CurrentPlant = player2CurrentMetal = player2CurrentAnimal = player2CurrentCosmic = 0

player1Acting = False
player2Acting = False
resolveNow = 0

theStack = []