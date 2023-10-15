import pygame
import menu_creator
import game
import pygame



pygame.font.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Autumn's Realm")
clock = pygame.time.Clock()


game_instance = game.Game(screen,
                              ["map01"],
                                 [
                                  menu_creator.start_menu,
                                  menu_creator.class_select,
                                  menu_creator.playing_game
                                  ]
                             )

while True:
    clock.tick(50)
    screen.fill((0, 0, 0))
    game_instance.update()
    pygame.display.flip()