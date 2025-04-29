#This is where the actual game runs

#importing as usual
import pygame
pygame.init()

from ships import *
from environment import *
from players import *

from assetfiles import *
from buttonassets import *

def drawgame(player1, player2):
    #function to draw the assets to the screen
    gameScreen()

    #draw the player's health onto the screen
    SCREEN.blit(OPTION_FONT.render("Health: " + str(player1.getCurrentHealth()), 1, YELLOW), (50, 620))
    SCREEN.blit(OPTION_FONT.render("Health: " + str(player2.getCurrentHealth()), 1, YELLOW), (550, 620))

    #players have their own drawing method
    player1.drawPlayer()
    player2.drawPlayer()

    #draw all the bullets currently in the air
    for bullet in player1.getBullets():
        pygame.draw.rect(SCREEN, bullet.getColour(), bullet.getRect())
    for bullet in player2.getBullets():
        pygame.draw.rect(SCREEN, bullet.getColour(), bullet.getRect())

    pygame.display.update() #never forget to update!

def handleBullets(player1, player2):
    #function to handle bullet movement
    for bullet in player1.getBullets():
        if bullet.rect.x > WIDTH:
            player1.bullets.remove(bullet)
        if player2.playerShip.rect.colliderect(bullet.rect):
            player1.bullets.remove(bullet)
            player2.takeDamage()
        else:
            bullet.moveBullet(1)
    for bullet in player2.getBullets():
        if bullet.rect.x < 0:
            player2.bullets.remove(bullet)
        if player1.playerShip.rect.colliderect(bullet.rect):
            player2.bullets.remove(bullet)
            player1.takeDamage()
        else:
            bullet.moveBullet(2)

def checkForDeaths(player1, player2):
    if player1.getCurrentHealth() == 0:
        print("ohes noes")
        return 1
    if player2.getCurrentHealth() == 0:
        print("noes ohes")
        return 2
    else:
        return 0
    
def doEsplosion(winner, winnerNum, loserx, losery):
    for counter in range(boom_list_size):
        gameScreen()
        winner.drawPlayer()

        boom = pygame.image.load(os.path.join("Assets", "Ships", "imgs_explode", boom_list[counter]))
        SCREEN.blit(boom, (loserx, losery))
        pygame.display.update()

    for count in range(400):
        if winnerNum == 1:
            gameScreen()
            SCREEN.blit(player1wins, (20, 150))
            winner.drawPlayer()
        if winnerNum == 2:
            gameScreen()
            SCREEN.blit(player2wins, (20, 150))
            winner.drawPlayer()
        pygame.display.update()
        count += 1


def rungame(choice1, choice2):
    gameScreen()
    pygame.display.update()

    clock = pygame.time.Clock()
    running = True
    loser = 0

    player1 = GenericPlayer(allLeftShips[choice1], 1)
    player2 = GenericPlayer(allRightShips[choice2], 2)
    
    while running == True:
        keys_pressed = pygame.key.get_pressed()
        clock.tick(FPS)

        for event in pygame.event.get():
            closeGame(event)

        if player1.getIfDisabled() == False:
            player1.handleMovement1(keys_pressed)

        if player2.getIfDisabled() == False:
            player2.handleMovement2(keys_pressed) 

        player1.doBulletCooldown()
        player2.doBulletCooldown()
        handleBullets(player1, player2)

        loser = checkForDeaths(player1, player2)
        if loser != 0:
            running = False
        drawgame(player1, player2)
    
    if loser == 1:
        doEsplosion(player2, 2, player1.playerShip.rect.x - 50, player1.playerShip.rect.y - 50)
    if loser == 2:
        doEsplosion(player1, 1, player2.playerShip.rect.x -50, player2.playerShip.rect.y - 50)