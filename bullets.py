import pygame
pygame.init()

class Bullet():
    def __init__(self, pVelocity, pColour, pRect):
        self.velocity = pVelocity
        self.colour = pColour
        self.rect = pRect
    
    def getVelocity(self):
        return self.velocity
    
    def getRect(self):
        return self.rect
    
    def getColour(self):
        return self.colour

    def moveBullet(self, player):
        if player == 2:
            self.rect.x -= self.velocity
        if player == 1:
            self.rect.x += self.velocity
