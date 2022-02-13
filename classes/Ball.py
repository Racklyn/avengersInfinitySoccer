import math
from tkinter.tix import Tree
import pygame, consts

class Ball:
    def __init__(self, x, y, radius, color, deceleration, goalposts):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 0
        self.color = color
        self.deceleration = deceleration
        self.isBlocked = False
        self.goalposts = goalposts

        self.isTouching = {
            'top': False,
            'right': False,
            'bottom': False,
            'left': False
        }

        self.xSpeed, self.ySpeed = 0, 0
        self.counter = 0


    def updateAndDraw (self, screen):
        
        newSpeed = self.speed - self.deceleration
        if newSpeed > 0:

            self.xSpeed *= (newSpeed/self.speed)
            self.ySpeed *= (newSpeed/self.speed)
            self.speed = newSpeed

            self.updatePosition(self.x + self.xSpeed, self.y + self.ySpeed)
        else:
            self.speed = 0

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def updatePosition(self, newX, newY):

        if self.goalposts.hasTouchedLeftGoalpost(self.x, self.y, self.radius):#newX - self.radius <= consts.GOALPOSTS_DEPTH:
            self.x = self.radius + consts.GOALPOSTS_DEPTH +1
            # self.isTouching['left'] = True
            self.xSpeed = -self.xSpeed
            # if self.y == player.y:
            #     player.x = 2*self.radius + player.radius
        elif self.goalposts.hasTouchedRightGoalpost(self.x, self.y, self.radius):#newX + self.radius >= consts.SCREEN_WIDTH - consts.GOALPOSTS_DEPTH:
            self.x = consts.SCREEN_WIDTH - self.radius - consts.GOALPOSTS_DEPTH -1
            # self.isTouching['Right'] = True
            self.xSpeed = -self.xSpeed
            # if self.y == player.y:
            #     player.x = consts.SCREEN_WIDTH - (2*self.radius + player.radius)
        else:
            self.x = newX

        if newY - self.radius <= 0:
            self.y = self.radius
            self.ySpeed = -self.ySpeed
            # if self.x == player.x:
            #     player.y = 2*self.radius + player.radius
        elif newY + self.radius >= consts.SCREEN_HEIGHT:
            self.y = consts.SCREEN_HEIGHT - self.radius
            self.ySpeed = -self.ySpeed
            # if self.y == player.y:
            #     player.y = consts.SCREEN_WIDTH - (2*self.radius + player.radius)
        else:
            self.y = newY      


    
    def handlePlayerTouch(self, player):
        # verificar se Player tocou na bola:
        minDist = self.radius + player.radius
        dist = math.hypot(self.x - player.x, self.y - player.y)
        # if dist <= minDist: # Jogador está tocando na bola
            # player.isTouchingBall = True
        #if player.isTouchingBall:


            # if player.x < self.x and player.y == self.y:
            #     self.isTouching['left'] = True
            # elif player.x > self.x and player.y == self.y:
            #     self.isTouching['right'] = True

            # if player.y < self.y and player.x == self.x:
            #     self.isTouching['bottom'] = True
            # elif player.y > self.y and player.x == self.x:
            #     self.isTouching['top'] = True


        if self.isBlocked:
            self.speed = 0
            
        else:
            self.speed = player.kickSpeed
        
        print(self.speed)

        xD = self.x - player.x
        yD = self.y - player.y

        newXD = minDist * xD/dist
        newYD = minDist * yD/dist

        self.xSpeed = self.speed * (self.x - player.x) / dist
        self.ySpeed = self.speed * (self.y - player.y) / dist

        self.updatePosition(player.x + newXD, player.y + newYD)


        # else:
        #     player.isTouchingBall = False
           
            
    def resetIsTouching(self, fill = False):
        self.isTouching = {
            'top': fill,
            'right': fill,
            'bottom': fill,
            'left': fill
        }