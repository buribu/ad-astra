import curses, curses.textpad
import geUtil

def disptitle(stdscr, opt):
    stdscr.erase()
    for x in range(0, 80):
        stdscr.addstr(0, x, '*', curses.color_pair(3))
    for y in range(0, 23):
        stdscr.addstr(y, 0, '^', curses.color_pair(3))
        stdscr.addstr(y, 79, '^', curses.color_pair(3))
    stdscr.addstr(4, 36, "AD ASTRA", curses.color_pair(3))
    stdscr.addstr(6, 36, "By Alice")
    curses.textpad.rectangle(stdscr, 17, 34, 20, 44)
    stdscr.addstr(9, 17, "It ought to be remembered that there is nothing")
    stdscr.addstr(10, 12, "more difficult to take in hand, more perilous to conduct,")
    stdscr.addstr(11, 13, "or more uncertain in its success, than to take the lead")
    stdscr.addstr(12, 18, "in the introduction of a new order of things.")
    stdscr.addstr(14, 45, "-Niccolo Machiavelli")
    stdscr.addstr(18, 36, "NEW GAME")
    stdscr.addstr(19, 36, "QUIT")
    if opt == 0:
        stdscr.addstr(18, 35, ">")
    elif opt == 1:
        stdscr.addstr(19, 35, ">")
    stdscr.addstr(22, 27,  "z to select, x to cancel")
    stdscr.addstr(23, 26,  "Shift-Q to exit at any time.")
    #if glob.MAC:
    #    stdscr.addstr(22, 79, glob.macfix())

def dispGalaxy(stdscr, gal, loc):
    curses.textpad.rectangle(stdscr, 0, 0, 16, 41)
    for star in gal.stuff:
        if gal.stuff[star].typ == 0: stdscr.addstr(star[1], star[0], "+")
        else: stdscr.addstr(star[1], star[0], "+", curses.color_pair(gal.stuff[star].typ))
    if gal.stuff.has_key((loc[0], loc[1])):
        stdscr.addstr(loc[1], loc[0], "+", curses.color_pair(5))
    else:
        stdscr.addstr(loc[1], loc[0], " ", curses.color_pair(5))

def dispStar(stdscr, star, loc):
    curses.textpad.rectangle(stdscr, 0, 42, 23, 78)
    stdscr.addstr(1, 45, star.formattedname, curses.color_pair(star.typ))
    if star.owner is not None:
        stdscr.addstr(2, 46, "Owned by " + sess.getEmpireName(star.owner), curses.color_pair(star.owner))
    stdscr.addstr(4, 45, "Galactic Coordinates " + str(loc))
    for i, planet in enumerate(star.planets):
        stdscr.addstr(6+i*3, 46, planet.description)
        stdscr.addstr(7+i*3, 48, planet.climate, curses.color_pair(planet.climateColour()))
        if planet.population > 1000000:
            stdscr.addstr(7+i*3, 63, str(planet.population/1000000)+"m", curses.color_pair(0))
        elif planet.population > 1000:
            stdscr.addstr(7+i*3, 63, str(planet.population/1000)+"k", curses.color_pair(1))
        elif planet.population > 0:
            stdscr.addstr(7+i*3, 63, str(planet.population), curses.color_pair(2))
    if len(star.planets) == 0:
        stdscr.addstr(6, 45, "No Planetary System")
    stdscr.addstr(20, 1, "z: System")

def dispUI(stdscr, sess):
    curses.textpad.rectangle(stdscr, 16, 0, 23, 41)
    stdscr.addstr(17, 1, sess.getLeaderFullName(0))
    stdscr.addstr(17, 41-(len(sess.getEmpireName(0))), sess.getEmpireName(0))
    stdscr.addstr(20, 13, "wasd: Cursor")
    stdscr.addstr(21, 1, "e: Empire")
    stdscr.addstr(21, 13, "D: Diplomacy")
    stdscr.addstr(21, 28, "R: Treasury")
    stdscr.addstr(22, 13, "S: Espionage")
    stdscr.addstr(22, 1, "f: Fleets")
    stdscr.addstr(22, 28, "Q: Quit")
    stdscr.addstr(20, 28, "r: Research")

