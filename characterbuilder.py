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
        self.health += healthchange

    def attack(self, enemy):
        if self.weapon.type == "spell":
            AC = enemy.touchAC
        else:
            AC = enemy.AC
        attroll = self.weapon.swing(self)
        print(self.gettype() + " attacks the " + enemy.gettype() + ". The roll is " + str(attroll) + "! " + enemy.gettype() + " has " + str(AC) +" AC.")
        if attroll >= AC:
            print("The attack hits!")
            enemy.changehealth(-self.weapon.damage(self))
            print(self.gettype() + " has " + str(self.health) + " hit points left!")
            print(enemy.gettype() + " has " + str(enemy.health) + " hit points left!")
        else:
            print("The attack misses!")
            print(self.gettype() + " has " + str(self.health) + " hit points left!")
            print(enemy.gettype() + " has " + str(enemy.health) + " hit points left!")
    
    def setAC(self):
        self.AC = self.armor.setAC(self)
    
    def setTouchAC(self):
        self.touchAC = self.armor.setAC(self)
    
    def sethealth(self):
        self.health = self.hitdie + ((randint(1, self.hitdie)) * (self.level - 1)) + self.getstatmod("con")
    
    def getAC(self, type):
        if type == "physical":
            return self.AC
        elif type == "magical":
            return self.touchAC
    
    def getstatmod(self, stat):
        return (self.stats[stat] - 10)//2

    def getHP(self):
        return self.health
    
    def gettype(self):
        return self.type

class Player(Creature):
    def __init__(self, name, type, stats, hitdie, armor, level, weapon):
        super().__init__(type, stats, hitdie, armor, level, weapon)
        self.name = name
    
    def gettype(self):
        return self.name

class Monster(Creature):
    def __init__(self, type, stats, hitdie, armor, level, weapon):
        super().__init__(type, stats, hitdie, armor, level, weapon)
    
    def sethealth(self):
        self.health = (getaverage(self.hitdie) + self.getstatmod("con")) * self.level

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