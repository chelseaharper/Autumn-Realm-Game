from time import sleep
import pygame
import buttons
import config

pygame.init()

start_menu_img = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/Start.png")
start_button = buttons.Button(50, 200, start_menu_img)
quit_menu_img = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/Quit.png")
quit_button = buttons.Button(350, 200, quit_menu_img)
figher_img = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/Fighter.png")
figher_button = buttons.Button((config.screen_width // 2), 150, figher_img)
archer_img = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/Archer.png")
archer_button = buttons.Button((config.screen_width // 2), 250, archer_img)
wizard_img = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/Wizard.png")
wizard_button = buttons.Button((config.screen_width // 2), 350, wizard_img)
yes_img = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/Yes.png")
yes_button = buttons.Button(400, 100, yes_img)
no_img = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/No.png")
no_button = buttons.Button(400, 300, no_img)

attack_img = pygame.transform.scale(pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/Attack.png"), (config.SCALE * 5, config.SCALE * 2.5))
attack_button = buttons.Button(150, 275, attack_img)
run_img = pygame.transform.scale(pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/Run.png"), (config.SCALE * 5, config.SCALE * 2.5))
run_button = buttons.Button(325, 275, run_img)

font = pygame.font.Font(None, 45)
startscreen_text = font.render("Welcome to Autumn's Realm!", True, config.white)
startscreen_textRect = startscreen_text.get_rect()
startscreen_textRect.center = (config.screen_width//2, 100)

charclass_text = font.render("Please select a class", True, config.white)
charclass_textRect = charclass_text.get_rect()
charclass_textRect.center = (config.screen_width//2, 50)

stats_text = font.render("Are these stats okay?", True, config.white)
stats_textRect = stats_text.get_rect()
stats_textRect.center = (config.screen_width//2, 25)

player_name_text = font.render("Please input your character's name.", True, config.white)
player_name_textRect = player_name_text.get_rect()
player_name_textRect.center = (config.screen_width//2, 25)

name_input_rect = pygame.Rect(200, 200, 320, 50)

def display_stats(statblock):
    str_text = font.render("Strength: " + str(statblock["str"]), True, config.white)
    str_textRect = str_text.get_rect()
    str_textRect.center = (150, 75)
    
    dex_text = font.render("Dexterity: " + str(statblock["dex"]), True, config.white)
    dex_textRect = dex_text.get_rect()
    dex_textRect.center = (150, 150)
    
    con_text = font.render("Constitution: " + str(statblock["con"]), True, config.white)
    con_textRect = con_text.get_rect()
    con_textRect.center = (150, 225)
    
    int_text = font.render("Intelligence: " + str(statblock["int"]), True, config.white)
    int_textRect = int_text.get_rect()
    int_textRect.center = (150, 300)
    
    wis_text = font.render("Wisdom: " + str(statblock["wis"]), True, config.white)
    wis_textRect = wis_text.get_rect()
    wis_textRect.center = (150, 375)
    
    cha_text = font.render("Charisma: " + str(statblock["cha"]), True, config.white)
    cha_textRect = cha_text.get_rect()
    cha_textRect.center = (150, 450)
    return {str_text:str_textRect, dex_text:dex_textRect, con_text:con_textRect, int_text:int_textRect, wis_text:wis_textRect, cha_text:cha_textRect}

