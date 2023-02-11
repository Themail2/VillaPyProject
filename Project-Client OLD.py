# WELCOME TO!
# ________  ___  ___      ___    ___ ________     
#|\   __  \|\  \|\  \    |\  \  /  /|\   __  \    
#\ \  \|\  \ \  \\\  \   \ \  \/  / | \  \|\  \   
# \ \   ____\ \  \\\  \   \ \    / / \ \  \\\  \  
#  \ \  \___|\ \  \\\  \   \/  /  /   \ \  \\\  \ 
#   \ \__\    \ \_______\__/  / /      \ \_______\
#    \|__|     \|_______|\___/ /        \|_______|
#                       \|___|/                   
# ________  ___  ___      ___    ___ ________     
#|\   __  \|\  \|\  \    |\  \  /  /|\   __  \    
#\ \  \|\  \ \  \\\  \   \ \  \/  / | \  \|\  \   
# \ \   ____\ \  \\\  \   \ \    / / \ \  \\\  \  
#  \ \  \___|\ \  \\\  \   \/  /  /   \ \  \\\  \ 
#   \ \__\    \ \_______\__/  / /      \ \_______\
#    \|__|     \|_______|\___/ /        \|_______|
#                       \|___|/                              


# A Tanner Balk and Brett Pirro Project

#TO-DO
# Make game grid, game grid needs to hold puyos, thinking 8x20 (160) tiles on grid 
# 
#
#
import pygame

#We Initialize the window handle, window name, and constants before Class and Function definitions for readablity

# Colors that will be used in the game
# Defining them as constants make the code much more readable
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 255)
PURPLE = (205, 13, 255)
GREY = (90, 90, 90)
YELLOW = (255, 255, 0)

# Sizes for the game grid draw function
gridWidth = 50
gridHeight = 50
gridMargin = 1

# Width and height for game window to be drawn 
width = 409
height = 850

# Displays the game window on the users screen
win = pygame.display.set_mode((width, height)) 

# Sets the Window name
pygame.display.set_caption("Client")


#Puyo class for our game. Our game grid will be gradually filled with puyo objects which will have interactions with each other
#A Puyo has a position (x,y), a width and height for its size on the screen, and a color. Color is important as this game is about color matching
class Puyo():
    # Constructor for Puyo Object
    def __init__(self, x, y, width, height, color):
         self.x = x
         self.y = y
         self.width = width
         self.height = height 
         self.rect = (x,y,width,height)
         self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.rect)

    def move(self):
        pygame.keys.get_pressed()

# The grid where the Puyos will live. The grid is 8x20 for 160 tiles to hold Puyos. Each tile can hold one Puyo.
def DrawGameGrid():
    #Constructor for GameGrid Object

    def drawGrid(self):
        for row in range(15):
            for col in range(8):
                pygame.draw.rect(win, WHITE, [(gridMargin + gridWidth) * col + gridMargin, (gridMargin + gridHeight) * row + gridMargin, gridWidth, gridHeight])
                

       
def redrawWindow():
    win.fill((255,255,255))
    pygame.display.update()


def main():
    run = True
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Instanciates the GameGrid Object
    grid = GameGrid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
        # Draws the game grid   
        # Updates the screen
        pygame.display.flip()
                  
    # Limit to 60 frames per second
    clock.tick(60)  
main()