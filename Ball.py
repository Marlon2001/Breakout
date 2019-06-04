import pygame
import configparser

class Ball(object):
    config = configparser.ConfigParser()
    config.read("config.ini")

    directionBall = dict(config['config'])

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    LIGHTYELLOW = (255, 204, 0)

    def __init__(self, x, y, d, vx, vy, radius, wallX, wallY, list_brick):
        self.x = x
        self.y = y
        self.dir = d
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.list_collisions = [{'W' : wallX}, {'H' : wallY}, list_brick]

    def move(self, Game):
        if self.dir == Ball.directionBall["d1"]:
            self.x -= self.vx
            self.y -= self.vy
        if self.dir == Ball.directionBall["d3"]: 
            self.x += self.vx
            self.y -= self.vy
        if self.dir == Ball.directionBall["d2"]:
            self.x -= self.vx
            self.y += self.vy
        if self.dir == Ball.directionBall["d4"]:
            self.x += self.vx
            self.y += self.vy
        self.collide(Game)

    def collide(self, Game):
        for i in self.list_collisions:
            if isinstance(i, dict):
                if i.get('W'):
                    wallX = i.get('W')
                    if self.x <= 0 or self.x >= wallX:
                        self.calculateTragectory('w')
                elif i.get('H'):
                    wallY = i.get('H')
                    if self.y <= 0 or self.y >= wallY:
                        self.calculateTragectory('h')
            elif isinstance(i, list):
                for brick in i:
                    collide = False

                    if (self.y >= brick.y) and (self.y <= (brick.y + brick.height)) and \
                       (self.x >= brick.x) and (self.x <= (brick.x + brick.height)):
                        self.calculateTragectory('w')
                        collide = True
                    elif (self.y >= brick.y) and (self.y <= (brick.y + brick.height)) and \
                       (self.x >= brick.x) and (self.x <= (brick.x + brick.width)):
                        self.calculateTragectory('h')
                        collide = True
                    
                    if collide:
                        try:
                            Game.LIST_BRICK.remove(brick)
                        except:
                            continue
                
    def calculateTragectory(self, i):
        if i == 'w' and self.dir == Ball.directionBall["d1"]:
            self.dir = Ball.directionBall["d3"]
        elif i == 'w' and self.dir == Ball.directionBall["d3"]:
            self.dir = Ball.directionBall["d1"]
        elif i == 'w' and self.dir == Ball.directionBall["d2"]:
            self.dir = Ball.directionBall["d4"]
        elif i == 'w' and self.dir == Ball.directionBall["d4"]:
            self.dir = Ball.directionBall["d2"]
        elif i == 'h' and self.dir == Ball.directionBall["d3"]:
            self.dir = Ball.directionBall["d4"]
        elif i == 'h' and self.dir == Ball.directionBall["d1"]:
            self.dir = Ball.directionBall["d2"]
        elif i == 'h' and self.dir == Ball.directionBall["d4"]:
            self.dir = Ball.directionBall["d3"]
        elif i == 'h' and self.dir == Ball.directionBall["d2"]:
            self.dir = Ball.directionBall["d1"]

    def draw(self, surface):
        pygame.draw.circle(surface, Ball.BLUE, (self.x, self.y), self.radius, 0)
    
    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)