import random

VERSION = "0.01"

romanNumerals = {1:'I',2:'II',3:'III',4:'IV',5:'V'}

allTags = []

allTechs = {}

techsByFilter = {}

NAMES_USED = []

def addTag(tag):
    if tag not in allTags:
        allTags.append(tag)
        
def sortTags():
    allTags.sort()
    
def getNumberOfTags():
    return len(allTags)

def addTech(tech, techid):
    allTechs[techid] = tech
    for tag in tech.tags:
        if not techsByFilter.has_key(tag):
            techsByFilter[tag] = []
        techsByFilter[tag].append(tech)

def getAllTechs():
    return allTechs.values()

def getTagIndex(tag):
    return allTags.find(tag)

def generateStarName(): #must not exceed length 12 for correct display
    begins = ["Rig", "Dem", "Den", "Can", "Con", "Alt", "C", "Ch", "V", "L", "D", "R", "B", "T", "Th", "S", "Sh", "Sal", "Sel", "Cer"]
    mids = ["ete", "e", "i", "ai", "ere", "orte", "ore", "ife", "ifa", "o", "u", "a", "ao", "ei"]
    ends = ["l", "r", "s", "b", "n", "x", "lle", "re", "c", "mere", "phon"]
    result = "".join([random.choice(begins), random.choice(mids), random.choice(ends)])
    if result in NAMES_USED:
        return generateStarName()
    NAMES_USED.append(result)
    return result

def generatePersonName():
    #TODO: implement
    return generateStarName()
