import json
import numpy
import random

f = open("player1.txt")
player1Deck = json.load(f)
f.close()
player1Deck = numpy.array(list(player1Deck.values()))
random.shuffle(player1Deck)

f = open("player2.txt")
player2Deck = json.load(f)
f.close()
player2Deck = numpy.array(list(player2Deck.values()))
#print(player2Deck[0])
random.shuffle(player2Deck)

p1Life = 15
p2Life = 15

p1Stone = p1Plant = p1Metal = p1Animal = p1Extraterrestrial = 0
p2Stone = p2Plant = p2Metal = p2Animal = p2Extraterrestrial = 0