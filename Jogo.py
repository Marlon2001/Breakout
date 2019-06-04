import pygame
import random
import time
import sys
from pygame.locals import *
from Ball import Ball
from Board import Board
from Brick import Brick
import configparser

class Game(object):
    config = configparser.ConfigParser()
    config.read("config.ini")

    directionBall = dict(config['config'])

    BGCOLOR = (47, 79, 79)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    LIGHTYELLOW = (255, 204, 0)
    LIST_BRICK = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 500))
        pygame.display.set_caption("Breakout Game!")
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.board = Board(200, self.screen.get_height()-40, 100, 20)
        Game.LIST_BRICK = self.createBricks(70, 23, 90)
        self.ball = Ball(self.screen.get_width() // 2, (self.screen.get_height() // 2)+150, Game.directionBall["d1"], 1, 1, 10, self.screen.get_width(), self.screen.get_height(), Game.LIST_BRICK)
        
        self.pause = False
        self.score = 0

    def run(self):
        while True:
            if self.pause:
                self.pauseGame()
                continue

            self.clock.tick(280)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE:
                        if self.pause:
                            self.pause = False
                        else:
                            self.pause = True

            #print(self.score)
            self.ball.move(Game)
            self.board.move()
            self.draw()

    def draw(self):
        self.screen.fill(Game.BGCOLOR)
        self.ball.draw(self.screen)
        self.board.draw(self.screen)
        for brick in Game.LIST_BRICK:
            brick.draw(self.screen)
        pygame.display.update()

    def createBricks(self, width, height, n):
        list_brick = []
        posX = 0
        posY = 30
        distBorda = 25
        
        x = 0
        z = width
        while z > distBorda:
            z -= 1
            x -= 1

        for i in range(1, n+1):
            if i == 1:
                posX += x + width
            else:
                posX += width

            if (posX + width) > self.screen.get_width() - distBorda:
                posY += height
                posX = distBorda
                
            brick = Brick(posX, posY, width, height)
            list_brick.append(brick)
        return list_brick

    def pauseGame(self):
        event = pygame.event.wait()
        if event.type == K_SPACE:
            self.pause = False

