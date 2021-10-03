import time
from Animation import Animation

class Animator():
    def __init__(self):
        self.__animations: dict[str, Animation] = {}
        self.__is_flipped = False
        self.__curr_anim = None
        self.__once = False
        self.__not_abortable = False
    
    def add_anim(self, anim: Animation):
        self.__animations[anim.name] = anim

    def del_anim(self, name: str):
        if name in self.__animations:
            del self.__animations[name]

    def run(self, name: str, once: bool = False, not_abortable: bool = False):
        if self.__not_abortable:
            return
        if name in self.__animations:
            self.__once = once
            self.__not_abortable = not_abortable
            self.__curr_anim = self.__animations[name]
            if (self.__curr_anim.length > 1):
                self.__start = time.time()
    
    def stop(self):
        self.__start = None
        self.__curr_anim = None

    def get_frame(self):
        curr = self.__curr_anim
        if not curr:
            return None
        if (self.__curr_anim.length == 1):
            frame_num = 0
        else:
            now = time.time()
            if self.__once and int((now - self.__start) * curr.speed) >= curr.length - 1:
                self.__not_abortable = False
            frame_num = int((now - self.__start) * curr.speed) % curr.length
        if self.__is_flipped and curr.flipped_frames:
            return curr.flipped_frames[frame_num]
        return curr.frames[frame_num]

    def flip(self):
        self.__is_flipped = not self.__is_flipped

    @property
    def is_flipped(self):
        return self.__is_flipped

    @property
    def curr_anim(self):
        return self.__curr_anim.name

    @property
    def can_control(self):
        return not self.__not_abortable
    
