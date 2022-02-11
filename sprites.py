import math
from turtle import speed
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


    def handleTouchOtherPlayer(self, otherPlayer):
        # verificar se Player tocou na bola:
        minDist = self.radius + otherPlayer.radius
        dist = math.hypot(self.x - otherPlayer.x, self.y - otherPlayer.y)
        if dist <= minDist: # Jogador está tocando no outro jogador
            xD = self.x - otherPlayer.x
            yD = self.y - otherPlayer.y

            newXD = minDist * xD/dist
            newYD = minDist * yD/dist

            self.newPositionVerif(otherPlayer.x + newXD, otherPlayer.y + newYD)


    def newPositionVerif(self, newX, newY):
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

        isMoving = False
        xInc,yInc = 0,0

        if pygame.key.get_pressed()[up]:
            yInc -= self.speed
            isMoving = True
        if pygame.key.get_pressed()[down]:
            yInc += self.speed
            isMoving = True
        if pygame.key.get_pressed()[left]:
            xInc -= self.speed
            isMoving = True
        if pygame.key.get_pressed()[right]:
            xInc += self.speed
            isMoving = True


        if not (xInc==0 or yInc==0):
            xInc /= math.sqrt(2)
            yInc /= math.sqrt(2)


        self.newPositionVerif(self.x + xInc, self.y + yInc)

        return isMoving




class Ball:
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color


    def draw (self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    
    def hadlePlayerTouch(self, player):
        # verificar se Player tocou na bola:
        minDist = self.radius + player.radius
        dist = math.hypot(self.x - player.x, self.y - player.y)
        if dist <= minDist: # Jogador está tocando na bola
            xD = self.x - player.x
            yD = self.y - player.y

            newXD = minDist * xD/dist
            newYD = minDist * yD/dist


            newX = player.x + newXD
            newY = player.y + newYD

            #essa parte ficará em uma função separada, para verificar sempre que a bola estiver em movimento
            if newX - self.radius <= 0:
                self.x = self.radius
                if self.y == player.y:
                    player.x = 2*self.radius + player.radius
            elif newX + self.radius >= consts.SCREEN_WIDTH:
                self.x = consts.SCREEN_WIDTH - self.radius
                if self.y == player.y:
                    player.x = consts.SCREEN_WIDTH - (2*self.radius + player.radius)
            else:
                self.x = newX

            if newY - self.radius <= 0:
                self.y = self.radius
                if self.x == player.x:
                    player.y = 2*self.radius + player.radius
            elif newY + self.radius >= consts.SCREEN_HEIGHT:
                self.y = consts.SCREEN_HEIGHT - self.radius
                if self.y == player.y:
                    player.y = consts.SCREEN_WIDTH - (2*self.radius + player.radius)
            else:
                self.y = newY            


            Vx = self.speed * (self.x - player.x) / dist
            Vy = self.speed * (self.y - player.y) / dist




# def handleCircleColision(c1, c2): # c1: stopped; c2: moving
#     minDist = c1.radius + c2.radius
#     dist = math.hypot(c1.x - c2.x, c1.y - c2.y)
#     if dist <= minDist: # Jogador está tocando na bola
#         xD = c1.x - c2.x
#         yD = c1.y - c2.y

#         newXD = minDist * xD/dist
#         newYD = minDist * yD/dist


#         newX = c2.x + newXD
#         newY = c2.y + newYD

#         #essa parte ficará em uma função separada, para verificar sempre que a bola estiver em movimento
#         if newX - c1.radius <= 0:
#             c1.x = c1.radius
#             if c1.y == c2.y:
#                 c2.x = 2*c1.radius + c2.radius
#         elif newX + c1.radius >= consts.SCREEN_WIDTH:
#             c1.x = consts.SCREEN_WIDTH - c1.radius
#             if c1.y == c2.y:
#                 c2.x = consts.SCREEN_WIDTH - (2*c1.radius + c2.radius)
#         else:
#             c1.x = newX

#         if newY - c1.radius <= 0:
#             c1.y = c1.radius
#             if c1.x == c2.x:
#                 c2.y = 2*c1.radius + c2.radius
#         elif newY + c1.radius >= consts.SCREEN_HEIGHT:
#             c1.y = consts.SCREEN_HEIGHT - c1.radius
#             if c1.y == c2.y:
#                 c2.y = consts.SCREEN_WIDTH - (2*c1.radius + c2.radius)
#         else:
#             c1.y = newY          


#         Vx = c1.speed * (c1.x - c2.x) / dist
#         Vy = c1.speed * (c1.y - c2.y) / dist