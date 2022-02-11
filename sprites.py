from math import sqrt
import pygame, consts

class Player:
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        


    def draw (self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def onTouchBall(ball):
        pass


    def events (self, up, down, left, right):

        xInc,yInc = 0,0

        if pygame.key.get_pressed()[up]:
            yInc -= self.speed
        if pygame.key.get_pressed()[down]:
            yInc += self.speed
        if pygame.key.get_pressed()[left]:
            xInc -= self.speed
        if pygame.key.get_pressed()[right]:
            xInc += self.speed


        if not (xInc==0 or yInc==0):
            xInc /= sqrt(2)
            yInc /= sqrt(2)

        newX = self.x + xInc
        newY = self.y + yInc

        if newY < self.radius:
            self.y = self.radius
        elif newY > consts.SCREEN_HEIGHT - self.radius:
            self.y = consts.SCREEN_HEIGHT - self.radius
        else:
            self.y = newY

        if newX < self.radius:
            self.x = self.radius
        elif newX > consts.SCREEN_WIDTH - self.radius:
            self.x = consts.SCREEN_WIDTH - self.radius
        else:
            self.x = newX




class Ball:
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color


    def draw (self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    