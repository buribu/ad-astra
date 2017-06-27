import random
import geUtil

climates = {"Tropical":4, "Volcanic":2, "Oceanic":3, "Semi-oceanic":3, "Barren":1, "Gaseous":1, 
            "Hadean":2, "Idyllic":4, "Frozen":3, "Boreal":3, "Forested":4, "Swamp":4, "Desert":1}

class Planet:

    def __init__(self, homestar, pos, forceHome=False, own=None):
        self.homeStar = homestar
        self.rank = pos+1
        self.owner = own
        self.population = 0
        if not forceHome:
            self.size = random.choice(['Small', 'Small', 'Normal', 'Normal', 'Large'])
            if self.homeStar.variety == "Dwarf":
                self.habitable = random.choice([False, True])
            elif self.homeStar.variety == "Main Sequence Star":
                self.habitable = random.choice([False, True, True, True])
            elif self.homeStar.variety == "Giant":
                self.habitable = random.choice([False, False, False, True, True])
            self.populated = False
        else:
            self.size = random.choice(["Small", "Normal", "Normal", "Normal", "Normal", "Normal", "Large", "Large"])
            self.habitable = True
            self.populated = True
        self.randomizeClimate()
        if self.populated:
            self.initPop()
            
    def makeHomePlanet(self, own):
        self.owner = own
        self.size = random.choice(["Small", "Normal", "Normal", "Normal", "Normal", "Normal", "Large", "Large"])
        self.habitable = True
        self.populated = True
        self.initPop()
        
    def initPop(self):
        if self.size == "Small":
            self.population = random.randrange(1e8, 5e9)
        elif self.size == "Normal":
            self.population = random.randrange(5e8, 1e10)
        elif self.size == "Large":
            self.population = random.randrange(1e9, 4e10)
            
    def randomizeClimate(self):
        self.climate = random.choice(climates.keys())
        if self.climate == "Gaseous" and self.size != "Large": self.randomizeClimate()
        
    def climateColour(self):
        return climates[self.climate]

    @property
    def description(self):
        tmp = [self.homeStar.name, " ", geUtil.romanNumerals[self.rank], ": ", self.size]
        return "".join(tmp)

    @property
    def habitability(self):
        if self.populated: return "Populated"
        elif self.habitable: return "Habitable"
        else: return "Uninhabitable"

    @property
    def habcolour(self):
        if self.populated: return 4
        elif self.habitable: return 3
        else: return 2

class Star:

    def __init__(self, loc, forceHome=False, own=None):
        self.typ = random.choice([0, 1, 1, 1, 2, 2, 3])
        self.name = geUtil.generateStarName()
        self.location = loc
        self.planets = []
        self._owner = own
        if not forceHome:
            self.variety = random.choice(["Dwarf", "Dwarf", "Main Sequence Star", "Main Sequence Star", "Giant"])
            for n in range(0, random.randint(0, 5)):
                self.planets.append(Planet(self, n))
        else:
            self.variety = "Main Sequence Star"
            for n in range(0, random.randint(3, 5)):
                self.planets.append(Planet(self, n))
            random.choice(self.planets).makeHomePlanet(self._owner)
            
    def advanceTurn(self):
        pass

    @property
    def formattedname(self):
        return "".join([self.name, " (", self.variety, ")"])

    @property
    def owner(self):
        return self._owner

class Galaxy:

    def __init__(self, playercount=5, startotal=25):
        self.size = (40, 15)
        self.stuff = {}
        self.date = 1
        for player in range(0, playercount):
            while True:
                if self.placeStar(True, player):
                    break
        while len(self.stuff.keys()) < startotal:
            self.placeStar(False)

    def placeStar(self, home, player=None):
        if home:
            newCoord = (random.randrange(1, 41), random.randrange(1, 16))
            if self.stuff.has_key(newCoord):
                return False
            self.stuff[newCoord] = Star(newCoord, True, player)
            return True
        else:
            newCoord = (random.randrange(1, 41), random.randrange(1, 16))
            if self.stuff.has_key(newCoord):
                return False
            self.stuff[newCoord] = Star(newCoord)
            return True
            
    def advanceTurn(self):
        for stuff in self.stuff.values():
            stuff.advanceTurn()
        self.date += 1
            
    def prettyDate(self):
        return "{0:6}".format(self.date)
