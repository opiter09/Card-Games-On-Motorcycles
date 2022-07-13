def drawCards(number, playerIndex):
    for t in range(number):
        if (len(shared["player" + str(playerIndex) + "Hand"]) == 6):
            shared["player" + str(playerIndex) + "Discard"].insert(0, shared["player" + str(playerIndex) + "Hand"][0])
            shared["player" + str(playerIndex) + "Hand"] = shared["player" + str(playerIndex) + "Hand"][1:6]
        if (len(shared["player" + str(playerIndex) + "Deck"]) == 0):
            shared["player" + str(playerIndex) + "Life"] = 0
        shared["player" + str(playerIndex) + "Hand"].insert(7, shared["player" + str(playerIndex) + "Deck"][0])
        shared["player" + str(playerIndex) + "Deck"].pop(0)