import pygame, sys, consts, sprites

pygame.init()
clock = pygame.time.Clock()

sysFonte = pygame.font.SysFont("Arial", 20, True, False)
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("Avengers Infinity Soccer")


p1 = sprites.Player(50,50, 40, 10, consts.RED)
p2 = sprites.Player(100,300, 40, 10, consts.BLUE)
ball = sprites.Ball(consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2, 20, 10, consts.WHITE)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    isP1Moving = p1.events(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    isP2Moving = p2.events(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    
    if isP1Moving: p1.handleTouchOtherPlayer(p2)
    if isP2Moving: p2.handleTouchOtherPlayer(p1)

    ball.hadlePlayerTouch(p1)
    ball.hadlePlayerTouch(p2)
    

    #Visuals
    screen.fill(consts.BG_COLOR) # preenche toda a tela com a cor, "limpa"
    pygame.draw.line(screen, consts.WHITE, (consts.SCREEN_WIDTH/2, 0), (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT), 5)

    ball.draw(screen)
    p1.draw(screen)
    p2.draw(screen)
    

    # screen.blit(oScore, (30, 10))
    # screen.blit(pScore, (screen_width-100, 10))
    

    pygame.display.flip()
    clock.tick(60)