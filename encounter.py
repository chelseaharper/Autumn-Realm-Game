import pygame
import config
import utilities
import menus

class Battle():
    def __init__(self, screen, monsters, player):
        self.screen = screen
        self.monsters = monsters
        self.monsters.image = pygame.transform.scale(self.monsters.image, (config.SCALE * 5, config.SCALE * 5))
        self.player = player
        self.state = "active"
    
    def load_battle(self):
        pass

    def render_battle(self):
        self.screen.fill(config.white)
        rect = pygame.Rect(300, 50, config.SCALE * 10, config.SCALE * 10)
        self.screen.blit(self.monsters.image, rect)

        font = pygame.font.Font(None, 45)
        monster_health = font.render("Health: " + str(self.monsters.health), True, config.black)
        self.screen.blit(monster_health, (300, 200))
        attack_text = font.render("A monster appears!", True, config.black)
        self.screen.blit(attack_text, (25, 150))
        menus.attack_button.draw(self.screen)
        menus.run_button.draw(self.screen)
    
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
                self.state = "ended"