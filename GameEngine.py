from Control import Control
from GraphicsEngine import GraphicsEngine
from LinearAlgebra import Vector_2
from Object import Object
from PhisicsEngine import PhisicsEngine
from Worm import Worm

from time import sleep

class GameEngine:
    def __init__(self, map: list[str]):
        self.__objects: list[Object] = []
        self.__graphics = GraphicsEngine(len(map[0]), len(map), map, self.__objects)
        self.__phisics = PhisicsEngine(map, self.__objects)
        self.__control = None

    def add_worm(self):
        worm = Worm(Vector_2(5.0, 5.0))
        self.__objects.append(worm)
        return worm

    def run(self):
        while True:
            if self.__control:
                self.__control.handle_input()
            self.__phisics.calculate()
            self.__graphics.draw_frame()
            sleep(0.07)

    def init_control(self, player: Worm):
        self.__control = Control(player)