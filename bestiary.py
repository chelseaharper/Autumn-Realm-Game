import characterbuilder
import itemoptions
import random


def choosemonster(environment):
    if environment == "Grassland":
        monster = random.choice([goblin, slime])
        return monster
    elif environment == "Mountains":
        monster = random.choice([goblin, orc])
        return monster
    elif environment == "Fairy Forest":
        monster = random.choice([fairy, fairyguard])
        return monster
    elif environment == "Swamp":
        monster = random.choice([goblin, orc])
        return monster
    elif environment == "Cave":
        monster = random.choice([goblin, orc])
        return monster
    elif environment == "Forest":
        monster = random.choice([goblin, orc])
        return monster
    elif environment == "Town":
        monster = random.choice([mayor])
        return monster

#Monsters
goblin = characterbuilder.Monster("Goblin", characterbuilder.buildstatblock("melee"), 8, itemoptions.leather, 1, itemoptions.sword, 200, [])
orc = characterbuilder.Monster("Orc", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [])
fairy = characterbuilder.Monster("Fairy", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [])
fairyguard = characterbuilder.Monster("Fairy", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [])
slime = characterbuilder.Monster("Slime", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [])
fairyqueen = characterbuilder.Monster("Fairy Queen", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [])

#NPCs
mayor = characterbuilder.NPC("Mayor", characterbuilder.buildstatblock("commoner"), 6, itemoptions.clothes, 1, itemoptions.fists, 20, [], "Friendly")