import pygame
import config
import utilities
import menus
import time
from operator import itemgetter
import characterbuilder

class Battle():
    def __init__(self, screen, monster, player):
        self.screen = screen
        self.monster = monster
        self.monster.image = pygame.transform.scale(self.monster.image, (config.SCALE * 5, config.SCALE * 5))
        self.player = player
        self.playerstate = "alive"
        self.state = "active"
        self.escape_failed = 0
        self.monster_hit_player = 0
        self.player_hit_monster = 0
        self.combat_started = 50
        self.player_turn = False
        self.monster_turn = False
        self.attack_result = 0
        self.order = []
        self.set_up()
    
    def set_up(self):
        combatants = [self.monster, self.player]
        for i in combatants:
            i.rollinit()
            self.order.append([i.init, i])
        self.order = sorted(self.order, key=itemgetter(0), reverse=True)
        if type(self.order[0][1]) == characterbuilder.Monster:
            self.monster_turn = True
        elif type(self.order[0][1]) == characterbuilder.Player:
            self.player_turn = True

    def render_battle(self):
        self.screen.fill(config.white)
        rect = pygame.Rect(325, 35, config.SCALE * 10, config.SCALE * 10)
        self.screen.blit(self.monster.image, rect)

        font = pygame.font.Font(None, 45)
        monster_health = font.render("Monster Health: " + str(self.monster.health), True, config.black)
        self.screen.blit(monster_health, (325, 200))
        monster_health = font.render("Player Health: " + str(self.player.getHP("current")) + "/" + str(self.player.getHP("max")), True, config.black)
        self.screen.blit(monster_health, (200, 375))
        attack_text = font.render("A monster appears!", True, config.black)
        self.screen.blit(attack_text, (25, 50))
        if self.monster_turn:
            monster_turn_text = font.render("The monster attacks!", True, config.black)
            self.screen.blit(monster_turn_text, (25, 100))
            self.attack(self.monster, self.player)
            self.monster_turn = False
            self.player_turn = True
        elif self.player_turn:
            menus.attack_button.draw(self.screen)
            menus.run_button.draw(self.screen)
        if self.escape_failed > 0:
            failed_text = font.render("Unable to escape!", True, config.black)
            self.screen.blit(failed_text, (50, 150))
            self.escape_failed -= 1
        if self.player_hit_monster > 0:
            player_hit_text = font.render("You hit the monster!", True, config.black)
            self.screen.blit(player_hit_text, (50, 150))
            self.player_hit_monster -= 1
            if self.player_hit_monster == 0:
                self.player_turn = False
                self.monster_turn = True
        if self.monster_hit_player > 0:
            monster_hit_text = font.render("The monster hit you!", True, config.black)
            self.screen.blit(monster_hit_text, (50, 75))
            self.monster_hit_player -= 1
        if self.player_hit_monster < 0:
            player_missed_text = font.render("You missed the monster!", True, config.black)
            self.screen.blit(player_missed_text, (50, 150))
            self.player_hit_monster += 1
            if self.player_hit_monster == 0:
                self.player_turn = False
                self.monster_turn = True
        if self.monster_hit_player < 0:
            monster_missed_text = font.render("The monster missed you!", True, config.black)
            self.screen.blit(monster_missed_text, (50, 75))
            self.monster_hit_player += 1
    
    def attack(self, attacker, defender):
        attroll = attacker.weapon.swing(attacker)
        opposedAC = defender.getAC(attacker.weapon.type)
        success = 0
        if attroll - attacker.melee == 20:
            damage = attacker.weapon.damage(attacker) + attacker.weapon.damage(attacker)
            defender.changehealth(-damage)
            success = 1
        elif attroll >= opposedAC:
            damage = attacker.weapon.damage(attacker)
            defender.changehealth(-damage)
            success = 1
        if type(attacker) == characterbuilder.Player:
            if success == 0:
                self.player_hit_monster = -30
            elif success == 1:
                self.player_hit_monster = 30
        elif type(attacker) == characterbuilder.Monster:
            if success == 0:
                self.monster_hit_player = -30
            elif success == 1:
                self.monster_hit_player = 30
        

    def update(self):
        if self.monster.health <= 0:
            self.state = "ended"
        if self.player.health <= 0:
            self.playerstate = "dead"
            self.state = "ended"
        for event in pygame.event.get():
            if event == pygame.quit:
                utilities.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    utilities.end_game()
            elif self.player_turn and menus.attack_button.draw(self.screen):
                self.attack(self.player, self.monster)
                
            elif menus.run_button.draw(self.screen):
                escape = self.player.roll_check("dex")
                block = self.monster.roll_check("dex")
                if escape >= block:
                    self.escape_failed = 0
                    self.state = "ended"
                else:
                    self.escape_failed = 50
