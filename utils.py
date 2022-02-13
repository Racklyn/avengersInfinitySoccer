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

    screen.blit(goalBox, (int(consts.SCREEN_WIDTH/4),int(consts.SCREEN_HEIGHT/4)))

    pygame.display.flip()

    pygame.time.delay(2000)




def setToInitialState(p1, p2, ball):
    p1.setToInitialPosition()
    p2.setToInitialPosition()
    ball.setToInitialPosition()



def drawTopMenu(screen, p1, p2, font):
    pygame.draw.rect(screen, consts.WHITE, 
        (0, 0, consts.SCREEN_WIDTH, consts.TOP_MENU_HEIGHT))

    p1ScoreText = font.render("P1: %d"%p1.score, False, p1.color)
    p2coreScore = font.render("P2: %d"%p2.score, False, p2.color)
    screen.blit(p1ScoreText, (consts.SCREEN_WIDTH-100, 10))
    screen.blit(p2coreScore, (30, 10))

