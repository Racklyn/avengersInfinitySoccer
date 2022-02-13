import math

def handleBothSidesBallTouch(player, ball, goalposts):

    # if goalposts.hasTouchedLeftGoalpost(ball.x, ball.y, ball.radius):
    #     ball.isTouching['left'] = True
    # if goalposts.hasTouchedRightGoalpost(ball.x, ball.y, ball.radius):
    #     ball.isTouching['right'] = True

    # verificar se Player tocou na bola:
    minDist = ball.radius + player.radius
    dist = math.hypot(ball.x - player.x, ball.y - player.y)
    if dist <= minDist: # Jogador está tocando na bola
        #player.isTouchingBall = True

        if (player.x < ball.x and player.y == ball.y):# or goalposts.hasTouchedLeftGoalpost(ball.x, ball.y, ball.radius):
            ball.isTouching['left'] = True
        if (player.x > ball.x and player.y == ball.y):# or goalposts.hasTouchedRightGoalpost(ball.x, ball.y, ball.radius):
            ball.isTouching['right'] = True

        if player.y < ball.y and player.x == ball.x:
            ball.isTouching['bottom'] = True
        if player.y > ball.y and player.x == ball.x:
            ball.isTouching['top'] = True

        print(ball.isTouching)
    #if player.isTouchingBall:
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
    


        ball.handlePlayerTouch(player)

    else:
        ball.isBlocked = False


