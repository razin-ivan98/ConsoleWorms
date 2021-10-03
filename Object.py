from Animator import Animator
from LinearAlgebra import Vector_2, v_2_sum

class Object:
    def __init__(self, pos: Vector_2):
        self.__pos = pos
        self.__animator = Animator()
        self.__speed = Vector_2()
        self.is_on_ground = False

    def move(self, d: Vector_2):
        self.__pos = v_2_sum(self.__pos, d)

    @property
    def pos(self):
        return self.__pos

    def flip(self):
        self.__animator.flip()

    def get_img(self):
        return self._animator.get_frame()

    @property
    def _animator(self):
        return self.__animator

    @property
    def is_flipped(self):
        return self.__animator.is_flipped

    @property
    def speed(self):
        return self.__speed

    def set_speed(self, speed: Vector_2):
        self.__speed = speed


    @property
    def curr_anim(self):
        return self.__animator.curr_anim

    @property
    def collider(self):
        return None
