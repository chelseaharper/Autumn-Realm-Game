import pygame
import config
import utilities
import menus
import time

class Battle():
    def __init__(self, screen, monsters, player):
        self.screen = screen
        self.monsters = monsters
        self.monsters.image = pygame.transform.scale(self.monsters.image, (config.SCALE * 5, config.SCALE * 5))
        self.player = player
        self.state = "active"
        self.escape_failed = 0

    def render_battle(self):
        self.screen.fill(config.white)
        rect = pygame.Rect(325, 35, config.SCALE * 10, config.SCALE * 10)
        self.screen.blit(self.monsters.image, rect)

        font = pygame.font.Font(None, 45)
        monster_health = font.render("Monster Health: " + str(self.monsters.health), True, config.black)
        self.screen.blit(monster_health, (325, 200))
        monster_health = font.render("Player Health: " + str(self.player.getHP("current")) + "/" + str(self.player.getHP("max")), True, config.black)
        self.screen.blit(monster_health, (200, 375))
        attack_text = font.render("A monster appears!", True, config.black)
        self.screen.blit(attack_text, (25, 50))
        menus.attack_button.draw(self.screen)
        menus.run_button.draw(self.screen)
        if self.escape_failed > 0:
            failed_text = font.render("Unable to escape!", True, config.black)
            self.screen.blit(failed_text, (50, 75))
            self.escape_failed -= 1
    
    def update(self):
        for event in pygame.event.get():
            if event == pygame.quit:
                utilities.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    utilities.end_game()
            elif menus.attack_button.draw(self.screen):
                self.monsters.health -= 1
                if self.monsters.health <= 0:
                    self.state = "ended"
            elif menus.run_button.draw(self.screen):
                escape = self.player.roll_check("dex")
                block = self.monsters.roll_check("dex")
                if escape >= block:
                    self.escape_failed = 0
                    self.state = "ended"
                else:
                    self.escape_failed = 50