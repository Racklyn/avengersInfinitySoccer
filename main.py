import pygame, consts
from windows.FirstMenu import FirstMenu
from windows.GameWindow import GameWindow


pygame.init()
clock = pygame.time.Clock()

mainFont = pygame.font.SysFont(None, 30, True, False)
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("Avengers Infinity Soccer")

windowsID = {
    'FIRST_MENU': 0,
    'GAME_WINDOW': 1
}
currentWindowID = 0



firstMenu = FirstMenu(screen, mainFont)
gameWindow = GameWindow(screen, mainFont)

while True:

    if currentWindowID == windowsID['FIRST_MENU']: 
        currentWindowID = firstMenu.open(currentWindowID, windowsID)
    elif currentWindowID == windowsID['GAME_WINDOW']:
        currentWindowID = gameWindow.open(currentWindowID, windowsID)
    
    print(currentWindowID)


    pygame.display.flip()
    clock.tick(consts.FPS)