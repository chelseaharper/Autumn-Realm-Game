import pygame
import config
import characterbuilder
import menu_creator
import utilities
import bestiary
import itemoptions
import map_functions
import random
import encounter

class Game:
    def __init__(self, screen, maps, menus):
        self.playstate = utilities.PlayState.MENU
        self.map = map_functions.Map()
        self.maps = maps
        self.menus = menus
        self.current_menu = self.menus[0]
        self.screen = screen
        self.player = None
        self.objects = []
        self.camera = [0, 0]
        self.player_moved = False
        self.battle = None
    
    def determine_camera(self):
        pass

    def change_map(self, map):
        self.map.load_map(map)
    
    def update(self):
        if self.playstate == utilities.PlayState.MENU:
            self.handle_menu_events()
            self.current_menu.render_menu(self.screen)

        elif self.playstate == utilities.PlayState.MAP:
            self.player_moved = False
            self.screen.fill(config.black)
            self.handle_map_events()

            self.map.render_map(self.screen, self)

            for object in self.objects:
                object.render(self.screen, self.camera)
            
            if self.player_moved:
                self.determine_game_events()

        elif self.playstate == utilities.PlayState.BATTLE:
            self.battle.update()
            self.battle.render_battle()
            if self.battle.playerstate == "dead" and self.battle.monster_hit_player == 0:
                utilities.end_game()
            elif self.battle.state == "ended" and self.battle.playerstate == "run" and self.battle.escape_failed == 0:
                self.playstate = utilities.PlayState.MAP
            elif self.battle.state == "ended" and self.battle.playerstate == "won" and self.battle.player_hit_monster == 0:
                stat_increase = self.player.getXP(self.battle.monster)
                if stat_increase:
                    self.playstate = utilities.PlayState.STATMENU
                else:
                    self.playstate = utilities.PlayState.MAP
        
        elif self.playstate == utilities.PlayState.STATMENU:
            if self.player.type == "Fighter":
                self.player.raise_stat("CON")
            elif self.player.type == "Archer":
                self.player.raise_stat("DEX")
            elif self.player.type == "Wizard":
                self.player.raise_stat("INT")
            self.playstate = utilities.PlayState.MAP
    
    def set_up(self, map_name, charclass, charstats, player):
            character = charcreator(player, charclass, charstats)
            self.player = character
            self.objects.append(character)
            self.playstate = utilities.PlayState.MAP
            self.map.load_map(map_name)
    
    def get_player_name(self):
        name = ""
        small_font = pygame.font.Font(None, 30)
        player_name_text = small_font.render("Please input your character's name.", True, (255, 255, 255))
        player_name_textRect = player_name_text.get_rect()
        player_name_textRect.center = (config.screen_width//2, 25)
        
        name_input_rect = pygame.Rect(200, 200, 320, 50)

        self.screen.fill(config.black)
        pygame.draw.rect(self.screen, config.white, name_input_rect, 4)
        self.screen.blit(player_name_text, player_name_textRect)
        text_screen = small_font.render(name, False, (255, 255, 255))
        self.screen.blit(text_screen, (name_input_rect.x +5, name_input_rect.y +5))

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
        
        

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif self.current_menu.name == "Name":
                name = self.player[2]
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                        self.player[2] = name
                        name_text = ["Please enter your character's name:", self.player[2]]
                        self.current_menu = menu_creator.TextMenu("Name", 275, 175, ["Confirm"], "button", 150, 50, name_text, 20, 20, font=menu_creator.large_font)
                    else:
                        name += event.unicode
                        self.player[2] = name
                        name_text = ["Please enter your character's name:", self.player[2]]
                        self.current_menu = menu_creator.TextMenu("Name", 275, 175, ["Confirm"], "button", 150, 50, name_text, 20, 20, font=menu_creator.large_font)

        for i in self.current_menu.buttons:
            if i.handle_events():
                if i.name == "Quit Game":
                    exit()
                elif i.name == "Start Game":
                    pygame.time.wait(150)
                    self.current_menu = self.menus[1]
                elif i.name == "Resume Game":
                    pygame.time.wait(150)
                    self.playstate = utilities.PlayState.MAP
                elif i.name == "Save Game":
                    pygame.time.wait(150)
                    print("Save Not Implemented")
                elif i.name == "Load Game":
                    pygame.time.wait(150)
                    print("Load Not Implemented")
                elif i.name == "Fighter":
                    pygame.time.wait(150)
                    self.player = [[1, "melee"]]
                    self.player.append(characterbuilder.buildstatblock(self.player[0][1]))
                    stats = []
                    for key, value in self.player[1].items():
                        stats.append(f"{key}:  {value}")
                    self.current_menu = menu_creator.TextMenu("Stats", 275, 175, ["Yes", "No"], "button", 100, 50, stats, 20, 20, font=menu_creator.large_font)
                elif i.name == "Archer":
                    pygame.time.wait(150)
                    self.player = [[2, "ranged"]]
                    self.player.append(characterbuilder.buildstatblock(self.player[0][1]))
                    stats = []
                    for key, value in self.player[1].items():
                        stats.append(f"{key}:  {value}")
                    self.current_menu = menu_creator.TextMenu("Stats", 275, 175, ["Yes", "No"], "button", 100, 50, stats, 20, 20, font=menu_creator.large_font)
                elif i.name == "Wizard":
                    pygame.time.wait(150)
                    self.player = [[3, "caster"]]
                    self.player.append(characterbuilder.buildstatblock(self.player[0][1]))
                    stats = []
                    for key, value in self.player[1].items():
                        stats.append(f"{key}:  {value}")
                    self.current_menu = menu_creator.TextMenu("Stats", 275, 175, ["Yes", "No"], "button", 100, 50, stats, 20, 20, font=menu_creator.large_font)
                elif i.name == "No":
                    pygame.time.wait(150)
                    self.player.pop()
                    self.player.append(characterbuilder.buildstatblock(self.player[0][1]))
                    stats = []
                    for key, value in self.player[1].items():
                        stats.append(f"{key}:  {value}")
                    self.current_menu = menu_creator.TextMenu("Stats", 275, 175, ["Yes", "No"], "button", 100, 50, stats, 20, 20, font=menu_creator.large_font)
                elif i.name == "Yes":
                    pygame.time.wait(150)
                    self.player.append("")
                    name_text = ["Please enter your character's name:", self.player[2]]
                    self.current_menu = menu_creator.TextMenu("Name", 275, 175, ["Confirm"], "button", 150, 50, name_text, 20, 20, font=menu_creator.large_font)
                elif i.name == "Confirm":
                    if self.player[2] == "":
                        pass
                    else:
                        self.set_up("map01", self.player[0][0], self.player[1], self.player[2])
                        self.playstate == utilities.PlayState.MAP
                        pygame.time.wait(150)
                        self.current_menu = self.menus[2]
                    
    
    def handle_map_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                utilities.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playstate = utilities.PlayState.MENU
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
        if new_position[1] < 0 or new_position[1] > ((len(self.map.maplist)) - 1):
            return
        if self.map.maplist[new_position[1]][new_position[0]] in config.IMPASSIBLE:
            return
        if self.map.maplist[new_position[1]][new_position[0]] == "T":
            self.player.changehealth(self.player.getHP("max")) #Change so it loads a new map based on position
        
        self.player_moved = True
        unit.update_position(new_position)

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