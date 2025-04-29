#this is where all the buttons are created and kept for later use
import pygame
pygame.init()
import os

from buttons import *

coordinateArray1 = [[50, 210], [170, 210], [290, 210], [50, 350], [170, 350], [290, 350], [50, 490], [170, 490], [290, 490]]
coordinateArray2 = [[610, 210], [730, 210], [870, 210], [610, 350], [730, 350], [870, 350], [610, 490], [730, 490], [870, 490]]

playbutton = Buttons(400, 600, 200, 50, pygame.image.load(os.path.join("Assets", "Words", "buttons", "play.png")), pygame.image.load(os.path.join("Assets", "Words", "buttons", "play-hover.png")))
backbutton = Buttons(50, 650, 200, 20, pygame.image.load(os.path.join("Assets", "Words", "buttons", "back.png")), pygame.image.load(os.path.join("Assets", "Words", "buttons", "back-hover.png")))
controlsbutton = Buttons(600, 650, 350, 35, pygame.image.load(os.path.join("Assets", "Words", "buttons", "controls.png")),pygame.image.load(os.path.join("Assets", "Words", "buttons", "controls-hover.png")))
startbutton = Buttons(320, 300, 340, 35, pygame.image.load(os.path.join("Assets", "Words", "buttons", "start.png")), pygame.image.load(os.path.join("Assets", "Words", "buttons", "start-hover.png")))

backingArray1 = []
for i in range(9):
    backingArray1.append(Buttons(coordinateArray1[i][0], coordinateArray1[i][1], 110, 110, pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "Ships", "shipbutton.png")), (110, 110)), pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "Ships", "shipbutton-select.png")), (110, 110))))

backingArray2 = []
for i in range(9):
    backingArray2.append(Buttons(coordinateArray2[i][0], coordinateArray2[i][1], 110, 110, pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "Ships", "shipbutton.png")), (110, 110)), pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "Ships", "shipbutton-select.png")), (110, 110))))