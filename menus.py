from time import sleep
import pygame
import buttons
import config

pygame.init()
# surface = pygame.display.set_mode((600, 400))

# def set_difficulty(value, difficulty):
#     print(value)
#     print(difficulty)

# def start_the_game():
#     mainmenu._open(loading)
#     pygame.time.set_timer(update_loading, 30)

# def level_menu():
#     mainmenu._open(level)


# mainmenu = pygame_menu.Menu('Welcome', 600, 400, theme=themes.THEME_SOLARIZED)
# mainmenu.add.text_input('Name: ', default='username')
# mainmenu.add.button('Play', start_the_game)
# mainmenu.add.button('Levels', level_menu)
# mainmenu.add.button('Quit', pygame_menu.events.EXIT)

# level = pygame_menu.Menu('Select a Difficulty', 600, 400, theme=themes.THEME_BLUE)
# level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)

# loading = pygame_menu.Menu('Loading the Game...', 600, 400, theme=themes.THEME_DARK)
# loading.add.progress_bar("Progress", progressbar_id = "1", default=0, width = 200, )

# arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))

# update_loading = pygame.USEREVENT + 0

# while True:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == update_loading:
#             progress = loading.get_widget("1")
#             progress.set_value(progress.get_value() + 1)
#             if progress.get_value() == 100:
#                 pygame.time.set_timer(update_loading, 0)
#         if event.type == pygame.QUIT:
#             exit()

#     if mainmenu.is_enabled():
#         mainmenu.update(events)
#         mainmenu.draw(surface)
#         if (mainmenu.get_current().get_selected_widget()):
#             arrow.draw(surface, mainmenu.get_current().get_selected_widget())

#     pygame.display.update()

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
yes_button = buttons.Button(100, 300, yes_img)
no_img = pygame.image.load("D:/Python learning materials and programs/Text Autumn Realm Game/images/No.png")
no_button = buttons.Button(100, 100, no_img)

font = pygame.font.Font(None, 50)
startscreen_text = font.render("Welcome to Autumn's Realm!", True, config.white)
startscreen_textRect = startscreen_text.get_rect()
startscreen_textRect.center = (config.screen_width//2, 100)

charclass_text = font.render("Please select a class", True, config.white)
charclass_textRect = charclass_text.get_rect()
charclass_textRect.center = (config.screen_width//2, 50)

stats_text = font.render("Are these stats okay?", True, config.white)
stats_textRect = stats_text.get_rect()
stats_textRect.center = (config.screen_width//2, 50)