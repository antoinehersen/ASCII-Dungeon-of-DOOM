# http://docs.python.org/howto/curses.html
import curses
stdscr = curses.initscr()
stdscr.timeout(-1);
curses.noecho()
while 1:
    c = stdscr.getch()
    if c == ord('p'): stdscr.addstr("FART\n")
    elif c == ord('c'): stdscr.addch('x')
    elif c == ord('f'): stdscr.erase()
    elif c == ord('q'): break  # Exit the while()
    elif c == curses.KEY_HOME: x = y = 0

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
