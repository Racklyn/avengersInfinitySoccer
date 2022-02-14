import pygame, sys, consts
from classes.Player import Player
from classes.Ball import Ball
from classes.Goalposts import Goalposts
import utils

pygame.init()
clock = pygame.time.Clock()

mainFont = pygame.font.SysFont(None, 30, True, False)
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("Avengers Infinity Soccer")


# Creating objects - Initial values
p1 = Player(consts.SCREEN_WIDTH/2 + 200, consts.SCREEN_HEIGHT/2 + 1, 40, 10, consts.RED, 10)
p2 = Player(consts.SCREEN_WIDTH/2 - 200, consts.SCREEN_HEIGHT/2 + 1, 40, 10, consts.BLUE, 10)
goalposts = Goalposts(screen)
ball = Ball(consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2, 20, consts.WHITE, 0.08, goalposts)

gameSettings = {
    'isGamePaused': False,
    'hasGameFinished': False,
    'menuPausedOption': 0
}

timer = 0
counter = 0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                if gameSettings['hasGameFinished']:
                    gameSettings['hasGameFinished'] = False
                elif not gameSettings['isGamePaused']:
                    gameSettings['isGamePaused'] = True

                


            if gameSettings['isGamePaused']:

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    gameSettings['menuPausedOption'] =  0 if gameSettings['menuPausedOption'] == 1 else 1
                if event.key == pygame.K_RETURN:
                    if gameSettings['menuPausedOption'] == 0:
                        gameSettings['isGamePaused'] = False
                    elif gameSettings['menuPausedOption'] == 1:
                        gameSettings = {
                            'isGamePaused': False,
                            'hasGameFinished': True,
                            'menuPausedOption': 0
                        }
                        



    if gameSettings['hasGameFinished']:
        
        utils.endGameWindow(p1, p2, screen)
        timer = 0
        counter = 0

        p1.score = 0
        p2.score = 0
        utils.setToInitialState(p1, p2, ball)


    elif gameSettings['isGamePaused']:
        utils.drawGamePausedMenu(screen, gameSettings['menuPausedOption'], pygame.event.get())
    else:
        p1.events(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
        p2.events(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        

        # Game logic -------------------
        ball.update()
        p1.handleTouchOtherPlayer(p2)
        p2.handleTouchOtherPlayer(p1)

        utils.handleBothSidesBallTouch(p1, ball, goalposts)
        utils.handleBothSidesBallTouch(p2, ball, goalposts)

        # Goal verification ---------
        if ball.hasTouchedLeftGoal():
            utils.goal(1, p1, p2, screen)
            utils.setToInitialState(p1, p2, ball)
            
        if ball.hasTouchedRightGoal():
            utils.goal(2, p1, p2, screen)
            utils.setToInitialState(p1, p2, ball)

        ball.resetIsTouching()

        timer, counter = utils.updateGameTimer(timer, counter)
        if timer > 4:
            gameSettings['hasGameFinished'] = True


        # Visuals ----------------------
        screen.fill(consts.BG_COLOR)
        pygame.draw.line(screen, consts.WHITE, (consts.SCREEN_WIDTH/2, 0), (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT), 6)
        
        goalposts.drawGoalposts()
        ball.draw(screen)
        p1.draw(screen)
        p2.draw(screen)

        
        utils.drawTopMenu(screen, p1, p2, timer, mainFont)

        pygame.display.flip()

    clock.tick(consts.FPS)