import math
import pygame, consts

class Player:
    def __init__(self, x, y, radius, speed, color, kickSpeed):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.kickSpeed = kickSpeed
        self.isTouchingBall = False

        self.isMoving = False
        

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

        if newY - self.radius < 0:
            self.y = self.radius
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


    # def handleBothSidesBallTouch(self, ball, goalposts):
    #     if self.isTouchingBall:
    #         if (ball.isTouching["left"] and ball.isTouching["right"]):
    #             if (self.x > ball.x):
    #                 self.x = ball.x + ball.radius + self.radius
    #             else:
    #                 self.x = ball.x - ball.radius - self.radius
            
    #         if (ball.isTouching["top"] and ball.isTouching["bottom"]):
    #             if (self.y > ball.y):
    #                 self.y = ball.y + ball.radius + self.radius
    #             else:
    #                 self.y = ball.y - ball.radius - self.radius