def mainScreenTurnOn(stdscr, gal, loc, sess, MAC=False):
    stdscr.erase()
    dispGalaxy(stdscr, gal, loc)
    if gal.stuff.has_key((loc[0], loc[1])):
        dispStar(stdscr, gal.stuff[(loc[0], loc[1])], loc)
    else:
        stdscr.addstr(1, 45, "INTERSTELLAR SPACE")
        stdscr.addstr(4, 45, "Galactic Coordinates " + str(loc))
    stdscr.addstr(18, 26, "Star Era " + gal.prettyDate())
    dispUI(stdscr, sess)
    #if MAC:
    #    stdscr.addstr(22, 79, glob.macfix())
    
def displayTech(stdscr, cursor, filteredtechs, sess):
    stdscr.erase()
    curses.textpad.rectangle(stdscr, 0, 0, 18, 19)
    curses.textpad.rectangle(stdscr, 18, 0, 23, 19)
    curses.textpad.rectangle(stdscr, 0, 49, 4, 78)
    curses.textpad.rectangle(stdscr, 0, 20, 14, 48)
    stdscr.addstr(21, 1, "wasd: Cursor")
    stdscr.addstr(22, 1, "Space: Return")
    if cursor[0] != 0:
        stdscr.addstr(19, 1, "z: Research")
        stdscr.addstr(20, 1, "e: Details")
    stdscr.addstr(1, 1, "Filter by tag...")
    if cursor[0] == 0 and cursor[1] == 0:
        stdscr.addstr(2, 2, "ALL", curses.color_pair(5))
    elif cursor[1] == 0:
        stdscr.addstr(2, 2, "ALL", curses.color_pair(1))
    else:
        stdscr.addstr(2, 2, "ALL")
    for i, tag in enumerate(geUtil.allTags):
        if cursor[0] == 0 and cursor[1] == i+1:
            stdscr.addstr(i+3, 2, tag, curses.color_pair(5))
        elif cursor[1] == i+1:
            stdscr.addstr(i+3, 2, tag, curses.color_pair(1))
        else:
            stdscr.addstr(i+3, 2, tag)
    for i, tech in enumerate(filteredtechs):
        if cursor[0] == 1 and i == cursor[2]:
            if tech == sess.getPlayerEmpire().currentresearch:
                stdscr.addstr(i+1, 21, tech.name, curses.color_pair(7))
            else:
                stdscr.addstr(i+1, 21, tech.name, curses.color_pair(5))
        elif tech == sess.getPlayerEmpire().currentresearch:
            stdscr.addstr(i+1, 21, tech.name, curses.color_pair(3))
        else:
            stdscr.addstr(i+1, 21, tech.name)
    if sess.getPlayerEmpire().currentresearch is not None:
        stdscr.addstr(1, 50, "Current:  " + str(sess.getPlayerEmpire().currentresearch.name))
    else:
        stdscr.addstr(1, 50, "Current: ")
        stdscr.addstr(1, 60, "None", curses.color_pair(2))
    stdscr.addstr(2, 50, "Progress: " + str(sess.getPlayerEmpire().researchprogress))
    stdscr.addstr(3, 50, "RP/month: " + str(sess.getPlayerEmpire().researchrate))

def displayEmpire(stdscr, sess):
    #Need to implement auto-centering algorithm for text
    stdscr.erase()
    curses.textpad.rectangle(stdscr, 0, 31, 5, 47)
    curses.textpad.rectangle(stdscr, 18, 0, 23, 19)
    stdscr.addstr(1, 34, "The Mighty")
    stdscr.addstr(2, 32, sess.getEmpireName(0).upper())
    stdscr.addstr(3, 39, "of")
    stdscr.addstr(4, 33, sess.getLeaderFullName(0).upper())
    stdscr.addstr(22, 1, "Space: Return")

def displayEspionage(stdscr, sess):
    stdscr.erase()
    stdscr.addstr(22, 1, "Space: Return")

def displayTreasury(stdscr, sess):
    stdscr.erase()
    stdscr.addstr(22, 1, "Space: Return")

def displayFleets(stdscr, sess):
    stdscr.erase()
    stdscr.addstr(22, 1, "Space: Return")

def displayDiplomacy(stdscr, sess):
    stdscr.erase()
    stdscr.addstr(22, 1, "Space: Return")
