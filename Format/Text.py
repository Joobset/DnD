def ESC(color):
    return "\033[" + str(color) + "m"

def FORE(color):
    return ESC("3" + str(color))

def BACK(color):
    return ESC("4" + str(color))

black = 0
red = 1
green = 2
yellow = 3
blue = 4
magenta = 5
cyan = 6
white = 7

class F:
    RESET = ESC(0)
    BLACK = FORE(black)
    RED = FORE(red)
    GREEN = FORE(green)
    YELLOW = FORE(yellow)
    BLUE = FORE(blue)
    MAGENTA = FORE(magenta)
    CYAN = FORE(cyan)
    WHITE = FORE(white)

class B:
    BLACK = BACK(black)
    RED = BACK(red)
    GREEN = BACK(green)
    YELLOW = BACK(yellow)
    BLUE = BACK(blue)
    MAGENTA = BACK(magenta)
    CYAN = BACK(cyan)
    WHITE = BACK(white)

