from enum import Enum
import pygame

class GameState(Enum):
    NONE = 0,
    RUNNING = 1,
    ENDED = 2

class PlayState(Enum):
    MENU = 0,
    MAP = 1,
    BATTLE = 2

def update_game_state(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = GameState.ENDED
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state = GameState.ENDED
    return state