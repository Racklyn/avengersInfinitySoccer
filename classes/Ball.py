import pygame, consts, os

class Ball:
    def __init__(self, x, y, radius, color, deceleration, goalposts):
        self.x = x
        self.y = y
        self.initialX = x
        self.initialY = y
        self.radius = radius
        self.speed = 0
        self.color = color
        self.deceleration = deceleration
        self.isBlocked = False
        self.goalposts = goalposts

        ballImage = pygame.image.load(os.path.join(consts.IMAGES_DIR, 'ball01.png'))
        self.ballImage = pygame.transform.scale(ballImage, (self.radius*2, self.radius*2))

        self.isTouching = {
            'top': False,
            'right': False,
            'bottom': False,
            'left': False
        }

        self.xSpeed, self.ySpeed = 0, 0
        self.counter = 0

    def setToInitialPosition(self):
        self.x = self.initialX
        self.y = self.initialY
        self.speed = 0


    def draw(self, screen):
        screen.blit(self.ballImage, (self.x - self.radius, self.y - self.radius))
        #pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def update (self):
        
        newSpeed = self.speed - self.deceleration
        if newSpeed > 0:

            self.xSpeed *= (newSpeed/self.speed)
            self.ySpeed *= (newSpeed/self.speed)
            self.speed = newSpeed

            self.updatePosition(self.x + self.xSpeed, self.y + self.ySpeed)
        else:
            self.speed = 0



    def updatePosition(self, newX, newY):

        if self.goalposts.hasTouchedLeftGoalpost(newX, newY, self.radius): #self.isTouching['left']:

            self.x = self.radius + self.goalposts.depth + 1
            #self.x += self.speed
            #self.isTouching['left'] = True
            self.xSpeed = -self.xSpeed
        elif self.goalposts.hasTouchedRightGoalpost(self.x, self.y, self.radius):
            self.x = consts.SCREEN_WIDTH - self.radius - self.goalposts.depth - 1
            #self.x -= self.speed
            #self.isTouching['Right'] = True
            self.xSpeed = -self.xSpeed
        else:
            self.x = newX

        if newY - self.radius <= consts.TOP_MENU_HEIGHT:
            self.y = self.radius + consts.TOP_MENU_HEIGHT
            self.ySpeed = -self.ySpeed
        elif newY + self.radius >= consts.SCREEN_HEIGHT:
            self.y = consts.SCREEN_HEIGHT - self.radius
            self.ySpeed = -self.ySpeed
        else:
            self.y = newY      


    
    def handlePlayerTouch(self, player, minDist, dist):
        if self.isBlocked:
            self.speed = 0
            
        else:
            self.speed = player.kickSpeed
        
            #print(self.speed)
            #print("dist",dist)

            xD = self.x - player.x
            yD = self.y - player.y

            newXD = minDist * xD/dist
            newYD = minDist * yD/dist

            self.xSpeed = self.speed * (self.x - player.x) / dist
            self.ySpeed = self.speed * (self.y - player.y) / dist

            self.updatePosition(player.x + newXD, player.y + newYD)

            
    def resetIsTouching(self, fill = False):
        self.isTouching = {
            'top': fill,
            'right': fill,
            'bottom': fill,
            'left': fill
        }

    def hasTouchedLeftGoal(self):
        return (self.x - self.radius <= 0) and not self.goalposts.hasTouchedLeftGoalpost(self.x, self.y, self.radius)
    
    def hasTouchedRightGoal(self):
        return self.x + self.radius >= consts.SCREEN_WIDTH and not self.goalposts.hasTouchedRightGoalpost(self.x, self.y, self.radius)