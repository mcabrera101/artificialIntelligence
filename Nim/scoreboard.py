import pygame
import rgbcolors
import random

class ScoreBoard:
    def __init__(self, screen):
        self._screen = screen
        (w, h) = screen.get_size()
        self._dimension = (w-100, h/16)
        self.location = 0
        self._score = str(0)

    def calcScore(self, game):
        #self._score =
        print("score is: {}".format(self._score))
       
        
    def draw(self):
        score_font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self._scoreR = score_font.render('Score: %s' % (self._score), True, rgbcolors.black)
        self._score_pos = self._scoreR.get_rect(topleft=self._dimension)
        self.location = (self._score_pos.x,self._score_pos.x)
        self._screen.blit(self._scoreR, self._score_pos)
        
        