import pygame, consts
from windows.SelectP1Menu import SelectP1Menu
from windows.SelectP2Menu import SelectP2Menu
from windows.FirstMenu import FirstMenu
from windows.GameWindow import GameWindow
from windows.ControlsMenu import ControlsMenu
from windows.AboutMenu import AboutMenu


pygame.init()
clock = pygame.time.Clock()

mainFont = pygame.font.SysFont(None, 30, True, False)
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("Avengers Infinity Soccer")

windowsID = {
    'FIRST_MENU': 0,
    'GAME_WINDOW': 1,
    'ABOUT_MENU': 2,
    'SELECT_P1_MENU': 3,
    'SELECT_P2_MENU': 4,
    'CONTROLS_MENU': 5
}
currentWindowID = 0


player1Char = 0
player2Char = 1



firstMenu = FirstMenu(screen)
gameWindow = GameWindow(screen, mainFont)
aboutMenu = AboutMenu(screen, mainFont)
selectP1Menu = SelectP1Menu(screen, mainFont)
selectP2Menu = SelectP2Menu(screen, mainFont)
controlsMenu = ControlsMenu(screen, mainFont)

while True:

    if currentWindowID == windowsID['FIRST_MENU']: 
        currentWindowID = firstMenu.open(currentWindowID, windowsID)

    elif currentWindowID == windowsID['SELECT_P1_MENU']:
        currentWindowID, player1Char = selectP1Menu.open(currentWindowID, windowsID, player1Char)

    elif currentWindowID == windowsID['SELECT_P2_MENU']:
        currentWindowID, player2Char = selectP2Menu.open(currentWindowID, windowsID, player1Char, player2Char)

    elif currentWindowID == windowsID['GAME_WINDOW']:
        currentWindowID = gameWindow.open(currentWindowID, windowsID, player1Char, player2Char)

    elif currentWindowID == windowsID['ABOUT_MENU']:
        currentWindowID = aboutMenu.open(currentWindowID, windowsID)

    elif currentWindowID == windowsID['CONTROLS_MENU']:
        currentWindowID = controlsMenu.open(currentWindowID, windowsID)
    


    pygame.display.flip()
    clock.tick(consts.FPS)