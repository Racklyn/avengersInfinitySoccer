import consts, utils, pygame, sys, charactersInfo, os
from classes.Ball import Ball
from classes.Goalposts import Goalposts
from classes.Player import Player

class GameWindow():
    def __init__(self, screen, mainFont):
        self.screen = screen
        self.mainFont = mainFont
        self.isStarting = True

        # Creating objects - Initial values
        self.p1 = Player(consts.SCREEN_WIDTH/2 + 200, consts.SCREEN_HEIGHT/2 + 1,
                         40, 10, consts.BLACK, 10)
        self.p2 = Player(consts.SCREEN_WIDTH/2 - 200, consts.SCREEN_HEIGHT/2 + 1,
                         40, 10, consts.WHITE, 10)
        self.goalposts = Goalposts(self.screen)
        self.ball = Ball(consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2, 20, consts.WHITE, 0.08, self.goalposts)
        

        field = pygame.image.load(os.path.join(consts.IMAGES_DIR, 'field01.png')).convert()
        self.field = pygame.transform.scale(field, (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))



        self.gameSettings = {
            'isGamePaused': False,
            'hasGameFinished': False,
            'menuPausedOption': 0
        }

        self.timer = 0
        self.counter = 0
    
    def startGameSettings(self, p1Info, p2Info):
        self.timer = 0 
        self.counter = 0

        self.p1.score = 0
        self.p2.score = 0

        self.p1.color = p1Info['color']
        self.p2.color = p2Info['color']

        self.p1.setAndLoadImage(p1Info['image'])
        self.p2.setAndLoadImage(p2Info['image'])

        utils.setToInitialState(self.p1, self.p2, self.ball)


    def open(self, currentWindowID, windowsID, player1Char, player2Char):

        p1Info = charactersInfo.info[player1Char]
        p2Info = charactersInfo.info[player2Char]

        if self.isStarting:
            self.startGameSettings(p1Info, p2Info)
            self.isStarting = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    if self.gameSettings['hasGameFinished']:
                        currentWindowID = windowsID['FIRST_MENU']
                        self.startGameSettings(p1Info, p2Info)
                        self.isStarting = True

                        self.gameSettings['hasGameFinished'] = False
                    elif not self.gameSettings['isGamePaused']:
                        self.gameSettings['isGamePaused'] = True

                    


                if self.gameSettings['isGamePaused']:

                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.gameSettings['menuPausedOption'] =  0 if self.gameSettings['menuPausedOption'] == 1 else 1
                    if event.key == pygame.K_RETURN:
                        if self.gameSettings['menuPausedOption'] == 0:
                            self.gameSettings['isGamePaused'] = False
                        elif self.gameSettings['menuPausedOption'] == 1:
                            self.gameSettings = {
                                'isGamePaused': False,
                                'hasGameFinished': True,
                                'menuPausedOption': 0
                            }
                            



        if self.gameSettings['hasGameFinished']:
            
            self.endGameWindow(self.screen)
            


        elif self.gameSettings['isGamePaused']:
            self.drawGamePausedMenu(self.screen, self.gameSettings['menuPausedOption'])
        else:
            self.p1.events(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
            self.p2.events(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
            

            # Game logic -------------------
            self.ball.update()
            self.p1.handleTouchOtherPlayer(self.p2)
            self.p2.handleTouchOtherPlayer(self.p1)

            utils.handleBothSidesBallTouch(self.p1, self.ball, self.goalposts)
            utils.handleBothSidesBallTouch(self.p2, self.ball, self.goalposts)

            # Goal verification ---------
            if self.ball.hasTouchedLeftGoal():
                utils.goal(1, self.p1, self.p2, self.screen)
                utils.setToInitialState(self.p1, self.p2, self.ball)
                
            if self.ball.hasTouchedRightGoal():
                utils.goal(2, self.p1, self.p2, self.screen)
                utils.setToInitialState(self.p1, self.p2, self.ball)

            self.ball.resetIsTouching()

            self.timer, self.counter = utils.updateGameTimer(self.timer, self.counter)
            if self.timer >= 90:
                self.gameSettings['hasGameFinished'] = True



            # Visuals ----------------------
                # Field image:
            #self.screen.fill(consts.BG_COLOR)
            self.screen.blit(self.field, (0,0))
            pygame.draw.line(self.screen, consts.WHITE, (consts.SCREEN_WIDTH/2, 0), (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT), 6)
            
            self.goalposts.drawGoalposts()
            self.ball.draw(self.screen)
            self.p1.draw(self.screen)
            self.p2.draw(self.screen)

            
            self.drawTopMenu(self.screen, p1Info, p2Info)

            
        return  currentWindowID

    



    def drawTopMenu(self, screen, p1Info, p2Info):
        pygame.draw.rect(screen, consts.WHITE, 
            (0, 0, consts.SCREEN_WIDTH, consts.TOP_MENU_HEIGHT))

        p2ScoreText = self.mainFont.render("%s: %d"%(p2Info['name'], self.p2.score), False, self.p2.color)
        p2Score_rect = p2ScoreText.get_rect(center=(consts.SCREEN_WIDTH/4, consts.TOP_MENU_HEIGHT/2))

        p1coreScore = self.mainFont.render("%s: %d"%(p1Info['name'], self.p1.score), False, self.p1.color)
        p1Score_rect = p1coreScore.get_rect(center=(3*consts.SCREEN_WIDTH/4,  consts.TOP_MENU_HEIGHT/2))

        timerText = self.mainFont.render("%d:00 min."%self.timer, False, consts.GRAY)
        timer_rect = timerText.get_rect(center=(consts.SCREEN_WIDTH/2,  consts.TOP_MENU_HEIGHT/2))

        screen.blit(p2ScoreText, p2Score_rect)
        screen.blit(p1coreScore, p1Score_rect)
        screen.blit(timerText, timer_rect)


    
    def drawGamePausedMenu(self, screen, option):

        pausedBox = pygame.Surface((int(consts.SCREEN_WIDTH/4), int(consts.SCREEN_HEIGHT/4)))
        pausedBox.set_alpha(230)
        pausedBox.fill(consts.WHITE)

        font = pygame.font.SysFont(None, 30, True, False)
        title = font.render("Jogo pausado!", False, consts.GRAY)
        text_rect = title.get_rect(center=(pausedBox.get_width()/2, pausedBox.get_height()/2 - 30))
        pausedBox.blit(title, text_rect)

        font2 = pygame.font.SysFont(None, 20, True, False)
        op1 = font2.render("Retomar", False, consts.RED if option==0 else consts.GRAY)
        text_rect = op1.get_rect(center=(pausedBox.get_width()/2, pausedBox.get_height()/2 + 20))
        pausedBox.blit(op1, text_rect)

        op2 = font2.render("Sair da partida", False, consts.RED if option==1 else consts.GRAY)
        text_rect = op2.get_rect(center=(pausedBox.get_width()/2, pausedBox.get_height()/2 + 50))
        pausedBox.blit(op2, text_rect)

        pausedBox_rect = pausedBox.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(pausedBox, pausedBox_rect)

        pygame.display.flip()


        

    def endGameWindow(self, screen):

        endGameBox = pygame.Surface((int(consts.SCREEN_WIDTH/3), int(consts.SCREEN_HEIGHT/3)))
        endGameBox.fill(consts.BLACK)

        font = pygame.font.SysFont(None, 40, True, False)
        title = font.render("FIM DE JOGO !", False, consts.WHITE)
        text_rect = title.get_rect(center=(endGameBox.get_width()/2, endGameBox.get_height()/2 - 20))
        endGameBox.blit(title, text_rect)

        scoresText = font.render("%d x %d"%(self.p2.score, self.p1.score), False, consts.WHITE)
        text_rect = scoresText.get_rect(center=(endGameBox.get_width()/2, endGameBox.get_height()/2 + 20))
        endGameBox.blit(scoresText, text_rect)

        font2 = pygame.font.SysFont('Arial', 14, False, False)
        msg = font2.render("Pressione SPACE / ESC para voltar ao menu", True, consts.LIGHT_GRAY)
        text_rect = msg.get_rect(center=(endGameBox.get_width()/2, endGameBox.get_height() - 30))
        endGameBox.blit(msg, text_rect)

        endGameBox_rect = endGameBox.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(endGameBox, endGameBox_rect)

        pygame.display.flip()