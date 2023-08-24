from random import randint

class Weapon:
    def __init__(self, damagedie, cost):
        self.damagedie = damagedie
        self.cost = cost

class Melee(Weapon):
    def __init__(self, damagedie, cost):
        super().__init__(damagedie, cost)
        self.type = "physical"

    def swing(self,  weilder):
        return randint(1, 20) + weilder.melee
    
    def damage (self, weilder):
        return randint(1, self.damagedie) + weilder.melee
    

class Ranged(Weapon):
    def __init__(self, damagedie, cost):
        super().__init__(damagedie, cost)
        self.type = "physical"

    def swing(self,  weilder):
        return randint(1, 20) + weilder.ranged
    
    def damage (self, weilder):
        return randint(1, self.damagedie) + weilder.ranged

class Caster(Weapon):
    def __init__(self, damagedie, cost):
        super().__init__(damagedie, cost)
        self.type = "magical"

    def swing(self,  weilder):
        return randint(1, 20) + weilder.caster
    
    def damage (self, weilder):
        return randint(1, self.damagedie) + weilder.caster

class Armor():
    def __init__(self, defense, cost):
        self.defense = defense
        self.cost = cost
    
    def setAC(self):
        pass

class Physical(Armor):
    def __init__(self, defense, cost):
        super().__init__(defense, cost)
        self.type = "physical"

    def setAC(self, wearer):
        return wearer.getAC(self.type) + self.defense
        

class Magical(Armor):
    def __init__(self, defense, cost):
        super().__init__(defense, cost)
        self.type = "magical"
    
    def setAC(self, wearer):
        return wearer.getAC(self.type) + self.defense

class Usable():
    def __init__(self, usedfor, cost):
        self.usedfor = usedfor
    
    def useitem(self, use, target):
        pass

class VendorTrash():
    def __init__(self, cost):
        self.cost = cost

class Potion(Usable):
    def __init__(self, name, usedfor, cost, die, modifier):
        super().__init__(usedfor, cost)
        self.name = name
        self.die = die
        self.modifier = modifier
    
    def useitem(self, target):
        effect = randint(1, self.die) + self.modifier
        if self.usedfor == "healing":
            target.changehealth(effect)
        elif self.usedfor == "damage":
            target.changehealth(-effect)

#Items available in game
sword = Melee(8, 5)
bow = Ranged(6, 5)
wand = Caster(4, 5)
leather = Physical(3, 10)
chain = Physical(4, 10)
padded = Physical(2, 10)
curelight = Potion("Potion: Cure Light Wounds", "healing", 25, 8, 1)
inflictlight = Potion("Potion: Inflict Light Wounds", "damage", 25, 8, 1)