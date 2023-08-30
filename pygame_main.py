import pygame
import characterbuilder
import bestiary
import itemoptions
import game
import config
import utilities
import map_functions

pygame.init()

screen = pygame.display.set_mode((config.screen_width, config.screen_height))

pygame.display.set_caption("Autumn's Realm")
map = map_functions.Map()
map.load_map("map01")

clock = pygame.time.Clock()
gameinstance = game.Game(screen, map)
gameinstance.set_up()

while gameinstance.state == utilities.GameState.RUNNING:
    clock.tick(50)
    gameinstance.update()
    pygame.display.flip()