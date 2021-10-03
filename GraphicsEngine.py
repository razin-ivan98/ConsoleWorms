from DrawEngine import DrawEngine
from Object import Object

class GraphicsEngine:
    def __init__(
        self,
        width: int,
        height: int,
        map: list[str],
        objects: list[Object]
    ):
        self.__drawEngine = DrawEngine(width, height)
        self.__map = map
        self.__objects = objects

    def __draw_map(self):
        for y, line in enumerate(self.__map):
            for x, cell in enumerate(line):
                self.__drawEngine.setPixel(x, y, cell)

    def __draw_objects(self):
        for object in self.__objects:
            pos = object.pos
            img = object.get_img()
            width = len(img[0])
            height = len(img)
            start_x = int(pos.x) - width // 2
            start_y = int(pos.y) - height // 2
            for y, line in enumerate(img):
                for x, cell in enumerate(line):
                    self.__drawEngine.setPixel(start_x + x, start_y + y, cell)

    def __makeFrame(self):
        # setPixel = self.__drawEngine.setPixel
        # width = self.__drawEngine.width
        # height = self.__drawEngine.height
        self.__draw_map()
        self.__draw_objects()

    def draw_frame(self):
        self.__makeFrame()
        self.__drawEngine.draw()


