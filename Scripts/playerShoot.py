import bge
from collections import OrderedDict

class Shoot(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.scene = bge.logic.getCurrentScene()
        self.mouse = bge.logic.mouse.inputs
        self.tiro = False
        pass

    def update(self):
        LEFTMOUSE = self.mouse[bge.events.LEFTMOUSE].activated
        player = self.scene.objects.get("obj_player")
        shoot = self.scene.objects.get("empty_shootRotation")
        if LEFTMOUSE:
            shoot = self.scene.addObject("empty_shootRotation", self.object, 0)
            self.tiro = True
        
        if player and self.tiro and shoot:
            print(shoot.name, player.name)
            if shoot.children[0].collide(player) < 1:
                shoot.endObject()
                print("apaga")
        pass
