from random import randint
import itemoptions
import pygame
import config



class Creature:
    def __init__(self, type, stats, hitdie, armor, level, weapon, items, money):
        self.type = type
        self.stats = stats
        self.armor = armor
        self.melee = self.getstatmod("STR")
        self.ranged = self.getstatmod("DEX")
        self.caster = self.getstatmod("INT")
        self.AC = 10 + (self.getstatmod("DEX"))
        self.touchAC = 10 + (self.getstatmod("DEX"))
        self.maxhealth = 0
        self.health = 0
        self.level = level
        self.hitdie = hitdie
        self.weapon = weapon
        self.init = 0
        self.items = items
        self.money = money
        self.stat_increase = 0
        self.updateitems([armor, weapon])
        self.sethealth()
        self.setAC()
    
    def rollinit(self):
        self.init = randint(1, 20) + self.getstatmod("DEX")
    
    def changehealth (self, healthchange):
        if self.health + healthchange > self.maxhealth:
            self.health = self.maxhealth
        else:
            self.health += healthchange
    
    def updateitems(self, additions):
        self.items += additions

    def setAC(self):
        self.AC = self.armor.setAC(self)
    
    def setTouchAC(self):
        self.touchAC = self.armor.setAC(self)
    
    def sethealth(self):
        self.health = self.hitdie + ((randint(1, self.hitdie)) * (self.level - 1)) + self.getstatmod("CON")
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
    
    def getitems(self):
        return self.items
    
    def roll_check(self, stat):
        return (randint(1, 20) + self.getstatmod(stat))

class Player(Creature):
    def __init__(self, name, type, stats, hitdie, armor, level, weapon, items, money, x_position, y_position):
        super().__init__(type, stats, hitdie, armor, level, weapon, items, money)
        self.name = name
        self.image = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/RPG_Kenney_Tiles/tile_0098.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.currXP = 0
        self.needXP = 0
        self.position = [x_position, y_position]
        self.setXPneeded()
    
    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]
    
    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * config.SCALE - (camera[0] * config.SCALE), self.position[1] * config.SCALE - (camera[1] * config.SCALE), config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)

    def gettype(self):
        return self.name
    
    def raiselevel(self):
        self.level += 1
        self.stats["CON"] += 0.25
        self.stat_increase += 0.25
        self.maxhealth += (randint(1, self.hitdie) + self.getstatmod("CON"))
        self.changehealth(getaverage(self.hitdie))
        self.setXPneeded()
        if self.stat_increase % 1 == 0:
            return True
    
    def setXPneeded(self):
        self.needXP += 500 * self.level

    def getHP(self, HPtype):
        if HPtype == "current":
            HP = self.health
        elif HPtype == "max":
            HP = self.maxhealth
        return HP
    
    def getXP(self, monster):
        self.currXP += monster.XP
        if self.currXP >= self.needXP:
            return self.raiselevel()
    
    def raise_stat(self, stat):
        self.stats[stat] += 1
        self.stat_increase -= 1

class Monster(Creature):
    def __init__(self, type, stats, hitdie, armor, level, weapon, XP, items, money, monster_image):
        super().__init__(type, stats, hitdie, armor, level, weapon, items, money)
        self.XP = XP
        self.image = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/RPG_Kenney_Tiles/" + monster_image + ".png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
    
    def sethealth(self):
        self.health = (getaverage(self.hitdie) + self.getstatmod("CON")) * self.level

class NPC(Monster):
    def __init__(self, type, stats, hitdie, armor, level, weapon, XP, items, money, attitude, monster_image):
        super().__init__(type, stats, hitdie, armor, level, weapon, XP, items, money, monster_image)
        self.attitudeoptions = ["Helpful", "Friendly", "Indifferent", "Unfriendly", "Hostile"]
        self.attitude = attitude
    
    def getDC(self):
        if self.attitude == "Hostile":
            DC = 12 + self.getstatmod("CHA")
        elif self.attitude == "Unfriendly":
            DC = 10 + self.getstatmod("CHA")
        elif self.attitude == "Indifferent":
            DC = 7 + self.getstatmod("CHA")
        elif self.attitude == "Friendly":
            DC = 5 + self.getstatmod("CHA")
        elif self.attitude == "Helpful":
            DC = 0 + self.getstatmod("CHA")
        return DC
    
    def getnextattitude(self, amount):
        if (self.attitudeoptions.index(self.attitude) - amount) < 0:
            self.attitude = self.attitudeoptions[0]
        elif (self.attitudeoptions.index(self.attitude) - amount) > len(self.attitudeoptions):
            self.attitude = self.attitudeoptions[(len(self.attitudeoptions) - 1)]
        else:
            self.attitude = self.attitudeoptions[(self.attitudeoptions.index(self.attitude) - amount)]

    def changeattitude(self, roll):
        DC = self.getDC()
        amount = 0
        if roll >= DC:
            amount += 1
            roll -= DC
            while roll > 4:
                amount +=1
                roll -=5
            self.attitude = self.getnextattitude(amount)
        elif roll < (DC - 4):
            amount -= 1
            self.attitude = self.getnextattitude(amount)
        else:
            pass
        return [amount, self.attitude]

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
        statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
        if prio == "melee":
            if statblock["STR"] < 12:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            elif statblock["CON"] < 12:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            else:
                statsokay = "y"
        elif prio == "ranged":
            if statblock["DEX"] < 12:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            elif statblock["CON"] < 12:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            else:
                statsokay = "y"
        elif prio == "caster":
            if statblock["INT"] < 12:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            elif statblock["WIS"] < 12:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            else:
                statsokay = "y"
        elif prio == "commoner":
            if statblock["STR"] > 14:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            elif statblock["DEX"] > 14:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            elif statblock["CON"] > 14:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            elif statblock["INT"] > 14:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            elif statblock["WIS"] > 14:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            elif statblock["CHA"] > 14:
                statblock = {"STR": rollstat(), "DEX": rollstat(), "CON": rollstat(), "INT": rollstat(), "WIS": rollstat(), "CHA": rollstat()}
            else:
                statsokay = "y"
    return statblock