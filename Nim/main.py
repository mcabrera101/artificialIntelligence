
import pygame
from scene import *
from scoreboard import *
from NimDisplay import *
from game_of_nim import GameOfNim
from collections import namedtuple
from inBox import *

def main():

    pygame.init()
    GameState = namedtuple('GameState', 'to_move, utility, board, moves')
    GameState.to_move = ["max", "min"]
    GameState.board = [0, 5, 3, 1]

    nimGame = GameOfNim(GameState)

    window_size = (500, 400)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(window_size)
    title = 'NIM'
    description = ["write 2digit num. press enter to execute", "1st digit = column. 2digit = #tiles to remove","right arrow for AI move" ]


    pygame.display.set_caption(title)
    nim = nimDisplay(screen, nimGame)
    inBox = InputBox(0,0,50,50, screen)


    scoreboard = ScoreBoard(screen)

    scene_list = [TitleScene(screen, title, rgbcolors.green, 72), DescriptionScene(screen, description, rgbcolors.black,
                    20), GameLevel(screen, clock, scoreboard, nim, inBox)]
    
    for scene in scene_list:
        while scene.is_valid():
            
            for e in pygame.event.get():
                scene.process_event(e)

            scene.draw()
            scene.update()
            pygame.display.update()
        
    pygame.quit()