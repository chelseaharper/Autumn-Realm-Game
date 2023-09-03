import pygame
import characterbuilder
import bestiary
import itemoptions
import game
import config
import utilities
from utilities import game_state
import map_functions
from time import sleep
import buttons
import menus

pygame.init()

screen = pygame.display.set_mode((config.screen_width, config.screen_height))
game_menu = True
player_menu = False
charclass = 0
class_selected = False
stats_chosen = False

pygame.display.set_caption("Autumn's Realm")
map = map_functions.Map()
map.load_map("map01")
gameinstance = game.Game(screen, map)

clock = pygame.time.Clock()
def start_game():
    global game_menu
    global game_state

    game_menu= False
    gameinstance.set_up()
    game_state = utilities.update_game_state(game_state)

def load_game():
    pass

update_start = pygame.USEREVENT + 0
update_quit = pygame.USEREVENT + 1

while game_state != utilities.GameState.ENDED:
    clock.tick(50)
    if game_menu == True:
        screen.blit(menus.startscreen_text, menus.startscreen_textRect)
        for events in pygame.event.get():
            if menus.start_button.draw(screen):
                game_menu = False
                player_menu = True
            elif menus.quit_button.draw(screen):
                utilities.end_game()
    elif player_menu == True and class_selected == False:
        for events in pygame.event.get():
            screen.fill(config.black)
            screen.blit(menus.charclass_text, menus.charclass_textRect)
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    utilities.end_game()
            elif menus.figher_button.draw(screen):
                charclass = 1
#                game_state = utilities.GameState.RUNNING
                class_selected = True
                print(charclass)
#                player_menu = False
            elif menus.archer_button.draw(screen):
                charclass = 2
#                game_state = utilities.GameState.RUNNING
                class_selected = True
                print(charclass)
#                player_menu = False
            elif menus.wizard_button.draw(screen):
                charclass = 3
#                game_state = utilities.GameState.RUNNING
                class_selected = True
                print(charclass)
#                player_menu = False
    elif player_menu == True and class_selected == True and stats_chosen == False:
        for events in pygame.event.get():
            screen.fill(config.black)
            screen.blit(menus.stats_text, menus.stats_textRect)
#            charstats = game.statsokay(charclass)
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    utilities.end_game()
            elif menus.yes_button.draw(screen):
                reroll = 'y'
#                game_state = utilities.GameState.RUNNING
                stats_chosen = True
            elif menus.no_button.draw(screen):
                reroll = 'n'
#                game_state = utilities.GameState.RUNNING
            
    elif game_menu == False and gameinstance.playstate == utilities.PlayState.MENU:
        gameinstance.set_up(charclass)
        game_state = utilities.GameState.RUNNING
    if gameinstance.playstate == utilities.PlayState.MAP:
        gameinstance.update()
    elif gameinstance.playstate == utilities.PlayState.BATTLE:
        pass
    pygame.display.flip()
