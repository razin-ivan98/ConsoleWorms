import time
from LinearAlgebra import Vector_2, v_2_mul, v_2_sum

from Object import Object
from Stone import Stone

G = 15.0

class PhisicsEngine:
    def __init__(self, map: list[list[str]], objects: list[Object]):
        self.__map = map
        self.__objects = objects
        self.__start_time = time.time()
        self.__last_time = self.__start_time

    def calculate(self):
        curr_time = time.time()
        d_time = curr_time - self.__last_time

        for object in self.__objects:
            if not object.is_on_ground:
                object.set_speed(Vector_2(object.speed.x, object.speed.y + G * d_time))

            d = v_2_mul(object.speed, d_time)
            if self.__is_intersect(object, v_2_sum(object.pos, Vector_2(0.0, d.y))):
                object.set_speed(Vector_2(object.speed.x, object.speed.y / 2))
            else:
                object.move(Vector_2(y = d.y))
            if not self.__is_intersect(object, v_2_sum(object.pos, Vector_2(d.x, 0.0))):
                object.move(Vector_2(x = d.x))
            object.is_on_ground = self.__is_on_ground(object)
            if not object.is_on_ground:
                if object.speed.y > 15:
                    object.force_fall()
                else:
                    object.fall()
            else:
                object.set_speed(Vector_2(object.speed.x, 0.0))
                object.touchdown()
            if object.fired:
                speed = Vector_2(-30.0 if object.is_flipped else 30.0, -10.0)
                self.__objects.append(Stone(object.pos, speed))
        self.__last_time = curr_time

    def __is_intersect(self, object: Object, new_pos: Vector_2 = None):
        pos = object.pos
        map = self.__map
        if new_pos:
            pos = new_pos
        if pos.x >= len(map[0]) or pos.x < 0 or pos.y >= len(map) or pos.y < 0:
            return True
        if object.collider:
            collider = object.collider
        else:
            collider = object.get_img()
        width = len(collider[0])
        height = len(collider)
        start_x = int(pos.x) - width // 2
        start_y = int(pos.y) - height // 2
        for y, line in enumerate(collider):
            for x, cell in enumerate(line):
                if map[start_y + y][start_x + x] != " ":
                    return True
        return False
    
    def __is_on_ground(self, object: Object):
        pos = object.pos
        if object.collider:
            collider = object.collider
        else:
            collider = object.get_img()
        width = len(collider[0])
        height = len(collider)
        start_x = int(pos.x) - width // 2
        start_y = int(pos.y) + height // 2
        if start_y >= len(self.__map):
            return True
        
        for x in range(start_x, start_x + width):
            if self.__map[start_y][x] != " ":
                return True
        return False
