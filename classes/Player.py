import pygame, consts, os, math

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
        self.directions = {
            'up': False,
            'down': True,
            'left': False,
            'right': False
        }

        image = pygame.image.load(os.path.join(consts.IMAGES_DIR, 'ironMan.png'))
        self.image = pygame.transform.scale(image, (self.radius*2, self.radius*2))

        self.isMoving = False
        
    def setToInitialPosition(self):
        self.x = self.xInitial
        self.y = self.yInitial

    def setAndLoadImage(self, imageName):
        try:
            image = pygame.image.load(os.path.join(consts.IMAGES_DIR, imageName))
        except:
            print("ERRO AO INICIAR IMAGEM DO PERSONAGEM ESCOLHIDO! Iniciando como IronMan.png")
            image = pygame.image.load(os.path.join(consts.IMAGES_DIR, 'ironMan.png'))

        self.image = pygame.transform.scale(image, (self.radius*2, self.radius*2))



    def draw (self, screen):
        
        angle = 0

        dir = list(filter(lambda d: self.directions[d], self.directions.keys()))
        moreOneDir = False
        if len(dir) > 1:
            moreOneDir = True
            if self.directions['right'] and self.directions['up']:
                angle=45
            elif self.directions['left'] and self.directions['up']:
                angle=135
            elif self.directions['left'] and self.directions['down']:
                angle=225
            if self.directions['right'] and self.directions['down']:
                angle=315
        elif len(dir) == 1:
            angle = {'right': 0, 'up': 90, 'left': 180, 'down': 270}[dir[0]]

        
        f = math.sqrt(2) if moreOneDir else 1

        rotatedImage = pygame.transform.rotate(self.image, angle)
        
        #pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        screen.blit(rotatedImage, (self.x - f*self.radius, self.y - f*self.radius))


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

        newDirections = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }


        if pygame.key.get_pressed()[up]:
            yInc -= self.speed
            newDirections['up'] = True
        if pygame.key.get_pressed()[down]:
            yInc += self.speed
            newDirections['down'] = True
        if pygame.key.get_pressed()[left]:
            xInc -= self.speed
            newDirections['left'] = True
        if pygame.key.get_pressed()[right]:
            xInc += self.speed
            newDirections['right'] = True

        if not (xInc==yInc==0):
            self.isMoving = True
            self.directions = newDirections

        if not (xInc==0 or yInc==0):
            xInc /= math.sqrt(2)
            yInc /= math.sqrt(2)
        


        self.updatePosition(self.x + xInc, self.y + yInc)
