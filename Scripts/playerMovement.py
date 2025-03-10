import bge
import mathutils
from collections import OrderedDict

class Movement(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.keyboard = bge.logic.keyboard.inputs
        
        pass
    
    def keys(self):
        #Teclas do teclado prontas:
        self.WKEY = self.keyboard[bge.events.WKEY].active
        self.SKEY = self.keyboard[bge.events.SKEY].active
        self.AKEY = self.keyboard[bge.events.AKEY].active
        self.DKEY = self.keyboard[bge.events.DKEY].active
        pass
    
    def rotation(self):
        self.keys()
        #Direcoes das teclas
        y = self.SKEY - self.WKEY
        x = self.DKEY - self.AKEY
        #aplica a rotação para as direções certas
        self.object.applyRotation(mathutils.Vector([y,0,x]) * 0.01, True)
              
    def update(self):
        self.rotation()
        
        pass
    