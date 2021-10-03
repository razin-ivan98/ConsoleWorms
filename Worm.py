
from LinearAlgebra import Vector_2
from Object import Object

from animations.worm.walk import walk
from animations.worm.idle import idle
from animations.worm.jump import jump
from animations.worm.fall import fall
from animations.worm.rising import rising


MOVE_STEP = 9.0
JUMP_SPEED = 10.0

COLLIDER = [
    " 5555 ",
    "555555",
    "555555",
    " 5555 "
]

class Worm(Object):
    def __init__(self, pos: Vector_2):
        super().__init__(pos)
        self._animator.add_anim(walk)
        self._animator.add_anim(idle)
        self._animator.add_anim(jump)
        self._animator.add_anim(fall)
        self._animator.add_anim(rising)

        self._animator.run("idle")
        self.__collider = COLLIDER

        self.__is_force_falling = False

        self.__fired = False

    def walk(self, to_left: bool = False):
        if not self.is_on_ground or not self._animator.can_control:
            return
        if self.curr_anim != "walk":
            self._animator.run("walk")
        if to_left:
            if not self.is_flipped:
                self.flip()
            dx = -MOVE_STEP
        else:
            if self.is_flipped:
                self.flip()
            dx = MOVE_STEP
        self.set_speed(Vector_2(dx))
    
    def jump(self):
        if not self.is_on_ground or not self._animator.can_control:
            return
        self.set_speed(Vector_2(self.speed.x, -JUMP_SPEED))
        self._animator.run("jump")

    def fall(self):
        if not self.curr_anim == "jump":
            self._animator.run("jump")

    def force_fall(self):
        self.__is_force_falling = True
        if not self.curr_anim == "fall":
            self._animator.run("fall")
    
    def touchdown(self):
        if self.__is_force_falling:
            self.__is_force_falling = False
            self._animator.run("rising", once = True, not_abortable = True)
        if self.curr_anim == "jump":
            self._animator.run("idle")

    def idle(self):
        if not self.is_on_ground:
            return
        self.set_speed(Vector_2(0.0, self.speed.y))
        if self.curr_anim != "idle":
            self._animator.run("idle")

    def fire(self):
        if not self.is_on_ground or not self._animator.can_control:
            return
        self.__fired = True

    @property
    def fired(self):
        fired = self.__fired
        self.__fired = False
        return fired
    
    @property
    def collider(self):
        return self.__collider

    
