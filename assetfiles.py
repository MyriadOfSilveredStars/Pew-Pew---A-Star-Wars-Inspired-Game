#Some assets are needed across the board, so they go here
import pygame
pygame.init()
import os

from ships import *

#screen stuff
HEIGHT = 700
WIDTH = 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

#backgrounds
starrybackdrop = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Backgrounds", "genericstars.jpg")), (1000, 700))
hyperspacezoom = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Backgrounds", "hyperspacezoom.jpg")), (1000, 700))
menu_tatooine = pygame.image.load(os.path.join("Assets", "Planets", "tatooine.jpg"))

#fight screen extra bits
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
INFOBASE = pygame.Rect(0, 600, WIDTH, 100)

#sounds
pewsound = pygame.mixer.Sound(os.path.join("Assets", "Sounds", "pew.wav"))

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (89, 203, 232)

#fonts
OPTION_FONT = pygame.font.Font(os.path.join("Assets", "Words", "clonewars2.ttf"), 35)
HEADING_FONT = pygame.font.Font(os.path.join("Assets", "Words", "clonewars2.ttf"), 50)
NAME_FONT = pygame.font.Font(os.path.join("Assets", "Words", "clonewars2.ttf"), 65)
TEENY_FONT = pygame.font.Font(os.path.join("Assets", "Words", "clonewars2.ttf"), 22)

#title texts
maintitle = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Words", "title.png")), (750, 150))
fighttitle = pygame.image.load(os.path.join("Assets", "Words", "fightmodetitle.png"))

#other words
player1wins = pygame.image.load(os.path.join("Assets", "Words", "player1wins.png"))
player2wins = pygame.image.load(os.path.join("Assets", "Words", "player2wins.png"))

#esplosion
boom_list = os.listdir(os.path.join("Assets", "Ships", "imgs_explode")) # your directory path
boom_list_size = len(boom_list) - 1

#left side ship assets
xWingLeft = XWing(15, pygame.Rect(170, 210, 120, 120), pygame.transform.scale(pygame.transform.rotate(
    pygame.image.load(os.path.join("Assets", "Ships", "PlayerVers", "xwing.png")), 90), (80, 80)), 2, 4)
firesprayLeft = Firespray(20, pygame.Rect(50, 210, 120, 120), pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Ships", "PlayerVers", "slave1.png")), (50, 80)), 1, 4)
tieFighterLeft = TIE(15, pygame.Rect(50, 490, 120, 120), pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Ships", "PlayerVers", "tiefighter.png")), (80, 80)), 2, 4)
n1Left = N1(15, pygame.Rect(50, 350, 120, 120), pygame.transform.scale(pygame.transform.rotate(
    pygame.image.load(os.path.join("Assets", "Ships", "PlayerVers", "n1starfighter.png")), -90), (90, 90)), 2, 6)
razorcrestLeft = Razorcrest(25, pygame.Rect(170, 350, 120, 120), pygame.transform.scale(pygame.transform.rotate(
    pygame.image.load(os.path.join("Assets", "Ships", "PlayerVers", "razorcrest.png")), -90), (80, 80)), 2, 4)
havocLeft = Omicron(20, pygame.Rect(170, 490, 120, 120), pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Ships", "PlayerVers", "havocmarauder.png")), (80, 80)), 2, 6)
falconLeft = LightFreighter(30, pygame.Rect(290, 350, 120, 120), pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Ships", "PlayerVers", "milleniumfalcon.png")), (80, 80)), 1, 5)
allLeftShips = [firesprayLeft, xWingLeft, "null", n1Left, razorcrestLeft, falconLeft, tieFighterLeft, havocLeft, "null"]

#right side ship assets
xWingRight = XWing(15, pygame.Rect(730, 210, 120, 120), pygame.transform.scale(pygame.transform.rotate(
    pygame.image.load(os.path.join("Assets", "Ships", "PlayerVers", "xwing.png")), -90), (80, 80)), 2, 4)
firesprayRight = Firespray(20, pygame.Rect(870, 210, 120, 120), pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Ships", "EnemyVers", "slave1.png")), (50, 80)), 1, 4)
tieFighterRight = TIE(15, pygame.Rect(870, 490, 120, 120), pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Ships", "EnemyVers", "tiefighter.png")), (100, 80)), 2, 4)
n1Right = N1(15, pygame.Rect(870, 350, 120, 120), pygame.transform.scale(pygame.transform.rotate(
    pygame.image.load(os.path.join("Assets", "Ships", "EnemyVers", "n1starfighter.png")), 90), (90, 90)), 2, 6)
razorcrestRight = Razorcrest(25, pygame.Rect(730, 350, 120, 120), pygame.transform.scale(pygame.transform.rotate(
    pygame.image.load(os.path.join("Assets", "Ships", "EnemyVers", "razorcrest.png")), 90), (80, 80)), 2, 4)
havocRight = Omicron(20, pygame.Rect(730, 490, 120, 120), pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Ships", "EnemyVers", "havocmarauder.png")), (80, 80)), 2, 6)
falconRight = LightFreighter(30, pygame.Rect(610, 350, 120, 120), pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "Ships", "EnemyVers", "milleniumfalcon.png")), (80, 80)), 1, 5)
allRightShips = ["null", xWingRight, firesprayRight, n1Right, razorcrestRight, havocRight, "null", tieFighterRight, falconRight]