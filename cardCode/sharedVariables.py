import json
import numpy
import random

f = open("player1.txt")
player1Deck = json.load(f)
f.close()
player1Deck = numpy.array(list(player1Deck.values()))
random.shuffle(player1Deck)
player1Hand = player1Deck[0:4]
player1Deck = player1Deck[4:40]

f = open("player2.txt")
player2Deck = json.load(f)
f.close()
player2Deck = numpy.array(list(player2Deck.values()))
random.shuffle(player2Deck)
player2Hand = player2Deck[0:4]
player2Deck = player2Deck[4:40]

player1Comrades = player2Comrades = {
    "0": {"Name": "Killer Clown", "Contracted": "True"},
    "1": {"Name": "Killer Clown", "Contracted": "True"},
    "2": {"Name": "Killer Clown", "Contracted": "True"},
    "3": {"Name": "Killer Clown", "Contracted": "True"},
    "4": {"Name": "Killer Clown", "Contracted": "True"},}
player1Auxiliaries = player2Auxiliaries = []
player1Discard = player2Discard = []

player1Life = 15
player2Life = 15

player1Stone = player1Plant = player1Metal = player1Animal = player1Cosmic = 0
player2Stone = player2Plant = player2Metal = player2Animal = player2Cosmic = 0

def myGlobals():
    return globals()