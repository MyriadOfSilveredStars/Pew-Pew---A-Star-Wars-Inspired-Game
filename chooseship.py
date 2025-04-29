import pygame
pygame.init()

from ships import *
from environment import *
from players import *
from gamemode import *

from assetfiles import *
from buttonassets import *   

def drawShips(finalChoice1, finalChoice2):
    chooseShipScreen()
    drawLeftCoordinates = [[80, 220], [190, 220], [0,0], [60, 355], [190, 360], [305, 360], [65, 500], [190, 500], [0,0]]
    drawRightCoordinates = [[0,0], [740, 220], [900, 220], [625, 360], [740, 360], [880, 355], [0,0], [735, 500], [880, 500]]

    for j in range(9):
        if finalChoice1 == -1:
            backingArray1[j].checkForHover()
            SCREEN.blit(backingArray1[j].getImage(), (coordinateArray1[j][0], coordinateArray1[j][1]))
        else:
            SCREEN.blit(backingArray1[finalChoice1].getImage(), (coordinateArray1[finalChoice1][0], coordinateArray1[finalChoice1][1]))

        if finalChoice2 == -1:
            backingArray2[j].checkForHover()
            SCREEN.blit(backingArray2[j].getImage(), (coordinateArray2[j][0], coordinateArray2[j][1]))
        else:
            SCREEN.blit(backingArray2[finalChoice2].getImage(), (coordinateArray2[finalChoice2][0], coordinateArray2[finalChoice2][1]))


    for i in range(len(allLeftShips)):
        if allLeftShips[i] != "null":
            if finalChoice1 == -1:
                SCREEN.blit(allLeftShips[i].getImage(), (drawLeftCoordinates[i][0], drawLeftCoordinates[i][1]))
            else:
                SCREEN.blit(allLeftShips[finalChoice1].getImage(), (drawLeftCoordinates[finalChoice1][0], drawLeftCoordinates[finalChoice1][1]))
        if allRightShips[i] != "null":
            if finalChoice2 == -1: 
                SCREEN.blit(allRightShips[i].getImage(), (drawRightCoordinates[i][0], drawRightCoordinates[i][1]))
            else:    
                SCREEN.blit(allRightShips[finalChoice2].getImage(), (drawRightCoordinates[finalChoice2][0], drawRightCoordinates[finalChoice2][1]))
                

def shipmenu():
    finalChoice1 = -1
    finalChoice2 = -1

    chooseShipScreen()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            closeGame(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backbutton.isHovered() == True:
                    from main import beginGame
                    beginGame()
                if controlsbutton.isHovered() == True:
                    print("hello there")
                for i in range(9):
                    if backingArray1[i].isHovered() == True and i != 2 and 1 != 8:
                        finalChoice1 = i
                        print("Player 1 has chosen: " + str(finalChoice1))
                    if backingArray2[i].isHovered() == True and i != 0 and 1 != 8:
                        print(i)
                        finalChoice2 = i
                        print("Player 2 has chosen: " + str(finalChoice2))
                
                if startbutton.isHovered() == True:
                    rungame(finalChoice1, finalChoice2)
                    finalChoice1 = -1
                    finalChoice2 = -1
                        

        

        drawShips(finalChoice1, finalChoice2) 

        backbutton.checkForHover()
        controlsbutton.checkForHover()
        SCREEN.blit(backbutton.getImage(), (50, 650))
        SCREEN.blit(controlsbutton.getImage(), (600, 650))
        if finalChoice1 != -1 and finalChoice2 != -1:
            SCREEN.blit(startbutton.getImage(), (320, 300))
            startbutton.checkForHover()
        pygame.display.update()

