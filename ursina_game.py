from ursina import *

app = Ursina()
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, 1))
Sky()
base.disableMouse()
base.camNode.setActive(False)

import racingCode.racing as racing
import cardCode.cards as cards

def update():   # update gets automatically called.
    racing.racingUpdate()
    cards.cardsUpdate()

def input(key):
    if (key == "escape"):
        application.quit()
    racing.racingInput(key)
    cards.cardsInput(key)

app.run()