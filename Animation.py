class Animation:
    def __init__(self, name: str, frames: list[list[str]], speed: float, flipped: list[list[str]] = None):
        self.name = name
        self.frames = frames
        self.speed = speed
        self.length = len(frames)
        self.flipped_frames = flipped
        if flipped:
            assert len(flipped) == len(frames), \
                "Количество кадров обычной и отраженной анимации должно совпадать"