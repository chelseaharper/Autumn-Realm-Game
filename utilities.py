from enum import Enum
import pygame

class GameState(Enum):
    NONE = 0,
    RUNNING = 1,
    ENDED = 2

class PlayState(Enum):
    MENU = 0,
    MAP = 1,
    BATTLE = 2,
    STATMENU = 3

game_state = GameState.NONE

def end_game():
    game_state = GameState.ENDED
    exit()