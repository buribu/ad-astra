import random
import geUtil, geMapObjects, geGameObjects, geMenus, geTechnology

class GameSession:
    
    def __init__(self):
        self.galaxy = geMapObjects.Galaxy()
        self.debugInit()
        
    def debugInit(self):
        self.empires = {0:geGameObjects.Empire("Attercop Empire", 0, geGameObjects.Person("Alice", "F")),
                                1:geGameObjects.Empire("Rebels", 1), 
                                3:geGameObjects.Empire("Starmining Inc.", 3), 
                                4:geGameObjects.Empire("Space Elves", 4),
                                2:geGameObjects.Empire("Pirates", 2)}
    
    def process(self, ch):
        return geMenus.m.get().process(ch, self.galaxy, self)

    def advanceTurn(self):
        for empire in self.empires.values():
            empire.advanceTurn()
        self.galaxy.advanceTurn()
        
    def addEmpire(self, empire, index):
        self.empires[index] = empire
        
    def getEmpire(self, index):
        return self.empires[index]
        
    def getPlayerEmpire(self):
        return self.empires[0]
        
    def getEmpireName(self, index):
        return self.empires[index].name
        
    def getLeaderName(self, index):
        return self.empires[index].leader.name
        
    def getLeaderFullName(self, index):
        return self.empires[index].leader.fullTitle
            
