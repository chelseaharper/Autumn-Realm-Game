from operator import itemgetter
from tkinter import messagebox
import sys
import characterbuilder
import itemoptions

#Character Creation Functions: these functions are used for creating, displaying, and updating player characters in the game.
def statsokay(prio):
    charstats = characterbuilder.buildstatblock(prio)
    print("Your player stats are: " + str(charstats))
    answer = input("Would you like to reroll? (y/n)")
    while answer == "y":
        charstats = characterbuilder.buildstatblock(prio)
        print("Your player stats are: " + str(charstats))
        answer = input("Would you like to reroll? (y/n)")
    return charstats

def charcreator():
    charclass = int(input("What class would you like to play?\n1. fighter\n2. archer\n3. wizard\n"))
    if (charclass == 1):
        playerstats = statsokay("melee")
        hdie = 10
        armor = itemoptions.chain
        weapon = itemoptions.sword
        playerclass = "Fighter"
    elif charclass == 2:
        playerstats = statsokay("ranged")
        hdie = 8
        armor = itemoptions.leather
        weapon = itemoptions.bow
        playerclass = "Archer"
    elif charclass == 3:
        playerstats = statsokay("caster")
        hdie = 6
        armor = itemoptions.padded
        weapon = itemoptions.wand
        playerclass = "Wizard"
    
    charname = input("What would you like to name your character? ")
    return characterbuilder.Player(charname, playerclass, playerstats, hdie, armor, 1, weapon)

def levelup(player):
    print("You have gained a level!")
    player.raiselevel()
    displayplayer(player)

def displayplayer(player):
    print("------------------------------")
    print("Name: " + player.gettype() + "\tlevel " + str(player.level) + " " + player.type)
    print("HP: " + str(player.getHP("current")) + "/" + str(player.getHP("max")) + "\nAC: " + str(player.getAC("physical")) + "\nTouch AC: " + str(player.getAC("magical")))

#Combat Functions: these functions are used for managing combat encounters between the player and other characters in the game.
def attack(attacker, defender):
    print("The " + attacker.gettype() + " attacks!")
    attroll = attacker.weapon.swing(attacker)
    opposedAC = defender.getAC(attacker.weapon.type)
    if attroll - attacker.melee == 20:
        print("It's a crit!")
        damage = attacker.weapon.damage(attacker) + attacker.weapon.damage(attacker)
        defender.changehealth(-damage)
        print("The " + defender.gettype() + " takes " + str(damage) + " damage. The " + defender.gettype() + "'s HP is " + str(defender.getHP("current")) + ".\n")
    elif attroll >= opposedAC:
        print("The attack hits!")
        damage = attacker.weapon.damage(attacker)
        defender.changehealth(-damage)
        print("The " + defender.gettype() + " takes " + str(damage) + " damage. The " + defender.gettype() + "'s HP is " + str(defender.getHP("current")) + ".\n")
    else:
        print("The attack misses!\n")

def combat(combatants):
    XPearned = 0
    order = []
    for i in combatants:
        i.rollinit()
        order.append([i.init, i])
    order = sorted(order, key=itemgetter(0), reverse=True)
    fight = True
    while fight == True:
        for i in order:
            nextchar = order[(order.index(i) + 1) % len(order)]
            if type(i[1]) == characterbuilder.Player:
                swing = input("Would you like to attack? ")
                if swing == "y":
                    print(str(len(order) - 1) + " enemies are attacking you.\n")
                    enemies = []
                    counter = 1
                    for j in order:
                        if type(j[1]) == characterbuilder.Monster:
                            print(str(counter) + ". " + j[1].gettype() + "\n")
                            enemies.append([counter, j])
                            counter += 1
                    target = int(input("Which enemy would you like to attack? "))
                    nextchar = order[order.index(enemies[target - 1][1])]
                    attack(i[1], nextchar[1])
                elif swing == "n":
                    print("You run away!")
                    fight = False
                    break
                if nextchar[1].health <= 0:
                    print("The " + nextchar[1].gettype() + " dies!")
                    XPearned += nextchar[1].XP
                    order.remove(nextchar)
                if len(order) <= 1:
                    fight = False
                    print("You won the fight! You gain " + str(XPearned) + " experience points!")
                    i[1].currXP += XPearned
                    break
            elif type(i[1]) == characterbuilder.Monster:
                hasswung = False
                while hasswung == False:
                    if type(nextchar[1]) == characterbuilder.Player:
                        hasswung = True
                        attack(i[1], nextchar[1])
                        if nextchar[1].health <= 0:
                            print("You have died.")
                            order.remove(nextchar)
                            input("Thanks for playing Autumn's Realm! Hit any key to exit.")
                            sys.exit()
                        if len(order) <= 1:
                            fight = False
                            break
                    else:
                        nextchar = order[(order.index(nextchar) + 1) % len(order)]

#Non-Combat Functions: these functions are used for managing encounters between the player and other characters in the game which do not
# involve combat. The non-combat encounter may result in combat depending on the result, but that would call a combat function.
def negotiate(player, target):
    pass
#Main functionality of the game
def main():
    playgame = input("Would you like to play Autumn's Realm? (y/n) ")
    if playgame == "y" or "Y":
        print("Let's create a character.")
        player = charcreator()
        displayplayer(player)
        input("Press any key to begin.")
        monsterstats = characterbuilder.buildstatblock("melee")
        monster1 = characterbuilder.Monster("Goblin", monsterstats, 8, itemoptions.leather, 1, itemoptions.sword, 200)
        monster2 = characterbuilder.Monster("Orc", monsterstats, 8, itemoptions.chain, 1, itemoptions.sword, 300)
        fighters = [player, monster1, monster2]
        combat(fighters)
        if player.currXP == player.needXP:
            levelup(player)
        input("Thanks for playing Autumn's Realm! Hit any key to exit.")

    else:
        input("Thanks for playing Autumn's Realm! Hit any key to exit.")

if __name__ == "__main__":
    main()