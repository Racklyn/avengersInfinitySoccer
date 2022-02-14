import pygame, consts

def drawMenuControlHint(screen, text):
    font = pygame.font.SysFont("Arial", 16, True, False)
    hint = font.render(text, True, consts.BLACK)
    text_rect = hint.get_rect(center=(consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT - 20))
    screen.blit(hint, text_rect)