import pygame, sys, consts, charactersInfo
import drawingUtils


class SelectP2Menu():
    def __init__(self, screen, mainFont):
        self.screen = screen
        self.mainFont = mainFont
        self.option = 0

    def open(self, currentWindowID, windowsID, player1Char, player2Char):

        charsList = list(filter(lambda c: not c['id'] == player1Char, charactersInfo.info))


        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_b or event.key == pygame.K_BACKSPACE:
                    currentWindowID = windowsID['SELECT_P1_MENU']

                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE: 
                    currentWindowID = windowsID['GAME_WINDOW']

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if self.option <= 0:
                        self.option = len(charsList) - 1
                    else:
                        self.option -= 1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.option >= len(charsList) - 1:
                        self.option = 0
                    else:
                        self.option += 1



        # Visuals -----------------
        self.screen.fill(consts.FIRST_MENU_BG)



        font = pygame.font.SysFont(None, 40, True, True)
        title = font.render("Selecione o PLAYER 2", True, consts.WHITE)
        text_rect = title.get_rect(center=(consts.SCREEN_WIDTH/2, 50))
        self.screen.blit(title, text_rect)


        # Characters card container ------

        drawingUtils.drawCharactersCardContainer(self.screen, charsList, self.option)


        drawingUtils.drawMenuControlHint(self.screen,
            "ENTER - Iniciar jogo   ESC/B - voltar   ← esquerda   → direita"
        )



        return currentWindowID, charsList[self.option]['id']


    