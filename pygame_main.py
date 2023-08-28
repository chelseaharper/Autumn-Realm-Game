import pygame
import characterbuilder
import bestiary
import itemoptions
import game
import config
import utilities

pygame.init()

screen = pygame.display.set_mode((config.screen_width, config.screen_height))

pygame.display.set_caption("Autumn's Realm")

clock = pygame.time.Clock()
gameinstance = game.Game(screen)
gameinstance.set_up()

while gameinstance.state == utilities.GameState.RUNNING:
    clock.tick(50)
    gameinstance.update()
    pygame.display.flip()