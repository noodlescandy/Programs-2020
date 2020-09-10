from curses import wrapper
import curses
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.leaveok(False) # turns off flashing cursor
    
    """stdscr.addstr(1,1,"test", curses.A_REVERSE)
    stdscr.addstr(5,2,"also", curses.A_DIM) # can also have attributes

    stdscr.move(3,3) # moves cursor to 3,3 (y,x)
    stdscr.addstr('b', curses.A_STANDOUT)

    stdscr.addch(7,8,'5', curses.color_pair(3))"""
    max = stdscr.getmaxyx()
    maxY = max[0] - 1
    maxX = max[1] - 2
    posX = 1
    posY = 1
    stdscr.move(1,1)
    while True:
        oldposX = posX
        oldposY = posY
        input = stdscr.getch()
        if input == ord('w'):
            posY -= 1
        else:
            if input == ord('a'):
                posX -= 1
                #stdscr.addstr(7,7,"A")
            else:
                if input == ord('s'):
                    posY += 1
                else:
                    if input == ord('d'):
                        posX += 1
                        #stdscr.addstr(7,7,"D")
        
        if (oldposX != posX or oldposY != posY):
            if posX < 0 or posY < 0 or posX > maxX or posY > maxY:
                posX = oldposX
                posY = oldposY
            stdscr.addstr(oldposY, oldposX, ' ', curses.A_STANDOUT)
            stdscr.move(posY, posX)
            stdscr.addstr('o')
            #stdscr.move(posY, posX-1)
            stdscr.addstr(1,20,"X=" + str(posX) + "  ")
            stdscr.addstr(2,20,"Y=" + str(posY) + "  ")
            stdscr.refresh()

wrapper(main)
