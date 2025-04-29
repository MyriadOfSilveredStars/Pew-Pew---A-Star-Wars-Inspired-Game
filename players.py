from assetfiles import *

class GenericPlayer:
    def __init__(self, pShip, pNum):
        self.playerShip = pShip
        self.playerHP = self.playerShip.getHealth()
        self.bullets = []
        self.velocity = 7
        self.height = self.playerShip.rect.height
        self.width = self.playerShip.rect.width
        self.isDisabled = False
        self.bulletcooldown = 0
        self.playerNumber = pNum

    def drawPlayer(self):
        SCREEN.blit(self.playerShip.getImage(), (self.playerShip.rect.x, self.playerShip.rect.y))

    def movePlayer(self, direction):
        if direction == "up":
            self.playerShip.updateYPos(-self.velocity)
        if direction == "left":
            self.playerShip.updateXPos(-self.velocity)
        if direction == "down":
            self.playerShip.updateYPos(self.velocity)
        if direction == "right":
            self.playerShip.updateXPos(self.velocity)

    def getIfDisabled(self):
        return self.isDisabled
    
    def setIsDisabled(self):
        if self.isDisabled == False:
            self.isDisabled = True
        if self.isDisabled == True:
            self.isDisabled = False

    def takeDamage(self):
        self.playerHP -= 1

    def getCurrentHealth(self):
        return self.playerHP

    def getBullets(self):
        return self.bullets

    def handleMovement1(self, key):
        if key[pygame.K_w] and self.playerShip.rect.y > 0:
            self.movePlayer("up")
        if key[pygame.K_a] and self.playerShip.rect.x > 0:
            self.movePlayer("left")
        if key[pygame.K_s] and self.playerShip.rect.y < 600 - self.height:
            self.movePlayer("down")
        if key[pygame.K_d] and self.playerShip.rect.x < BORDER.x - self.width:
            self.movePlayer("right")

        if key[pygame.K_f] and len(self.bullets) < self.playerShip.getMaxBullets():
            pewsound.play()
            #pew pew code here
            if self.playerShip.getCannons() == 2 and self.bulletcooldown == 0:
                self.bullets.append(self.playerShip.spawnBullets(RED, pygame.Rect(self.playerShip.rect.x + self.width, self.playerShip.rect.y + 10, 10, 5)))
                self.bullets.append(self.playerShip.spawnBullets(RED, pygame.Rect(self.playerShip.rect.x + self.width, self.playerShip.rect.y + 30, 10, 5)))
            if self.playerShip.getCannons() == 1 and self.bulletcooldown == 0:
                self.bullets.append(self.playerShip.spawnBullets(RED, pygame.Rect(self.playerShip.rect.x + self.width, self.playerShip.rect.y + 10, 10, 5)))
            self.bulletcooldown = 5

        if key[pygame.K_v]:
            self.playerShip.doPowerup(1)
            

    def handleMovement2(self, key):
        if key[pygame.K_UP] and self.playerShip.rect.y > 0:
            self.movePlayer("up")
        if key[pygame.K_LEFT] and self.playerShip.rect.x > BORDER.x + 10:
            self.movePlayer("left")
        if key[pygame.K_DOWN] and self.playerShip.rect.y < 600 - self.height:
            self.movePlayer("down")
        if key[pygame.K_RIGHT] and self.playerShip.rect.x < WIDTH - self.width:
            self.movePlayer("right")

        if key[pygame.K_RCTRL] and len(self.bullets) < self.playerShip.getMaxBullets():
            pewsound.play()
            #pew pew code here
            if self.playerShip.getCannons() == 2 and self.bulletcooldown == 0:
                self.bullets.append(self.playerShip.spawnBullets(GREEN, pygame.Rect(self.playerShip.rect.x - 5, self.playerShip.rect.y + 10, 10, 5)))
                self.bullets.append(self.playerShip.spawnBullets(GREEN, pygame.Rect(self.playerShip.rect.x - 5, self.playerShip.rect.y + 30, 10, 5)))
            if self.playerShip.getCannons() == 1 and self.bulletcooldown == 0:
                self.bullets.append(self.playerShip.spawnBullets(GREEN, pygame.Rect(self.playerShip.rect.x - 5, self.playerShip.rect.y + 10, 10, 5)))
            self.bulletcooldown = 5

        if key[pygame.K_LSHIFT]:
            self.playerShip.doPowerup(2)

    def doBulletCooldown(self):
        if self.bulletcooldown != 0:
            self.bulletcooldown -= 1

    def toString(self):
        return "Player " + self.playerNumber + " wins!";

