import bge
from collections import OrderedDict

class Shoot(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.scene = bge.logic.getCurrentScene()
        self.mouse = bge.logic.mouse.inputs
        pass

    def update(self):
        LEFTMOUSE = self.mouse[bge.events.LEFTMOUSE].activated
        player = self.scene.objects.get("obj_player")
        shoot = self.scene.objects.get("empty_shootRotation")
        if LEFTMOUSE:
            shoot = self.scene.addObject("empty_shootRotation", self.object)
        pass
