import pygame
import characterbuilder
import bestiary
import itemoptions
import utilities
import config
import map_functions
import random
import encounter

class Game():
    def __init__(self, screen, map):
        self.screen = screen
        self.objects = []
        self.playstate = utilities.PlayState.MENU
        self.map = map
        self.camera = [0, 0]
        self.player_moved = False
        self.battle = None
    
    def set_up(self, charclass, charstats, player):
        character = charcreator(player, charclass, charstats)
        self.player = character
        self.objects.append(character)
        self.playstate = utilities.PlayState.MAP
        self.map.load_map("map01")
    
    def determine_camera(self):
        pass
    
    def change_map(self, map):
        self.map.load_map(map)

    def update(self):
        if self.playstate == utilities.PlayState.MAP:
            self.player_moved = False
            self.screen.fill(config.black)
            self.handle_events()

            self.map.render_map(self.screen, self)

            for object in self.objects:
                object.render(self.screen, self.camera)
            
            if self.player_moved:
                print("MOVED!")
                self.determine_game_events()
        elif self.playstate == utilities.PlayState.BATTLE:
            self.battle.update()
            self.battle.render_battle()
            if self.battle.playerstate == "dead" and self.battle.monster_hit_player == 0:
                utilities.end_game()
            elif self.battle.state == "ended" and self.battle.playerstate == "won" and self.battle.player_hit_monster == 0:
                stat_increase = self.player.getXP(self.battle.monster)
                if stat_increase:
                    self.playstate = utilities.PlayState.STATMENU
                else:
                    self.playstate = utilities.PlayState.MAP
        elif self.playstate == utilities.PlayState.STATMENU:
            if self.player.type == "Fighter":
                self.player.raise_stat("con")
            elif self.player.type == "Archer":
                self.player.raise_stat("dex")
            elif self.player.type == "Wizard":
                self.player.raise_stat("int")
            self.playstate = utilities.PlayState.MAP
    
    def determine_game_events(self):
        map_tile = self.map.maplist[self.player.position[1]][self.player.position[0]]

        if map_tile == config.MAP_TILE_ROAD:
            return
        if map_tile == config.MAP_TILE_TOWN:
            return
        
        self.determine_monster(map_tile)
    
    def determine_monster(self, tile):
        random_number = random.randint(1, 10)
        if random_number <= 2:
            match tile:
                case "G":
                    monsterhome = "Grassland"
                case "M":
                    monsterhome = "Mountains"
                case "f":
                    monsterhome = "Fairy Forest"
                case "S":
                    monsterhome = "Swamp"
                case "c":
                    monsterhome = "Cave"
                case "F":
                    monsterhome = "Forest"
                case "t":
                    monsterhome = "Town"
            found_monster = bestiary.choosemonster(monsterhome)

            self.battle = encounter.Battle(self.screen, found_monster, self.player)
            self.playstate = utilities.PlayState.BATTLE
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                utilities.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    utilities.end_game()
                elif event.key == pygame.K_w or event.key == pygame.K_UP: #move up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN: #move down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT: #move left
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT: #move right
                    self.move_unit(self.player, [1, 0])
    
    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
        if new_position[0] < 0 or new_position[0] > (len(self.map.maplist[0]) - 1):
            return
        if new_position[1] < 0 or new_position[1] > ((len(self.map.maplist) / 2) - 1):
            return
        if self.map.maplist[new_position[1]][new_position[0]] in config.IMPASSIBLE:
            return
        if self.map.maplist[new_position[1]][new_position[0]] == "T":
            self.player.changehealth(self.player.getHP("max")) #Change so it loads a new map based on position
        
        self.player_moved = True
        unit.update_position(new_position)

    def get_monster(self):
        pass

#Update and move this function as appropriate to interface with a visual UI
def charcreator(charname, charclass, stats):
    if (charclass == 1):
        hdie = 10
        armor = itemoptions.chain
        weapon = itemoptions.sword
        playerclass = "Fighter"
    elif charclass == 2:
        hdie = 8
        armor = itemoptions.leather
        weapon = itemoptions.bow
        playerclass = "Archer"
    elif charclass == 3:
        hdie = 6
        armor = itemoptions.padded
        weapon = itemoptions.wand
        playerclass = "Wizard"
    return characterbuilder.Player(charname, playerclass, stats, hdie, armor, 1, weapon, [], 0, 1, 1)