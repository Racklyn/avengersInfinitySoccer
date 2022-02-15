import pygame, sys, consts
import drawingUtils


class ControlsMenu():
    def __init__(self, screen, mainFont):
        self.screen = screen
        self.mainFont = mainFont
        self.font1 = pygame.font.SysFont('Arial', 18, True, False)

    def open(self, currentWindowID, windowsID):
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                currentWindowID = windowsID['FIRST_MENU']
                    




        # Visuals -----------------
        self.screen.fill(consts.FIRST_MENU_BG)



        font = pygame.font.SysFont(None, 40, True, True)
        title = font.render("CONTROLES", True, consts.WHITE)
        text_rect = title.get_rect(center=(consts.SCREEN_WIDTH/2, 50))
        self.screen.blit(title, text_rect)


        texts = [
            "Controles Player 1",
            "SETAS: ← → ↑ ↓",
            "Controles Player 2",
            "TECLAS: A, W, S e D",
            "Outros",
            "Pausar o jogo: SPACE/ESC"
        ]

        offSet = -80
        for i, t in enumerate(texts):
            font = self.font1
            color = consts.BLACK
            incOffSet = 60
            if i%2==0:
                font = self.mainFont
                color = consts.WHITE
                incOffSet = 40
            
            text = font.render(t, True, color)
            text_rect = text.get_rect(center=(consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2 + offSet))
            self.screen.blit(text, text_rect)
            offSet += incOffSet


        

        drawingUtils.drawMenuControlHint(self.screen,
            "Pressione qualquer TECLA para voltar"
        )



        return currentWindowID


    