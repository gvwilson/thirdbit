import curses
import sys

from util import open_log, log, make_lines, start, ROW, COL

# [window]
class Window:
    def __init__(self, screen, size):
        self._screen = screen
        if size is None:
            self._nrow = curses.LINES
            self._ncol = curses.COLS
        else:
            self._nrow = min(size[ROW], curses.LINES)
            self._ncol = min(size[COL], curses.COLS)

    def draw(self, lines):
        self._screen.erase()
        for (y, line) in enumerate(lines):
            if 0 <= y < self._nrow:
                self._screen.addstr(y, 0, line[:self._ncol])
# [/window]

def main(stdscr, size, lines):
    window = Window(stdscr, size)
    window.draw(lines)
    while True:
        key = stdscr.getkey()
        if key.lower() == "q":
            return

if __name__ == "__main__":
    size, lines = start()
    curses.wrapper(lambda stdscr: main(stdscr, size, lines))
