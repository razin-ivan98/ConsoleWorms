class Vector_2:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

def v_2_sum(a: Vector_2, b: Vector_2):
    return Vector_2(a.x + b.x, a.y + b.y)

def v_2_sub(a: Vector_2, b: Vector_2):
    return Vector_2(a.x - b.x, a.y - b.y)

def v_2_mul(a: Vector_2, k: float):
    return Vector_2(a.x * k, a.y * k)