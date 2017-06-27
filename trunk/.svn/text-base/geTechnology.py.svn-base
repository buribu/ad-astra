import os
import geUtil

techs = {}

class Technology:
    
    def __init__(self, f):
        with open(os.path.join("tech",f)) as fil:
            self.rawdat = fil.read()
        self.name = self.rawdat[self.rawdat.find("<name>")+6:self.rawdat.find("</name>")]
        self.id = self.rawdat[self.rawdat.find("<fiid>")+6:self.rawdat.find("</fiid>")]
        self.cost = int(self.rawdat[self.rawdat.find("<cost>")+6:self.rawdat.find("</cost>")])
        
        if "<tags>" in self.rawdat:
            self.tags = self.rawdat[self.rawdat.find("<tags>")+6:self.rawdat.find("</tags>")].split(";")
            for tag in self.tags:
                geUtil.addTag(tag)
        
        if "<pers>" in self.rawdat:
            self.personeffects = self.rawdat[self.rawdat.find("<pers>")+6:self.rawdat.find("</pers>")].split(";")
        if "<ship>" in self.rawdat:
            self.shipeffects = self.rawdat[self.rawdat.find("<ship>")+6:self.rawdat.find("</ship>")].split(";")
        if "<empi>" in self.rawdat:
            self.empireeffects = self.rawdat[self.rawdat.find("<empi>")+6:self.rawdat.find("</empi>")].split(";")
        
    def applyToPerson(self, pers):
        for effect in self.personeffects:
            parts = effect.split()
            if parts[1] == "add":
                pers.attributes[parts[0]] += int(parts[2])
            elif parts[1] == "subtract":
                pers.attributes[parts[0]] -= int(parts[2])
            elif parts[1] == "set":
                pers.attributes[parts[0]] = int(parts[2])
    
    def applyToEmpire(self, emp):
        for effect in self.empireeffects:
            parts = effect.split()
            if parts[1] == "add":
                emp.attributes[parts[0]] += int(parts[2])
            elif parts[1] == "subtract":
                emp.attributes[parts[0]] -= int(parts[2])
            elif parts[1] == "set":
                emp.attributes[parts[0]] = int(parts[2])
    
    def applyToShip(self, ship):
        for effect in self.shipeffects:
            parts = effect.split()
            if parts[1] == "add":
                ship.attributes[parts[0]] += int(parts[2])
            elif parts[1] == "subtract":
                ship.attributes[parts[0]] -= int(parts[2])
            elif parts[1] == "set":
                ship.attributes[parts[0]] = int(parts[2])
        
for fil in os.listdir("tech"):
        if ".tech" in fil:
            try:
                geUtil.addTech(Technology(fil), fil)
            except:
                print "Failed to load tech from file: " + str(fil)
                
geUtil.sortTags()
