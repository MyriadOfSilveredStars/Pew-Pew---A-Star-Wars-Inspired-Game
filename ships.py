#The base class for all ships
from bullets import *
import random
from assetfiles import *

class GenericShips:
    def __init__(self, pHealth, pRect, pImage, pCannons, pBullets):
        self.hp = pHealth
        self.rect = pRect
        self.img = pImage
        self.cannon = pCannons
        self.maxBullets = pBullets

    def getHealth(self):
        return self.hp

    def getMaxBullets(self):
        return self.maxBullets
    
    def getCannons(self):
        return self.cannon
    
    def setVelocity(self, newVelocity):
        self.vel = newVelocity
    
    def updateXPos(self, playerVel):
        self.rect.x += playerVel

    def updateYPos(self, playerVel):
        self.rect.y += playerVel

    def getImage(self):
        return self.img


class XWing(GenericShips):
    def spawnBullets(self, playerColour, playerRect):
        return Bullet(15, playerColour, playerRect)
    
    def doPowerup(self):
        #the X-Wing doesn't have a powerup yet
        pass

class TIE(GenericShips):
    def spawnBullets(self, playerColour, playerRect):
        return Bullet(15, playerColour, playerRect)
    
    def doPowerup(self):
        #the TIE doesn't have a powerup yet
        pass

class N1(GenericShips):
    def spawnBullets(self, playerColour, playerRect):
        return Bullet(15, playerColour, playerRect)
    
    def doPowerup(self, player):
        #powerup for the N1 is a teleport
        if player == 1:
            self.rect.x = random.randint(0, BORDER.x - self.rect.width)
            self.rect.y = random.randint(0, 600 - self.rect.height)
    
        if player == 2:
            self.rect.x = random.randint(BORDER.x + 5, WIDTH - self.rect.width)
            self.rect.y = random.randint(0, 600 - self.rect.height)

class Razorcrest(GenericShips):
    def spawnBullets(self, playerColour, playerRect):
        return Bullet(15, playerColour, playerRect)
    
    def doPowerup(self):
        #powerup for the Razor Crest is bullet deflection
        pass

class Firespray(GenericShips):
    def spawnBullets(self, playerColour, playerRect):
        return Bullet(15, playerColour, playerRect)
    
    def doPowerup(self):
        #powerup for the Firespray is a seismic charge
        pass

class Omicron(GenericShips):
    def spawnBullets(self, playerColour, playerRect):
        return Bullet(15, playerColour, playerRect)
    
    def doPowerup(self):
        #powerup for the Marauder is an electromagnetic pulse
        pass

class LightFreighter(GenericShips):
    def spawnBullets(self, playerColour, playerRect):
        return Bullet(15, playerColour, playerRect)
    
    def doPowerup(self):
        #powerup for the Falcon is a speed boost
        pass