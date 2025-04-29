import pygame
pygame.init()
import os

class Buttons:
    def __init__(self, pX, pY, pWidth, pHeight, pImage, pHoverImage):
        self.img = pImage
        self.hover = pHoverImage
        self.rect = pygame.Rect(pX, pY, pWidth, pHeight)
        self.hovered = False
        self.currentImg = self.img
        self.chosen = False

    def getImage(self):
        self.handleHovering()
        return self.currentImg
    
    def getHoverImage(self):
        return self.hover
    
    def isHovered(self):
        return self.hovered
    
    def isChosen(self):
        return self.chosen
    
    def setChosen(self):
        self.chosen = True
    
    def handleHovering(self):
        if self.hovered == True:
            self.currentImg = self.hover
        else:
            self.currentImg = self.img

    def checkForHover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

class Bullets:
    def __init__(self, velocity, colour, pX, pY, pWidth, pHeight):
        self.vel = velocity
        self.col = colour
        self.x = pX
        self.y = pY
        self.width = pWidth
        self.height = pHeight

    def getXCoord(self):
        return self.x
    
    def getYCoord(self):
        return self.y
    
    
