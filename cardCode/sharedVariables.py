import json
import random

player1Phase = ""
player2Phase = ""
firstPlayer = round(random.randint(500, 1000) / 500)
if (firstPlayer == 1):
    player1Phase = "Relaxation"
    player2Phase = "NotMe"
else:
    player1Phase = "NotMe"
    player2Phase = "Relaxation"

f = open("player1Deck.json")
player1Deck = json.load(f)
f.close()
player1Deck = player1OriginalDeck = list(player1Deck.values())
random.shuffle(player1Deck)
player1Hand = player1Deck[0:4]
player1Deck = player1Deck[4:40]

f = open("player2Deck.json")
player2Deck = json.load(f)
f.close()
player2Deck = player2OriginalDeck = list(player2Deck.values())
random.shuffle(player2Deck)
player2Hand = player2Deck[0:4]
player2Deck = player2Deck[4:40]

player1Comrades = player2Comrades = {
    "0": {"Name": "Wheel Runner", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}},
    "1": {"Name": "Killer Clown", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}},
    "2": {"Name": "Killer Clown", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}},
    "3": {"Name": "Killer Clown", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}}
}
player1Auxiliaries = player2Auxiliaries = {
    "0": {"Name": "Forest Fire", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}},
    "1": {"Name": "Trebuchet", "Contracted": "True", "StrengthChange": -1, "VitalityChange": -1, "Counters": {}}
}
player1Discard = player2Discard = ["Killer Clown"]

player1Life = 15
player2Life = 15

player1Stone = player1Plant = player1Metal = player1Animal = player1Cosmic = 0
player2Stone = player2Plant = player2Metal = player2Animal = player2Cosmic = 0

player1CurrentStone = player1CurrentPlant = player1CurrentMetal = player1CurrentAnimal = player1CurrentCosmic = 0
player2CurrentStone = player2CurrentPlant = player2CurrentMetal = player2CurrentAnimal = player2CurrentCosmic = 0

def myGlobals():
    return globals()