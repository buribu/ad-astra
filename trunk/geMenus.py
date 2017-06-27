import geUtil, geDisplay, geMapObjects
import curses

class menuGlob:
    '''Stuff all the menus need to access.'''
    
    def __init__(self):
        self.menu = TitleMenu()
        self.screen = None
        self.SCL = [1, 1]
        
    def get(self):
        return self.menu

    def change(self, menu):
        self.menu = menu
        
    def setScreen(self, scr):
        self.screen = scr

class TitleMenu:
    
    def __init__(self):
        self.opt = 0
        self.numberOfOptions = 2
        
    def display(self):
        geDisplay.disptitle(m.screen, self.opt)
        
    def process(self, ch, galaxy, sess):
        if ch == ord('z'):
            if self.opt == 0:
                m.change(GalaxyMenu(galaxy, sess))
            elif self.opt == 1:
                return True
        elif (ch == ord("w") or ch == curses.KEY_UP):
            self.opt -= 1
            if self.opt == -1:
                self.opt = self.numberOfOptions - 1
            self.display()
        elif (ch == ord("s") or ch == curses.KEY_DOWN):
            self.opt = (self.opt + 1) % self.numberOfOptions
            self.display()

class GalaxyMenu:
    
    def __init__(self, galaxy, sess):
        self.refreshDisplay(galaxy, sess)
        
    def refreshDisplay(self, galaxy, sess):
        geDisplay.mainScreenTurnOn(m.screen, galaxy, m.SCL, sess)
        
    def process(self, ch, galaxy, sess):
        if (ch == ord("w") or ch == curses.KEY_UP) and m.SCL[1] > 1:
            m.SCL[1] -= 1
            self.refreshDisplay(galaxy, sess)
        elif (ch == ord("s") or ch == curses.KEY_DOWN) and m.SCL[1] < 15:
            m.SCL[1] += 1
            self.refreshDisplay(galaxy, sess)
        elif (ch == ord("a") or ch == curses.KEY_LEFT) and m.SCL[0] > 1:
            m.SCL[0] -= 1
            self.refreshDisplay(galaxy, sess)
        elif (ch == ord("d") or ch == curses.KEY_RIGHT) and m.SCL[0] < 40:
            m.SCL[0] += 1
            self.refreshDisplay(galaxy, sess)
        elif ch == curses.KEY_ENTER or ch == 10:
            sess.advanceTurn()
            self.refreshDisplay(galaxy, sess)
        else:
            for key in menu_keys.keys():
                if ch == ord(key):
                    m.change(menu_keys[key](sess))

class ResearchMenu:
    
    def __init__(self, sess):
        self.currentFilter = "ALL"
        self.currentCursor = [0, 0, -1]
        self.allTechs = geUtil.getAllTechs()
        self.oldTechs = sess.getPlayerEmpire().technologies
        self.refreshDisplay(sess)
        
    def refreshDisplay(self, sess):
        geDisplay.displayTech(m.screen, self.currentCursor, self.getFilteredTechs(), sess)

    def getFilteredTechs(self):
        if self.currentCursor[1] == 0:
            return self.allTechs
        return geUtil.techsByFilter[geUtil.allTags[self.currentCursor[1]-1]]
        
    def process(self, ch, galaxy, sess):
        if ch == ord(" "):
            m.change(GalaxyMenu(galaxy, sess))
            return False
        elif (ch == ord("w") or ch == curses.KEY_UP):
            if self.currentCursor[0] == 0 and self.currentCursor[1] > 0:
                self.currentCursor[1] -= 1
            elif self.currentCursor[0] == 1 and self.currentCursor[2] > 0:
                self.currentCursor[2] -= 1
        elif (ch == ord("s") or ch == curses.KEY_DOWN):
            if self.currentCursor[0] == 0 and self.currentCursor[1] < geUtil.getNumberOfTags():
                self.currentCursor[1] += 1
            elif self.currentCursor[0] == 1 and self.currentCursor[2] < len(self.getFilteredTechs())-1:
                self.currentCursor[2] += 1
        elif (ch == ord("a") or ch == curses.KEY_LEFT):
            if self.currentCursor[0] > 0:
                self.currentCursor[0] -= 1
                if self.currentCursor[0] == 0:
                    self.currentCursor[2] = -1
        elif (ch == ord("d") or ch == curses.KEY_RIGHT):
            if self.currentCursor[0] < 1:
                self.currentCursor[0] += 1
                if self.currentCursor[0] == 1:
                    self.currentCursor[2] = 0
        elif ch == ord("z") and self.currentCursor[0] == 1:
            sess.getPlayerEmpire().setResearch(self.getFilteredTechs()[self.currentCursor[2]])
        else:
            return False
        self.refreshDisplay(sess)

class EmpireMenu:

    def __init__(self, sess):
        self.refreshDisplay(sess)

    def refreshDisplay(self, sess):
        geDisplay.displayEmpire(m.screen, sess)

    def process(self, ch, galaxy, sess):
        if ch == ord(" "):
            m.change(GalaxyMenu(galaxy, sess))
            return False

class EspionageMenu:

    def __init__(self, sess):
        self.refreshDisplay(sess)

    def refreshDisplay(self, sess):
        geDisplay.displayEspionage(m.screen, sess)

    def process(self, ch, galaxy, sess):
        if ch == ord(" "):
            m.change(GalaxyMenu(galaxy, sess))
            return False

class TreasuryMenu:

    def __init__(self, sess):
        self.refreshDisplay(sess)

    def refreshDisplay(self, sess):
        geDisplay.displayTreasury(m.screen, sess)

    def process(self, ch, galaxy, sess):
        if ch == ord(" "):
            m.change(GalaxyMenu(galaxy, sess))
            return False

class FleetsMenu:

    def __init__(self, sess):
        self.refreshDisplay(sess)

    def refreshDisplay(self, sess):
        geDisplay.displayFleets(m.screen, sess)

    def process(self, ch, galaxy, sess):
        if ch == ord(" "):
            m.change(GalaxyMenu(galaxy, sess))
            return False

class DiplomacyMenu:

    def __init__(self, sess):
        self.refreshDisplay(sess)

    def refreshDisplay(self, sess):
        geDisplay.displayDiplomacy(m.screen, sess)

    def process(self, ch, galaxy, sess):
        if ch == ord(" "):
            m.change(GalaxyMenu(galaxy, sess))
            return False

m = menuGlob()
menu_keys = {"r":ResearchMenu, 
             "e":EmpireMenu,
             "S":EspionageMenu,
             "R":TreasuryMenu,
             "f":FleetsMenu,
             "D":DiplomacyMenu}
