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

p = WindowPanel(title = "", text = "     CARD GAMES          By" + "\n" + "ON MOTORCYCLES   OEA", text_color = color.magenta, position = (0, 0.025, 0))

def input(key):
    global p
    if (key == "enter"):
        p.enabled = False
    if (key == "escape"):
        application.quit()
    racing.racingInput(key)
    cards.cardsInput(key)

app.run()