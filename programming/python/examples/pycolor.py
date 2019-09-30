"""
Simple demo to show how easy it is to add support  for ANSI Colors to Python3
"""

CSI = '\x1b['


class Ansi(object):
    FULL_RESET = 0

    def __init__(self):
        for name in dir(self):
            if not name.startswith('__'):
                setattr(self, name, CSI + str(getattr(self, name)) + 'm')


class Text(Ansi):
    DEFAULT = 39
    [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE] = range(30, 38)


class Background(Ansi):
    DEFAULT = 49
    [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE] = range(40, 48)


class Cursor(Ansi):
    BLINK = 5


Text = Text()
Background = Background()
Cursor = Cursor()

print(f"{Cursor.BLINK} This blinks {Cursor.FULL_RESET}")
print(f"{Text.RED} This is red {Text.DEFAULT}")
print(Background.BLUE, "This has a blue background", Text.DEFAULT)
