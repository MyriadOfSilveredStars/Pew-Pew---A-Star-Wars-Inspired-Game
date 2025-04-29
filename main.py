#This is the third iteration of Pew Pew
#My Star Wars themed space battle game
#Utilising the pygame library to create the game environment and functions
#aided by by new knowledge from my Year 1 Programming module at UEA

print("Suy'cuyi yaim!")

#importing all the good shit
import pygame
pygame.init()
import sys

from ships import *
from environment import *
from players import *

from assetfiles import *
from buttonassets import *

from chooseship import shipmenu


def beginGame(): #begin here
    pygame.display.set_caption("Pew Pew")

    titleScreen() #these bring up the static backgrounds
    pygame.display.update()

    while True:
        #okay, just this once I will comment this
        for event in pygame.event.get():
            closeGame(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN and playbutton.isHovered() == True:
                #for selecting the play button
                shipmenu()

        #checking if the button has been hovered over
        playbutton.checkForHover()
        SCREEN.blit(playbutton.getImage(), (400, 600))
        pygame.display.update()

beginGame()



