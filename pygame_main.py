import sys
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
charstats = {}
player_named = False
player = ""

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
                charclass = [1, "melee"]
                charstats = characterbuilder.buildstatblock(charclass[1])
                class_selected = True
            elif menus.archer_button.draw(screen):
                charclass = [2, "ranged"]
                charstats = characterbuilder.buildstatblock(charclass[1])
                class_selected = True
            elif menus.wizard_button.draw(screen):
                charclass = [3, "caster"]
                charstats = characterbuilder.buildstatblock(charclass[1])
                class_selected = True
    elif player_menu == True and class_selected == True and stats_chosen == False:
        for events in pygame.event.get():
            screen.fill(config.black)
            stat_display = menus.display_stats(charstats)
            screen.blit(menus.stats_text, menus.stats_textRect)
            for k in stat_display:
                screen.blit(k, stat_display[k])
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    utilities.end_game()
            elif menus.yes_button.draw(screen):
                reroll = 'n'
                stats_chosen = True
            elif menus.no_button.draw(screen):
                reroll = 'y'
                charstats = characterbuilder.buildstatblock(charclass[1])         
    elif player_menu == True and class_selected == True and stats_chosen == True and player_named == False:
        screen.fill(config.black)
        pygame.draw.rect(screen, config.white, menus.name_input_rect, 4)
        screen.blit(menus.player_name_text, menus.player_name_textRect)
        text_screen = menus.font.render(player, False, (255, 255, 255))
        screen.blit(text_screen, (menus.name_input_rect.x +5, menus.name_input_rect.y +5))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                utilities.end_game()
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    utilities.end_game()
                elif events.key == pygame.K_BACKSPACE:
                    player = player[:-1]
                elif events.key == pygame.K_RETURN and player == "":
                    pass
                elif events.key == pygame.K_RETURN:
                    player_named = True
                else:
                    player += events.unicode
    elif game_menu == False and gameinstance.playstate == utilities.PlayState.MENU:
        gameinstance.set_up(charclass[0], charstats, player)
        game_state = utilities.GameState.RUNNING
    if gameinstance.playstate == utilities.PlayState.MAP:
        gameinstance.update()
    elif gameinstance.playstate == utilities.PlayState.BATTLE:
        gameinstance.update()
    pygame.display.flip()
