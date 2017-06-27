import random, os, sys
try:
    import curses, curses.textpad
except:
    print "Curses library required! For support, go to: "
    print "http://www.daydreamspiral.com/forum/viewtopic.php?f=3&t=46"
    sys.exit()
import geUtil, geMapObjects, geDisplay, geGameObjects, geMenus
import geTechnology, geSession

session = geSession.GameSession()

def prog(stdscr):
    #stdscr.leaveok(1)
    try: curses.curs_set(0)
    except: pass
    geMenus.m.setScreen(stdscr)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_GREEN)
    curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_GREEN)
    geMenus.m.get().display()
    stdscr.refresh()
    while 1:
        ch = stdscr.getch()
        if ch == ord('Q'): break
        else:
            if session.process(ch): break
            stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(prog)
