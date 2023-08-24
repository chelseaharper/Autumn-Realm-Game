from random import randint

class Weapon:
    def __init__(self, damagedie):
        self.damagedie = damagedie

class Melee(Weapon):
    def __init__(self, damagedie):
        super().__init__(damagedie)
        self.type = "physical"

    def swing(self,  weilder):
        return randint(1, 20) + weilder.melee
    
    def damage (self, weilder):
        return randint(1, self.damagedie) + weilder.melee
    

class Ranged(Weapon):
    def __init__(self, damagedie):
        super().__init__(damagedie)
        self.type = "physical"

    def swing(self,  weilder):
        return randint(1, 20) + weilder.ranged
    
    def damage (self, weilder):
        return randint(1, self.damagedie) + weilder.ranged

class Caster(Weapon):
    def __init__(self, damagedie):
        super().__init__(damagedie)
        self.type = "magical"

    def swing(self,  weilder):
        return randint(1, 20) + weilder.caster
    
    def damage (self, weilder):
        return randint(1, self.damagedie) + weilder.caster

class Armor():
    def __init__(self, defense):
        self.defense = defense
    
    def setAC(self):
        pass

class Physical(Armor):
    def __init__(self, defense):
        super().__init__(defense)
        self.type = "physical"

    def setAC(self, wearer):
        return wearer.getAC(self.type) + self.defense
        

class Magical(Armor):
    def __init__(self, defense):
        super().__init__(defense)
        self.type = "magical"
    
    def setAC(self, wearer):
        return wearer.getAC(self.type) + self.defense

sword = Melee(8)
bow = Ranged(6)
wand = Caster(4)
leather = Physical(3)
chain = Physical(4)
padded = Physical(2)