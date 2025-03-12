import bge
from random import randint
from collections import OrderedDict

class Enemy(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        pass
    
    def movement(self):
        if self.object["move"] == 1:
            self.object.applyRotation([-0.003,0, 0.01], True)
        elif self.object["move"] == 2:
            self.object.applyRotation([-0.003, 0,0], True)
        elif self.object["move"] == 3:
            self.object.applyRotation([-0.003,0, -0.01],True)
        else:
            None
        pass
      
    def update(self):
        self.movement()
        pass
