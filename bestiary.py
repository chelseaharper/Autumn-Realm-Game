import characterbuilder
import itemoptions
import random


def choosemonster(environment):
    if environment == "Grassland":
        monstertype = random.choice([goblin, slime])
    elif environment == "Mountains":
        monstertype = random.choice([goblin, orc])
    elif environment == "Fairy Forest":
        monstertype = random.choice([fairy, fairyguard])
    elif environment == "Swamp":
        monstertype = random.choice([goblin, orc])
    elif environment == "Cave":
        monstertype = random.choice([goblin, orc])
    elif environment == "Forest":
        monstertype = random.choice([goblin, orc])
    elif environment == "Town":
        monstertype = random.choice([mayor])
    monster = characterbuilder.Monster(monstertype[0], monstertype[1], monstertype[2], monstertype[3], monstertype[4], monstertype[5], monstertype[6], monstertype[7], monstertype[8])
    return monster

#Monsters
goblin = ["Goblin", characterbuilder.buildstatblock("melee"), 8, itemoptions.leather, 1, itemoptions.sword, 200, [], 0]
orc = ["Orc", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0]
fairy = ["Fairy", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0]
fairyguard = ["Fairy", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0]
slime = ["Slime", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0]
fairyqueen = ["Fairy Queen", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0]
# goblin = characterbuilder.Monster("Goblin", characterbuilder.buildstatblock("melee"), 8, itemoptions.leather, 1, itemoptions.sword, 200, [], 0)
# orc = characterbuilder.Monster("Orc", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0)
# fairy = characterbuilder.Monster("Fairy", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0)
# fairyguard = characterbuilder.Monster("Fairy", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0)
# slime = characterbuilder.Monster("Slime", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0)
# fairyqueen = characterbuilder.Monster("Fairy Queen", characterbuilder.buildstatblock("melee"), 8, itemoptions.chain, 1, itemoptions.sword, 300, [], 0)

#NPCs
mayor = characterbuilder.NPC("Mayor", characterbuilder.buildstatblock("commoner"), 6, itemoptions.clothes, 1, itemoptions.fists, 20, [], 0, "Friendly")