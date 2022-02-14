import pygame, consts, math

def handleBothSidesBallTouch(player, ball, goalposts):

    if goalposts.hasTouchedLeftGoalpost(ball.x, ball.y, ball.radius):
        ball.isTouching['left'] = True
    if goalposts.hasTouchedRightGoalpost(ball.x, ball.y, ball.radius):
        ball.isTouching['right'] = True

    # verificar se Player tocou na bola:
    minDist = ball.radius + player.radius
    dist = math.hypot(ball.x - player.x, ball.y - player.y)
    if dist==0: dist=1

    if dist <= minDist: # Jogador está tocando na bola

        if (player.x < ball.x and player.y == ball.y):
            ball.isTouching['left'] = True
        if (player.x > ball.x and player.y == ball.y):
            ball.isTouching['right'] = True

        if player.y < ball.y and player.x == ball.x:
            ball.isTouching['bottom'] = True
        if player.y > ball.y and player.x == ball.x:
            ball.isTouching['top'] = True

        #print(ball.isTouching)

        if (ball.isTouching["left"] and ball.isTouching["right"]):
            
            if (player.x > ball.x):
                player.x = ball.x + ball.radius + player.radius
            else:
                player.x = ball.x - ball.radius - player.radius
            
        
        if (ball.isTouching["top"] and ball.isTouching["bottom"]):
            if (player.y > ball.y):
                player.y = ball.y + ball.radius + player.radius
            else:
                player.y = ball.y - ball.radius - player.radius

        ball.isBlocked = (ball.isTouching["left"] and ball.isTouching["right"]) or (ball.isTouching["top"] and ball.isTouching["bottom"])
    


        ball.handlePlayerTouch(player, minDist, dist)

    else:
        ball.isBlocked = False


def goal(goalP, p1, p2, screen):
    
    if goalP==1:
        goalPlayer=p1
    else:
        goalPlayer=p2

    goalPlayer.score += 1

    # Draw goal window
    goalBox = pygame.Surface((int(consts.SCREEN_WIDTH/2), int(consts.SCREEN_HEIGHT/2)))
    goalBox.set_alpha(230)
    goalBox.fill(consts.BLACK)
    
    # pygame.draw.rect(screen, consts.WHITE, 
    #     (100, 100, consts.SCREEN_WIDTH - 200, consts.TOP_MENU_HEIGHT - 200))

    font = pygame.font.SysFont(None, 40, True, False)
    msg = font.render("GOALLLLLL !", False, goalPlayer.color)
    text_rect = msg.get_rect(center=(goalBox.get_width()/2, goalBox.get_height()/2 - 20))
    goalBox.blit(msg, text_rect)

    font = pygame.font.SysFont(None, 40, True, False)
    scoresText = font.render("%d x %d"%(p2.score, p1.score), False, consts.WHITE)
    text_rect = scoresText.get_rect(center=(goalBox.get_width()/2, goalBox.get_height()/2 + 20))
    goalBox.blit(scoresText, text_rect)

    goalBox_rect = goalBox.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(goalBox, goalBox_rect)

    pygame.display.flip()

    pygame.time.delay(2000)




def setToInitialState(p1, p2, ball):
    p1.setToInitialPosition()
    p2.setToInitialPosition()
    ball.setToInitialPosition()



def drawTopMenu(screen, p1, p2, timer, font):
    pygame.draw.rect(screen, consts.WHITE, 
        (0, 0, consts.SCREEN_WIDTH, consts.TOP_MENU_HEIGHT))

    p1ScoreText = font.render("P1: %d"%p1.score, False, p1.color)
    p1Score_rect = p1ScoreText.get_rect(center=(80, consts.TOP_MENU_HEIGHT/2))

    p2coreScore = font.render("P2: %d"%p2.score, False, p2.color)
    p2Score_rect = p2coreScore.get_rect(center=(consts.SCREEN_WIDTH - 80,  consts.TOP_MENU_HEIGHT/2))

    timerText = font.render("%d:00 min."%timer, False, consts.GRAY)
    timer_rect = timerText.get_rect(center=(consts.SCREEN_WIDTH/2,  consts.TOP_MENU_HEIGHT/2))

    screen.blit(p1ScoreText, p1Score_rect)
    screen.blit(p2coreScore, p2Score_rect)
    screen.blit(timerText, timer_rect)


def drawGamePausedMenu(screen, option, events):

    pausedBox = pygame.Surface((int(consts.SCREEN_WIDTH/4), int(consts.SCREEN_HEIGHT/4)))
    pausedBox.set_alpha(230)
    pausedBox.fill(consts.WHITE)

    font = pygame.font.SysFont(None, 30, True, False)
    title = font.render("Jogo pausado!", False, consts.GRAY)
    text_rect = title.get_rect(center=(pausedBox.get_width()/2, pausedBox.get_height()/2 - 30))
    pausedBox.blit(title, text_rect)

    font = pygame.font.SysFont(None, 20, True, False)
    op1 = font.render("Retomar", False, consts.RED if option==0 else consts.GRAY)
    text_rect = op1.get_rect(center=(pausedBox.get_width()/2, pausedBox.get_height()/2 + 20))
    pausedBox.blit(op1, text_rect)

    font = pygame.font.SysFont(None, 20, True, False)
    op2 = font.render("Sair da partida", False, consts.RED if option==1 else consts.GRAY)
    text_rect = op2.get_rect(center=(pausedBox.get_width()/2, pausedBox.get_height()/2 + 50))
    pausedBox.blit(op2, text_rect)

    pausedBox_rect = pausedBox.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(pausedBox, pausedBox_rect)

    pygame.display.flip()


    

def endGameWindow(p1, p2, screen):

    endGameBox = pygame.Surface((int(consts.SCREEN_WIDTH/3), int(consts.SCREEN_HEIGHT/3)))
    endGameBox.fill(consts.BLACK)

    font = pygame.font.SysFont(None, 40, True, False)
    title = font.render("FIM DE JOGO !", False, consts.WHITE)
    text_rect = title.get_rect(center=(endGameBox.get_width()/2, endGameBox.get_height()/2 - 20))
    endGameBox.blit(title, text_rect)

    scoresText = font.render("%d x %d"%(p2.score, p1.score), False, consts.WHITE)
    text_rect = scoresText.get_rect(center=(endGameBox.get_width()/2, endGameBox.get_height()/2 + 20))
    endGameBox.blit(scoresText, text_rect)

    font2 = pygame.font.SysFont('Arial', 14, False, False)
    msg = font2.render("- Pressione SPACE para começar um novo jogo -", True, consts.LIGHT_GRAY)
    text_rect = msg.get_rect(center=(endGameBox.get_width()/2, endGameBox.get_height() - 30))
    endGameBox.blit(msg, text_rect)

    endGameBox_rect = endGameBox.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(endGameBox, endGameBox_rect)

    pygame.display.flip()




def updateGameTimer(timer, counter):
    if counter >= consts.FPS:
        timer += 1
        counter = 0
    else:
        counter += 1
    
    return timer, counter