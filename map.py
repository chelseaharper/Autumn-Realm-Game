import pygame
import config


class Map():
    def __init__(self, map):
        self.map = map

    def load_map(self, file_name):
        with open("D:/Python learning materials and programs/Pokemon Clone/images/maps/" + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])

                self.map.append(tiles)
            print(self.map)
    
    def render_map(self, screen):
        self.determine_camera()
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_images[tile]
                rect = pygame.Rect(x_pos * config.SCALE - (self.camera[0] * config.SCALE), y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos += 1
            y_pos += 1

map_tile_images = {
    "G" : pygame.transform.scale(pygame.image.load("D:/Python learning materials and programs/Pokemon Clone/images/Used/tileGrass1.png"), (config.SCALE, config.SCALE)),
    "W" : pygame.transform.scale(pygame.image.load("D:/Python learning materials and programs/Pokemon Clone/images/Used/rpgTile029.png"), (config.SCALE, config.SCALE))
    }