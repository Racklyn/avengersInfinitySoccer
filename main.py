import pygame, sys, consts
from classes.Player import Player
from classes.Ball import Ball
from classes.Goalposts import Goalposts
import utils

pygame.init()
clock = pygame.time.Clock()

sysFonte = pygame.font.SysFont("Arial", 20, True, False)
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("Avengers Infinity Soccer")


# Creating objects
p1 = Player(700,40, 40, 10, consts.RED, 10)
p2 = Player(100,consts.SCREEN_HEIGHT/2, 40, 10, consts.BLUE, 10)
goalposts = Goalposts(screen)
ball = Ball(consts.SCREEN_WIDTH/2, 40, 20, consts.WHITE, 0.08, goalposts)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    p1.events(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    p2.events(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    
    p1.handleTouchOtherPlayer(p2)
    p2.handleTouchOtherPlayer(p1)

    utils.handleBothSidesBallTouch(p1, ball, goalposts)
    utils.handleBothSidesBallTouch(p2, ball, goalposts)

    
    #ball.handlePlayerTouch(p2)

    # p1.handleBothSidesBallTouch(ball, goalposts)
    # p2.handleBothSidesBallTouch(ball, goalposts)

    ball.resetIsTouching()
    

    #Visuals
    screen.fill(consts.BG_COLOR) # preenche toda a tela com a cor, "limpa"
    pygame.draw.line(screen, consts.WHITE, (consts.SCREEN_WIDTH/2, 0), (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT), 6)

    
    goalposts.drawGoalposts()
    ball.updateAndDraw(screen)
    p1.draw(screen)
    p2.draw(screen)
    

    # screen.blit(oScore, (30, 10))
    # screen.blit(pScore, (screen_width-100, 10))
    

    pygame.display.flip()
    clock.tick(60)