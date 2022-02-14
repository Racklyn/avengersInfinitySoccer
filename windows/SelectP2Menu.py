import pygame, sys, consts
import drawingUtils


class SelectP2Menu():
    def __init__(self, screen, mainFont):
        self.screen = screen
        self.mainFont = mainFont
        self.option = 0

    def open(self, currentWindowID, windowsID):
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




        # Visuals -----------------
        self.screen.fill(consts.FIRST_MENU_BG)



        font = pygame.font.SysFont(None, 40, True, True)
        title = font.render("Selecione o PLAYER 2", True, consts.WHITE)
        text_rect = title.get_rect(center=(consts.SCREEN_WIDTH/2, 50))
        self.screen.blit(title, text_rect)



        drawingUtils.drawMenuControlHint(self.screen,
            "ENTER - confirmar   ESC/B - voltar   ↑ - subir   ↓ - descer"
        )



        return currentWindowID


    