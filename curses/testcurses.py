from curses import wrapper
import curses
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.leaveok(True) # turns off flashing cursor
    
    stdscr.addstr(1,1,"test", curses.A_REVERSE)
    stdscr.addstr(5,2,"also", curses.A_DIM) # can also have attributes

    stdscr.move(3,3) # moves cursor to 3,3 (y,x)
    stdscr.addstr('b', curses.A_STANDOUT)

    stdscr.addch(7,8,'5', curses.color_pair(3))

    stdscr.refresh()
    stdscr.getkey()
    time.sleep(3)

wrapper(main)
