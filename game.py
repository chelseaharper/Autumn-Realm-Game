import pygame
import characterbuilder
import bestiary
import itemoptions
import utilities
import config

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.state = utilities.GameState.NONE
    
    def set_up(self):
        self.state = utilities.GameState.RUNNING
    
    def update(self):
        self.screen.fill(config.black)
        self.handle_events()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = utilities.GameState.ENDED