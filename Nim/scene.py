
import pygame
import rgbcolors


class Scene:
    def __init__(self, screen):
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(rgbcolors.purple)
        self._is_valid = True

    
    def draw(self):
        self._screen.blit(self._background, (0, 0))
    
    def process_event(self, event):
        print(str(event))
        if event.type == pygame.QUIT:
            print('Good Bye!')
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print('Bye bye!')
            self._is_valid = False

    def is_valid(self):
        return self._is_valid
    
    def update(self):
        pass


class TitleScene(Scene):
    def __init__(self, screen, title, title_color, title_size):
        super().__init__(screen)
        self._background.fill(rgbcolors.pink)
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, title_color)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any key.', True, rgbcolors.black)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(w/2, h/2))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w/2, h - 50))
    
    def draw(self):
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)
    
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self._is_valid = False


class DescriptionScene(Scene):
    def __init__(self, screen, description, description_color, description_size):
        super().__init__(screen)
        self._description = description
        self._description_color = description_color
        self._description_size = description_size
        self._background.fill(rgbcolors.pink)
        title_font = pygame.font.Font(pygame.font.get_default_font(), description_size)
        self._title = title_font.render(description[0], True, description_color)
        self._title2 = title_font.render(description[1], True, description_color)
        self._title3 = title_font.render(description[2], True, description_color)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any key.', True, rgbcolors.black)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(w / 2, h / 2))
        self._title2_pos = self._title2.get_rect(center=(w / 2, h -75))
        self._title3_pos = self._title3.get_rect(center=(w / 2, h -100))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w / 2, h - 50))


    def draw(self):
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._title2, self._title2_pos)
        self._screen.blit(self._title3, self._title3_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)


    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self._is_valid = False

class GameLevel(Scene):
    def __init__(self, screen, clock, scoreboard, nimDisplay, inputBox):
        super().__init__(screen)
        self._background.fill(rgbcolors.aquamarine)
        self._screen = screen
        self._scoreboard = scoreboard
        self.clock = clock
        self._nimDisplay = nimDisplay
        self._inputBox = inputBox


    def gameOver(self):
        pass
            
    
    def draw(self):
        super().draw()
        #self._scoreboard.draw()
        self._nimDisplay.draw()
        self._inputBox.draw()


    def process_event(self, event):
        super().process_event(event)
        self._inputBox.process_event(event)
        self._nimDisplay.setMove(self._inputBox.getEntered())
        self._nimDisplay.process_event(event)

    def update(self):
        print("tick " + str(pygame.time.get_ticks()))
        self._inputBox.update()








        
