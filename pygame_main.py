import pygame
import characterbuilder
import bestiary
import itemoptions
import game
import config
import utilities
import map_functions
from time import sleep
import pygame_menu
from pygame_menu import themes

pygame.init()

screen = pygame.display.set_mode((config.screen_width, config.screen_height))
game_menu = False

pygame.display.set_caption("Autumn's Realm")
map = map_functions.Map()
#map.load_map("map01")
game_state = utilities.GameState.NONE
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

mainmenu = pygame_menu.Menu("Autumn's Realm", 600, 400, theme=themes.THEME_DEFAULT)
mainmenu.add.button('Play', start_game)
mainmenu.add.button('Load', load_game)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))

update_start = pygame.USEREVENT + 0

while game_state != utilities.GameState.ENDED:
    clock.tick(50)
    if game_menu == True:
        events = pygame.event.get()
        mainmenu.update(events)
        mainmenu.draw(screen)
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                     exit()
            elif event.type == update_start:
                mainmenu.close(start_game())
                print("Outside Start Game Function!")
    elif game_menu == False and gameinstance.playstate == utilities.PlayState.MENU:
        gameinstance.set_up()
        game_state = utilities.update_game_state(game_state)
        if gameinstance.playstate == utilities.PlayState.MAP:
            gameinstance.update()
        elif gameinstance.playstate == utilities.PlayState.BATTLE:
            pass
    pygame.display.flip()
