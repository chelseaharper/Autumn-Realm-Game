import pygame
import characterbuilder
import bestiary
import itemoptions
import utilities
import config
import map

class Game():
    def __init__(self, screen, map):
        self.screen = screen
        self.state = utilities.GameState.NONE
        self.map = map
    
    def set_up(self):
        self.state = utilities.GameState.RUNNING
    
    def update(self):
        self.screen.fill(config.black)
        self.handle_events()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = utilities.GameState.ENDED
    
    def get_monster(self):
        pass