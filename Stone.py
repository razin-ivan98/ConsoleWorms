
from LinearAlgebra import Vector_2
from Object import Object

from animations.stone.stone import stone

class Stone(Object):
    def __init__(self, pos: Vector_2, speed: Vector_2):
        super().__init__(pos)
        self.set_speed(speed)
        self._animator.add_anim(stone)
        self._animator.run("stone")

    def fall(self):
        return

    def touchdown(self):
        self.set_speed(Vector_2())
    
    def force_fall(self):
        return

    @property
    def fired(self):
        return False
    
