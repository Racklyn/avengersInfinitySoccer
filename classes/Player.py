import math
import pygame, consts

class Player:
    def __init__(self, x, y, radius, speed, color, kickSpeed, score=0):
        self.x = x
        self.y = y
        self.xInitial = x
        self.yInitial = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.kickSpeed = kickSpeed
        self.isTouchingBall = False
        self.score = score

        self.isMoving = False
        
    def setToInitialPosition(self):
        self.x = self.xInitial
        self.y = self.yInitial

    def draw (self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def handleTouchOtherPlayer(self, otherPlayer):

        if not self.isMoving: return

        minDist = self.radius + otherPlayer.radius
        dist = math.hypot(self.x - otherPlayer.x, self.y - otherPlayer.y)
        if dist <= minDist: # Jogador está tocando no outro jogador
            xD = self.x - otherPlayer.x
            yD = self.y - otherPlayer.y

            newXD = minDist * xD/dist
            newYD = minDist * yD/dist

            self.updatePosition(otherPlayer.x + newXD, otherPlayer.y + newYD)


    def updatePosition(self, newX, newY):
        if newX - self.radius < 0:
            self.x = self.radius
        elif newX + self.radius > consts.SCREEN_WIDTH:
            self.x = consts.SCREEN_WIDTH - self.radius
        else:
            self.x = newX

        if newY - self.radius < consts.TOP_MENU_HEIGHT:
            self.y = self.radius + consts.TOP_MENU_HEIGHT
        elif newY + self.radius > consts.SCREEN_HEIGHT:
            self.y = consts.SCREEN_HEIGHT - self.radius
        else:
            self.y = newY  


    def events (self, up, down, left, right):

        self.isMoving = False
        xInc,yInc = 0,0

        if pygame.key.get_pressed()[up]:
            yInc -= self.speed
        if pygame.key.get_pressed()[down]:
            yInc += self.speed
        if pygame.key.get_pressed()[left]:
            xInc -= self.speed
        if pygame.key.get_pressed()[right]:
            xInc += self.speed

        if not (xInc==yInc==0):
            self.isMoving = True

        if not (xInc==0 or yInc==0):
            xInc /= math.sqrt(2)
            yInc /= math.sqrt(2)
        


        self.updatePosition(self.x + xInc, self.y + yInc)
