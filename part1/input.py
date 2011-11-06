# http://docs.python.org/howto/curses.html
import curses
stdscr = curses.initscr()
stdscr.timeout(-1);

while 1:
    c = stdscr.getch()
    if c == ord('p'): print "POUUF"
    elif c == ord('q'): break  # Exit the while()
    elif c == curses.KEY_HOME: x = y = 0

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
