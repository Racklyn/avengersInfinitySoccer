import pygame, consts

class Goalposts:
    def __init__(self, screen, size = consts.GOALPOSTS_SIZE, depth = consts.GOALPOSTS_DEPTH):
        self.screen = screen
        self.size = size
        self.depth = depth

        self.startY = consts.SCREEN_HEIGHT/2 - self.size/2
        self.finalY = consts.SCREEN_HEIGHT/2 + self.size/2
        

    
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

    def hasTouchedLeftGoalpost(self, x, y, radius):
        xCond = x - radius <= self.depth
        yCond = y - radius <= self.startY or y + radius >= self.finalY
        return xCond and yCond

    def hasTouchedRightGoalpost(self, x, y, radius):
        xCond = x + radius >= consts.SCREEN_WIDTH - self.depth
        yCond = y - radius <= self.startY or y + radius >= self.finalY
        return xCond and yCond