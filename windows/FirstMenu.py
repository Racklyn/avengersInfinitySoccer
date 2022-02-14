import pygame, sys, consts


class FirstMenu():
    def __init__(self, screen, mainFont):
        self.screen = screen
        self.mainFont = mainFont

    def open(self, currentWindowID, windowsID):
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    currentWindowID = windowsID['GAME_WINDOW']



        self.screen.fill(consts.BLUE)
        msg = self.mainFont.render("MENU: Pressione SPACE para começar um novo jogo", True, consts.WHITE)
        text_rect = msg.get_rect(center=(consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2))
        self.screen.blit(msg, text_rect)


        return currentWindowID