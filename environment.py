#methods for the static backgrounds throughout the game
import pygame
pygame.init()
import sys

from assetfiles import *

def closeGame(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def titleScreen():
    SCREEN.blit(hyperspacezoom, (0, 0))
    SCREEN.blit(maintitle, (WIDTH//2 - 375, HEIGHT//2 - 100))

def menuScreen():
    pass

def chooseShipScreen():
    SCREEN.fill(BLACK)
    SCREEN.blit(fighttitle, (230, 50))
    SCREEN.blit(HEADING_FONT.render("Player 1", 1, YELLOW), (50, 160))
    SCREEN.blit(HEADING_FONT.render("Player 2", 1, YELLOW), (760, 160))

def gameScreen():
    SCREEN.blit(menu_tatooine, (0,0))
    pygame.draw.rect(SCREEN, BLACK, INFOBASE)
    pygame.draw.rect(SCREEN, WHITE, BORDER)