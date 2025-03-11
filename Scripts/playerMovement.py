import bge
from mathutils import Vector
from collections import OrderedDict

class Movement(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.keyboard = bge.logic.keyboard.inputs
        pass

    def update(self):
        #Teclas do teclado prontas:
        WKEY = self.keyboard[bge.events.WKEY].active
        SKEY = self.keyboard[bge.events.SKEY].active
        AKEY = self.keyboard[bge.events.AKEY].active
        DKEY = self.keyboard[bge.events.DKEY].active
        
        #Direcoes das teclas
        y = SKEY - WKEY
        x = DKEY - AKEY
        
        #aplica a rotação para as direções certas
        self.object.applyRotation(Vector([y,0,x]) * 0.01, True)
        pass
    