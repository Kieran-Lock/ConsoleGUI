from enum import Enum
from .rgb import RGB


class RGBs(Enum):
    DEFAULT_FOREGROUND = RGB(192, 192, 192)
    DEFAULT_BACKGROUND_PYCHARM = RGB(43, 43, 43)
    DEFAULT_BACKGROUND_REPLIT = RGB(28, 35, 51)
    BLACK = RGB(0, 0, 0)
    WHITE = RGB(255, 255, 255)
    RED = RGB(255, 0, 0)
    GREEN = RGB(0, 255, 0)
    BLUE = RGB(0, 0, 255)
    YELLOW = RGB(255, 255, 0)
    CYAN = RGB(0, 255, 255)
    MAGENTA = RGB(255, 0, 255)
    ORANGE = RGB(255, 165, 0)
    PURPLE = RGB(230, 230, 250)
    GREY = RGB(142, 142, 142)
    BROWN = RGB(162, 162, 42)