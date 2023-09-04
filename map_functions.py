import pygame
import config


class Map():
    def __init__(self):
        self.maplist = []

    def load_map(self, file_name):
        with open("D:/Python learning materials and programs/Text Autumn Realm Game/images/" + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])

                self.maplist.append(tiles)
    
    def render_map(self, screen, game):
        game.determine_camera()
        y_pos = 0
        for line in self.maplist:
            x_pos = 0
            for tile in line:
                image = map_tile_images[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE, config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos += 1
            y_pos += 1

map_tile_images = {
    config.MAP_TILE_GRASS : pygame.transform.scale(pygame.image.load("D:/Python learning materials and programs/Pokemon Clone/images/Used/tileGrass1.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_WATER : pygame.transform.scale(pygame.image.load("D:/Python learning materials and programs/Pokemon Clone/images/Used/rpgTile029.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ROAD : pygame.transform.scale(pygame.image.load("D:/Python learning materials and programs/Pokemon Clone/images/Used/rpgTile024.png"), (config.SCALE, config.SCALE))
    }