import pygame, consts, charactersInfo, os


cardImages = {}
for c in charactersInfo.info:
    image = pygame.image.load(os.path.join(consts.IMAGES_DIR, c['image']))
    image = pygame.transform.scale(image, (consts.CHARS_CARD_WIDTH - 10, consts.CHARS_CARD_WIDTH -10))
    cardImages[c['id']] = image


def drawMenuControlHint(screen, text):
    font = pygame.font.SysFont("Arial", 16, True, False)
    hint = font.render(text, True, consts.BLACK)
    text_rect = hint.get_rect(center=(consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT - 20))
    screen.blit(hint, text_rect)


def drawCharacterCard(container, xCenter, yCenter, characterIdx, isSelected):
    card = pygame.Surface((consts.CHARS_CARD_WIDTH, consts.CHARS_CARD_HEIGHT))
    
    if isSelected:
        border = pygame.Rect(
                xCenter - consts.CHARS_CARD_WIDTH/2 - 3,
                yCenter - consts.CHARS_CARD_HEIGHT/2 - 3,
                consts.CHARS_CARD_WIDTH + 6,
                consts.CHARS_CARD_HEIGHT + 6)
        pygame.draw.rect(container, consts.WHITE, border)
    else: 
        card.set_alpha(200)


    card.fill(charactersInfo.info[characterIdx]['color'])

    image_rect = cardImages[characterIdx].get_rect(center=(card.get_width()/2, yCenter))
    card.blit(cardImages[characterIdx], image_rect)


    font = pygame.font.SysFont('Arial', 14, True, False)
    btn_text = font.render(charactersInfo.info[characterIdx]['name'], True, 
                        consts.WHITE if isSelected else consts.LIGHT_GRAY)
    text_rect = btn_text.get_rect(center=(xCenter, card.get_height() + 30))
    container.blit(btn_text, text_rect)

    card_rect = card.get_rect(center=(xCenter, yCenter))
    container.blit(card, card_rect)


def drawCharactersCardContainer(screen, charactersList, option):

    space_between = 25
    nChars = len(charactersList)
    cardsContainer = pygame.Surface((nChars * (consts.CHARS_CARD_WIDTH + space_between) - space_between + 6, consts.CHARS_CARD_HEIGHT + 40 + 6))
    cardsContainer.fill(consts.FIRST_MENU_BG)

    xOffSet = consts.CHARS_CARD_WIDTH/2 + 3
    for idx,c in enumerate(charactersList):
        drawCharacterCard(cardsContainer, xOffSet, cardsContainer.get_height()/2 - 20, c['id'], option==idx)
        xOffSet += consts.CHARS_CARD_WIDTH + space_between

    cardsContainer_rect = cardsContainer.get_rect(center=(consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2))
    screen.blit(cardsContainer, cardsContainer_rect)