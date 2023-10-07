import pygame
import config

pygame.font.init()
large_font = pygame.font.Font(None, 45)
small_font = pygame.font.Font(None, 30)


class Button:
    def __init__(self, x, y, name, image_name1, width, height):
        self.position = [x, y]
        self.width = width
        self.height = height
        self.image = pygame.image.load(f"images/{image_name1}.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.Rect(self.position[0], self.position[1], width, height)
        self.name = name
        self.image_name1 = image_name1
        self.clicked = False
        self.text = large_font.render(name, True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (
            self.position[0] + (width // 2),
            self.position[1] + (height // 2),
        )

    def render(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.textRect)

    def handle_events(self):
        # Get the mouse position
        action = False
        position = pygame.mouse.get_pos()
        # Check if the mouse is over the button and has been clicked
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

class Menu:
    def __init__(self, name, x, y, button_names, button_image, button_width, button_height, orientation="vertical"):
        self.name = name
        self.position = [x, y]
        self.button_names = button_names
        self.buttons = []
        self.button_image = button_image
        self.button_width = button_width
        self.button_height = button_height
        self.orientation = orientation
        self.create_buttons()
    
    def create_buttons(self):
        for i, name in enumerate(self.button_names):
            x_pos = self.position[0] + 100
            y_pos = self.position[1] + (i * (self.button_height + 10))
            button = Button(x_pos, y_pos, name, self.button_image, self.button_width, self.button_height)
            self.buttons.append(button)
    
    def set_up(self):
        self.create_buttons()
    
    def render_menu(self, screen):
        for i in self.buttons:
            i.render(screen)

class TextMenu(Menu):
    def __init__(self, name, x, y, button_names, button_image, button_width, button_height, text, text_x, text_y, font=small_font):
        super().__init__(name, x, y, button_names, button_image, button_width, button_height)
        self.text = text
        self.text_position = [text_x, text_y]
        self.font = font
        self.textdisplay = self.create_text()
    
    def create_text(self):
        textdisplay = TextDisplay(
                    self.text_position[0],
                    self.text_position[1],
                    (config.screen_width / 2),
                    (config.screen_height / 2),
                    self.text,
                    self.font,
                    config.white)
        return textdisplay
    
    def render_menu(self, screen):
        self.textdisplay.render(screen)
        super().render_menu(screen)

class TextDisplay:
    def __init__(self, x, y, width, height, text, font, color):
        self.text = text
        self.width = width
        self.height = height
        self.position = [x, y]
        self.background = pygame.image.load("images/panel_blue.png")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.text = text
        self.font = font
        self.color = color
    
    def update_text(self, newtext):
        self.text = newtext
    
    def render(self, screen):
        screen.blit(self.background, self.rect)
        for text in self.text:
            words = [word.split(" ") for word in text.splitlines()]
            space = self.font.size(" ")[0]
            max_width, max_height = (self.width, self.height)
            if self.font.render(text, 0, self.color).get_size() > (max_width, max_height):
                x, y = (self.position[0] + 5, self.position[1] + 5)
                for line in words:
                    for word in line:
                        word_surface = self.font.render(word, True, self.color)
                        word_width, word_height = word_surface.get_size()
                        if x + word_width >= max_width:
                            x = self.position[0] + 5
                            y += word_height
                        screen.blit(word_surface, (x, y))
                        x += word_width + space
                    x = self.position[0]
                    y += word_height
            else:
                screen_text = self.font.render(text, True, (255, 255, 255))
                word_width, word_height = screen_text.get_size()
                self.textRect = screen_text.get_rect()
                self.textRect.center = (
                self.position[0] + (self.width // 2),
                self.position[1] + (50) + (self.text.index(text) * word_height),
                )
                screen.blit(screen_text, self.textRect)

stats = ["These will be some stats.", "This is some text."]

start_menu = Menu("Start", 75, 175, ["Start Game", "Load Game", "Quit Game"], "button", 250, 50)
class_select = Menu("Class", 75, 175, ["Fighter", "Archer", "Wizard"], "button", 250, 50)
playing_game = Menu("Play", 75, 175, ["Resume Game", "Load Game", "Save Game", "Quit Game"], "button", 250, 50)
