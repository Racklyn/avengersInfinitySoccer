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





class Ball:
    def __init__(self, x, y, radius, color, deceleration):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = 0
        self.color = color
        self.deceleration = deceleration

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

        if newX - self.radius <= consts.GOALPOSTS_DEPTH: #Goalposts.hasTouchedLeftGoalpost(self.x, self.y, self.radius)
            self.x = self.radius + consts.GOALPOSTS_DEPTH
            self.xSpeed = -self.xSpeed
            # if self.y == player.y:
            #     player.x = 2*self.radius + player.radius
        elif newX + self.radius >= consts.SCREEN_WIDTH - consts.GOALPOSTS_DEPTH:
            self.x = consts.SCREEN_WIDTH - self.radius - consts.GOALPOSTS_DEPTH
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
        if dist <= minDist: # Jogador está tocando na bola
            self.speed = player.kickSpeed

            xD = self.x - player.x
            yD = self.y - player.y

            newXD = minDist * xD/dist
            newYD = minDist * yD/dist

            self.updatePosition(player.x + newXD, player.y + newYD)

            self.xSpeed = self.speed * (self.x - player.x) / dist
            self.ySpeed = self.speed * (self.y - player.y) / dist



class Goalposts:
    def __init__(self, screen, size = consts.GOALPOSTS_SIZE, depth = consts.GOALPOSTS_DEPTH):
        self.screen = screen
        self.size = size
        self.depth = depth

        self.startY = consts.SCREEN_HEIGHT/2 - self.size/2
        self.finalY = consts.SCREEN_HEIGHT/2 + self.size/2
        #self.leftGoalpost = 

    
    def drawGoalposts(self):
        

        # Left goalpost
        pygame.draw.line(self.screen, consts.WHITE,
            (self.depth - 6, self.startY), (self.depth - 6, self.finalY), 6)
        pygame.draw.rect(self.screen, consts.BLACK, 
            (0, 0, self.depth, self.startY))
        pygame.draw.rect(self.screen, consts.BLACK, 
                (0, self.finalY, self.depth, consts.SCREEN_HEIGHT))
        

        # Right goalpost
        pygame.draw.line(self.screen, consts.WHITE,
            (consts.SCREEN_WIDTH - self.depth + 6, self.startY), 
            (consts.SCREEN_WIDTH - self.depth + 6, self.finalY), 6)
        pygame.draw.rect(self.screen, consts.BLACK, 
            (consts.SCREEN_WIDTH - self.depth, 0, consts.SCREEN_WIDTH, self.startY))
        pygame.draw.rect(self.screen, consts.BLACK, 
            (consts.SCREEN_WIDTH - self.depth, self.finalY, consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

    @staticmethod
    def hasTouchedLeftGoalpost(self, x, y, radius):
        xCond = x - radius <= self.depth
        yCond = y - radius <= self.startY or y + radius >= self.finalY
        return xCond and yCond