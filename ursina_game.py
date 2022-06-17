from ursina import *
from ursina.shaders import lit_with_shadows_shader

app = Ursina()
cycle = Entity(model = "motorcycle/motor", rotation = (0, 90, 0))
cycle2 = Entity(model = "motorcycle/motorBlue", position = (10, 0, 0))
start = Entity(model = "racing/roadStart", position = (0, -2.25, 0), scale = 10)
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, 1))
Sky()

def update():   # update gets automatically called.
    cycle.rotation_y += held_keys["d"]
    cycle.rotation_y -= held_keys["a"]
    cycle.setX(cycle, held_keys["w"] * -0.1)
    cycle.setX(cycle, held_keys["s"] * 0.1)
    
def input(key):
    if (key == "escape"):
        application.quit()

#for i in range(6)

base.disableMouse()

def createCamera(self, dispRegion):
    theCamera = base.makeCamera(base.win, displayRegion = dispRegion)
    theCamera.node().getLens().setAspectRatio(3.0/4.0)
    theCamera.setPos(0, 0, -10)
    return theCamera

base.camera1 = createCamera(base, (0.5, 1.0, 0, 1))
base.camera1.reparentTo(cycle)
base.camera1.lookAt(cycle)
base.camera1.setPos(15, 2, 0)
base.camera1.setHpr(90, 0, 0)

base.camera2 = createCamera(base, (0.0, 0.5, 0, 1))
base.camera2.reparentTo(cycle2)
base.camera2.lookAt(cycle2)
base.camera2.setPos(15, 2, 0)
base.camera2.setHpr(90, 0, 0)
        
base.camNode.setActive(False)

app.run()