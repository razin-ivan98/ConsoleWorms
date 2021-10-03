from time import process_time
import keyboard
from LinearAlgebra import Vector_2
from Worm import Worm


class Control:
    def __init__(self, player: Worm):
        self.__player = player 
    
    def handle_input(self):
        walking = False

        player = self.__player
        if keyboard.is_pressed('a'):
            player.walk(to_left = True)
            walking = True

        if keyboard.is_pressed('d'):
            player.walk(to_left = False)
            walking = True

        if keyboard.is_pressed(' '):
            player.jump()

        if keyboard.is_pressed('f'):
            player.fire()

        if not walking:
            player.idle()




        # self.__player.set_speed(Vector_2(dx))