import pygame, sys, consts
import drawingUtils


class AboutMenu():
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
                currentWindowID = windowsID['FIRST_MENU']
                    




        # Visuals -----------------
        self.screen.fill(consts.FIRST_MENU_BG)



        font = pygame.font.SysFont(None, 40, True, True)
        title = font.render("CRÉDITOS", True, consts.WHITE)
        text_rect = title.get_rect(center=(consts.SCREEN_WIDTH/2, 50))
        self.screen.blit(title, text_rect)


        texts = [
            "Desenvolvido por: Francisco Racklyn Sotero dos Santos",
            "Aluno do 1° período em Ciência da Computação - UFAL Arapiraca",
            "14 de fevereiro de 2022",
        ]

        offSet = -30
        for t in texts:
            title = self.mainFont.render(t, True, consts.BLACK)
            text_rect = title.get_rect(center=(consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2 + offSet))
            self.screen.blit(title, text_rect)
            offSet += 40

        drawingUtils.drawMenuControlHint(self.screen,
            "Pressione qualquer TECLA para voltar"
        )



        return currentWindowID


    