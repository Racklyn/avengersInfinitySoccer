import pygame, sys, consts, drawingUtils


class FirstMenu():
    def __init__(self, screen):
        self.screen = screen
        self.option = 0

    def open(self, currentWindowID, windowsID):
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    if self.option == 0:
                        currentWindowID = windowsID['SELECT_P1_MENU']
                    elif self.option == 1:
                        currentWindowID = windowsID['CONTROLS_MENU']
                    elif self.option == 3:
                        currentWindowID = windowsID['ABOUT_MENU']

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.option >= 3: self.option = 0
                    else: self.option +=1
                
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.option <= 0: self.option = 3
                    else: self.option -=1



        # Visuals -----------------
        self.screen.fill(consts.FIRST_MENU_BG)


        font = pygame.font.SysFont('Arial', 40, True, True)
        title = font.render("AVENGERS INFINITY SOCCER", True, consts.WHITE)
        text_rect = title.get_rect(center=(consts.SCREEN_WIDTH/2, 50))
        self.screen.blit(title, text_rect)

        self.drawButton(self.screen, consts.SCREEN_WIDTH/2, 200, "Novo jogo", self.option==0)
        self.drawButton(self.screen, consts.SCREEN_WIDTH/2, 300, "Controles", self.option==1)
        self.drawButton(self.screen, consts.SCREEN_WIDTH/2, 400, "Configurações *", self.option==2)
        self.drawButton(self.screen, consts.SCREEN_WIDTH/2, 500, "Créditos", self.option==3)

        drawingUtils.drawMenuControlHint(self.screen,
            "ENTER - selecionar   ↑ - subir   ↓ - descer"
        )


        return currentWindowID


    
    def drawButton(self, screen, xCenter, yCenter, text, isSelected):

        buttonBox = pygame.Surface((200, 80))
        if not isSelected: buttonBox.set_alpha(200)
        buttonBox.fill(consts.LIGHT_GRAY)

        font = pygame.font.SysFont(None, 30, True, False)
        btn_text = font.render(text, False, consts.HIGHLIGHT if isSelected else consts.GRAY)
        text_rect = btn_text.get_rect(center=(buttonBox.get_width()/2, buttonBox.get_height()/2))
        buttonBox.blit(btn_text, text_rect)

        buttonBox_rect = buttonBox.get_rect(center=(xCenter, yCenter))
        screen.blit(buttonBox, buttonBox_rect)