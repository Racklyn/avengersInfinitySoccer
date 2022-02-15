import pygame, sys, consts, charactersInfo
import drawingUtils


class SelectP1Menu():
    def __init__(self, screen, mainFont):
        self.screen = screen
        self.mainFont = mainFont
        self.option = 0

    def open(self, currentWindowID, windowsID, player1Char):
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_b or event.key == pygame.K_BACKSPACE:
                    currentWindowID = windowsID['FIRST_MENU']

                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE: 
                    currentWindowID = windowsID['SELECT_P2_MENU']

                if event.key == pygame.K_LEFT:
                    if self.option <= 0:
                        self.option = len(charactersInfo.info) - 1
                    else:
                        self.option -= 1
                if event.key == pygame.K_RIGHT:
                    if self.option >= len(charactersInfo.info) - 1:
                        self.option = 0
                    else:
                        self.option += 1


        # Visuals -----------------
        self.screen.fill(consts.FIRST_MENU_BG)



        font = pygame.font.SysFont(None, 40, True, True)
        title = font.render("Selecione o PLAYER 1", True, consts.WHITE)
        text_rect = title.get_rect(center=(consts.SCREEN_WIDTH/2, 50))
        self.screen.blit(title, text_rect)


        # Characters card container ------
        drawingUtils.drawCharactersCardContainer(self.screen, charactersInfo.info, self.option)


        drawingUtils.drawMenuControlHint(self.screen,
            "ENTER - confirmar   ESC/B - voltar   ← esquerda   → direita"
        )

        return currentWindowID, self.option


    