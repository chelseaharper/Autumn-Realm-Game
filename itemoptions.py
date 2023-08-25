from random import randint

class Weapon:
    def __init__(self, damagedie, cost):
        self.damagedie = damagedie
        self.cost = cost

class Melee(Weapon):
    def __init__(self, name, damagedie, cost):
        super().__init__(damagedie, cost)
        self.type = "physical"
        self.name = name

    def swing(self,  weilder):
        return randint(1, 20) + weilder.melee
    
    def damage (self, weilder):
        return randint(1, self.damagedie) + weilder.melee
    

class Ranged(Weapon):
    def __init__(self, name, damagedie, cost):
        super().__init__(damagedie, cost)
        self.type = "physical"
        self.name = name

    def swing(self,  weilder):
        return randint(1, 20) + weilder.ranged
    
    def damage (self, weilder):
        return randint(1, self.damagedie) + weilder.ranged

class Caster(Weapon):
    def __init__(self, name, damagedie, cost):
        super().__init__(damagedie, cost)
        self.type = "magical"
        self.name = name

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
    def __init__(self, name, defense, cost):
        super().__init__(defense, cost)
        self.type = "physical"
        self.name = name

    def setAC(self, wearer):
        return wearer.getAC(self.type) + self.defense
        

class Magical(Armor):
    def __init__(self, name, defense, cost):
        super().__init__(defense, cost)
        self.type = "magical"
        self.name = name
    
    def setAC(self, wearer):
        return wearer.getAC(self.type) + self.defense

class Usable():
    def __init__(self, usedfor, cost):
        self.usedfor = usedfor
    
    def useitem(self, use, target):
        pass

class VendorTrash():
    def __init__(self, name, cost):
        self.cost = cost
        self.name = name

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
sword = Melee("sword", 8, 5)
bow = Ranged("bow", 6, 5)
wand = Caster("wand", 4, 5)
fists = Melee("fists", 4, 0)
leather = Physical("leather armor", 3, 10)
chain = Physical("chain armor", 4, 10)
padded = Physical("padded armor", 2, 10)
clothes = Physical("clothes", 0, 1)
curelight = Potion("Potion: Cure Light Wounds", "healing", 25, 8, 1)
inflictlight = Potion("Potion: Inflict Light Wounds", "damage", 25, 8, 1)