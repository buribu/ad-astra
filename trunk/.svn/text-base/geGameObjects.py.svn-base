import random
import geUtil

class Empire:

    def __init__(self, na, ind, ruler=None):
        self.name = na
        self.index = ind
        self.attributes = {}
        self.technologies = []
        self.currentresearch = None
        self.researchrate = 20
        self.researchprogress = 0
        self.leader = ruler
        if self.leader == None:
            self.leader = Person(geUtil.generatePersonName(), random.choice(('F', 'M')))
        
    def hasTech(self, tech):
        return tech in self.technologies
        
    def setResearch(self, tech):
        self.currentresearch = tech
    
    def processResearch(self):
        self.researchprogress += self.researchrate
        try:
            if self.researchprogress >= self.currentresearch.cost:
                self.technologies.append(self.currentresearch)
                self.researchprogress -= self.currentresearch.cost
                self.currentresearch = None
                return True
        except AttributeError:
            pass
        return False
        
    def advanceTurn(self):
        self.processResearch()

class Person:

    def __init__(self, na, s):
        self.name = na
        self.sex = s
        self.attributes = {}
        self.currentEffects = []

    @property
    def fullTitle(self):
        if self.sex == 'F':
            return "Empress " + self.name
        else:
            return "Emperor " + self.name
            
class Ship:
    
    def __init__(self):
        self.attributes = {}
