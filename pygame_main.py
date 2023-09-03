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

pygame.display.set_caption("Autumn's Realm")
map = map_functions.Map()
map.load_map("map01")
gameinstance = game.Game(screen, map)

font = pygame.font.Font(None, 50)
startscreen_text = font.render("Welcome to Autumn's Realm!", True, config.white)
startscreen_textRect = startscreen_text.get_rect()
startscreen_textRect.center = (config.screen_width//2, 100)

charclass_text = font.render("Press any key to select a class", True, config.white)
charclass_textRect = charclass_text.get_rect()
charclass_textRect.center = (config.screen_width//2, 50)


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
        screen.blit(startscreen_text, startscreen_textRect)
        for events in pygame.event.get():
            if menus.start_button.draw(screen):
                game_menu = False
                player_menu = True
            elif menus.quit_button.draw(screen):
                utilities.end_game()
    elif player_menu == True:
        for events in pygame.event.get():
            screen.fill(config.black)
            screen.blit(charclass_text, charclass_textRect)
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    utilities.end_game()
                else:
                    gameinstance.set_up()
                    game_state = utilities.GameState.RUNNING
                    player_menu = False
    elif game_menu == False and gameinstance.playstate == utilities.PlayState.MENU:
        gameinstance.set_up()
    if gameinstance.playstate == utilities.PlayState.MAP:
        gameinstance.update()
    elif gameinstance.playstate == utilities.PlayState.BATTLE:
        pass
    pygame.display.flip()
