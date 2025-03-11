import bge
from mathutils import Vector
from collections import OrderedDict

class ShootMovement(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        #Entradas do teclado
        keyboard = bge.logic.keyboard.inputs
        
        W = keyboard[bge.events.WKEY].active
        S = keyboard[bge.events.SKEY].active
        A = keyboard[bge.events.AKEY].active
        D = keyboard[bge.events.DKEY].active
        
        #difinição da variável direction:
        x = S - W
        z = D - A
        self.direction = Vector([x ,0, z]) * 0.05
        
        if self.direction == Vector([0,0,0]):
          self.direction = Vector([-0.05, 0,0])
        
        
        pass

    def update(self):
        self.object.applyRotation(self.direction, True)
        pass
