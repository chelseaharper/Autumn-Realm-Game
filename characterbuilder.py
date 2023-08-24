from random import randint
import itemoptions

class Creature:
    def __init__(self, type, stats, hitdie, armor, level, weapon):
        self.type = type
        self.stats = stats
        self.armor = armor
        self.melee = self.getstatmod("str")
        self.ranged = self.getstatmod("dex")
        self.caster = self.getstatmod("int")
        self.AC = 10 + (self.getstatmod("dex"))
        self.touchAC = 10 + (self.getstatmod("dex"))
        self.maxhealth = 0
        self.health = 0
        self.level = level
        self.hitdie = hitdie
        self.weapon = weapon
        self.init = 0
        self.sethealth()
        self.setAC()
    
    def rollinit(self):
        self.init = randint(1, 20) + self.getstatmod("dex")
    
    def changehealth (self, healthchange):
        if self.health + healthchange > self.maxhealth:
            self.health = self.maxhealth
        else:
            self.health += healthchange
    
    def setAC(self):
        self.AC = self.armor.setAC(self)
    
    def setTouchAC(self):
        self.touchAC = self.armor.setAC(self)
    
    def sethealth(self):
        self.health = self.hitdie + ((randint(1, self.hitdie)) * (self.level - 1)) + self.getstatmod("con")
        self.maxhealth = self.health
    
    def getAC(self, type):
        if type == "physical":
            return self.AC
        elif type == "magical":
            return self.touchAC
    
    def getstatmod(self, stat):
        return (self.stats[stat] - 10)//2

    def getHP(self, HPtype):
        return self.health
    
    def gettype(self):
        return self.type

class Player(Creature):
    def __init__(self, name, type, stats, hitdie, armor, level, weapon):
        super().__init__(type, stats, hitdie, armor, level, weapon)
        self.name = name
        self.currXP = 0
        self.needXP = 0
        self.setXPneeded()
    
    def gettype(self):
        return self.name
    
    def raiselevel(self):
        self.level += 1
        if (self.level % 2) == 0:
            self.stats["con"] += 1
            if self.type == "Fighter":
                self.stats["str"] += 1
            elif self.type == "Archer":
                self.stats["dex"] += 1
            elif self.type == "Wizard":
                self.stats["int"] += 1
        self.maxhealth += (randint(1, self.hitdie) + self.getstatmod("con"))
        self.changehealth(getaverage(self.hitdie))
        self.setXPneeded()
    
    def setXPneeded(self):
        self.needXP += 500 * self.level

    def getHP(self, HPtype):
        if HPtype == "current":
            HP = self.health
        elif HPtype == "max":
            HP = self.maxhealth
        return HP

class Monster(Creature):
    def __init__(self, type, stats, hitdie, armor, level, weapon, XP):
        super().__init__(type, stats, hitdie, armor, level, weapon)
        self.XP = XP
    
    def sethealth(self):
        self.health = (getaverage(self.hitdie) + self.getstatmod("con")) * self.level

class NPC(Monster):
    def __init__(self, type, stats, hitdie, armor, level, weapon, XP, attitude):
        super().__init__(type, stats, hitdie, armor, level, weapon, XP)
        self.attitudeoptions = ["Helpful", "Friendly", "Indifferent", "Unfriendly", "Hostile"]
        self.attitude = attitude
    
    def getDC(self):
        if self.attitude == "Hostile":
            DC = 25 + self.getstatmod("cha")
        elif self.attitude == "Unfriendly":
            DC = 20 + self.getstatmod("cha")
        elif self.attitude == "Indifferent":
            DC = 15 + self.getstatmod("cha")
        elif self.attitude == "Friendly":
            DC = 10 + self.getstatmod("cha")
        elif self.attitude == "Helpful":
            DC = 0 + self.getstatmod("cha")
        return DC
    
    def getnextattitude(self, direction, amount):
        if direction == "improved":
            if (self.attitudeoptions.index(self.attitude) - amount) < 0:
                self.attitude = self.attitudeoptions[0]
            else:
                self.attitude = self.attitudeoptions[(self.attitudeoptions.index(self.attitude) - amount)]
        elif direction == "reduced":
            if (self.attitudeoptions.index(self.attitude) + amount) > len(self.attitudeoptions):
                self.attitude = self.attitudeoptions[(len(self.attitudeoptions) - 1)]
            else:
                self.attitude = self.attitudeoptions[(self.attitudeoptions.index(self.attitude) + amount)]

    def changeattitude(self, roll):
        DC = self.getDC()
        amount = 0
        if roll >= DC:
            amount += 1
            roll -= DC
            while roll > 4:
                amount +=1
                roll -=5
            self.attitude = self.getnextattitude("improved", amount)
        elif roll < (DC - 4):
            amount += 1
            self.attitude = self.getnextattitude("reduced", amount)
        else:
            pass

def getaverage(die):
    return (die/2) + 1

def rollstat():
    rolls = []
    i = 1
    while i <= 4:
        rolls.append(randint(1, 6))
        i += 1
    
    rolls.remove(min(rolls))
    return sum(rolls)

def buildstatblock(prio):
    statsokay = "n"
    while statsokay == "n":
        statblock = {"str": rollstat(), "dex": rollstat(), "con": rollstat(), "int": rollstat(), "wis": rollstat(), "cha": rollstat()}
        if prio == "melee":
            if statblock["str"] < 12:
                statblock = {"str": rollstat(), "dex": rollstat(), "con": rollstat(), "int": rollstat(), "wis": rollstat(), "cha": rollstat()}
            elif statblock["con"] < 12:
                statblock = {"str": rollstat(), "dex": rollstat(), "con": rollstat(), "int": rollstat(), "wis": rollstat(), "cha": rollstat()}
            else:
                statsokay = "y"
        elif prio == "ranged":
            if statblock["dex"] < 12:
                statblock = {"str": rollstat(), "dex": rollstat(), "con": rollstat(), "int": rollstat(), "wis": rollstat(), "cha": rollstat()}
            elif statblock["con"] < 12:
                statblock = {"str": rollstat(), "dex": rollstat(), "con": rollstat(), "int": rollstat(), "wis": rollstat(), "cha": rollstat()}
            else:
                statsokay = "y"
        elif prio == "caster":
            if statblock["int"] < 12:
                statblock = {"str": rollstat(), "dex": rollstat(), "con": rollstat(), "int": rollstat(), "wis": rollstat(), "cha": rollstat()}
            elif statblock["wis"] < 12:
                statblock = {"str": rollstat(), "dex": rollstat(), "con": rollstat(), "int": rollstat(), "wis": rollstat(), "cha": rollstat()}
            else:
                statsokay = "y"
    return statblock