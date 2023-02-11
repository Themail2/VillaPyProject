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


# The grid where the Puyos will live. The grid is 8x20 for 160 tiles to hold Puyos. Each tile can hold one Puyo.
class GameGrid():
    #Constructor for GameGrid Object
    def __init__(self):
        # List Comprehension 😎
        self.container = [["Empty" for x in range(8)] for y in range(15)]

    def drawGrid(self):
        for row in range(len(self.container)):
            for col in range(len(self.container[row])):
                if self.container[row][col] == "Empty":
                    pygame.draw.rect(win, WHITE, [(gridMargin + gridWidth) * col + gridMargin, (gridMargin + gridHeight) * row + gridMargin, gridWidth, gridHeight])
                if self.container[row][col] == "Green":
                    pygame.draw.circle(win, GREEN, [((gridMargin + gridWidth) * col + gridMargin)+25, ((gridMargin + gridHeight) * row + gridMargin)+25], 25)
                if self.container[row][col] == "Red":
                    pygame.draw.circle(win, RED, [((gridMargin + gridWidth) * col + gridMargin)+25, ((gridMargin + gridHeight) * row + gridMargin)+25],25)
                if self.container[row][col] == "Blue":   
                    pygame.draw.circle(win, BLUE, [((gridMargin + gridWidth) * col + gridMargin)+25, ((gridMargin + gridHeight) * row + gridMargin)+25],25)
                if self.container[row][col] == "Purple":
                    pygame.draw.circle(win, PURPLE, [((gridMargin + gridWidth) * col + gridMargin)+25, ((gridMargin + gridHeight) * row + gridMargin)+25],25)
                if self.container[row][col] == "Yellow":
                    pygame.draw.circle(win, YELLOW, [((gridMargin + gridWidth) * col + gridMargin)+25, ((gridMargin + gridHeight) * row + gridMargin)+25],25)  
    def gravity(self):
        for row in range(len(self.container)):
            for col in range(len(self.container[row])):
                
                if self.container[14-row][7-col] == "Green" or self.container[14-row][7-col] == "Red" or self.container[14-row][7-col] == "Blue" or self.container[14-row][7-col] == "Purple" or self.container[14-row][7-col] == "Yellow":
                    try:
                        if self.container[14-row+1][7-col] == "Empty":
                            self.container[14-row+1][7-col] = self.container[14-row][7-col]
                            self.container[14-row][7-col] = "Empty"
                    except:
                        pass

def redrawWindow():
    win.fill((255,255,255))
    pygame.display.update()


def main():
    run = True
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Instanciates the GameGrid Object
    grid = GameGrid()
    frames = 0
    grid.container[1][0] = "Green"
    grid.container[2][4] = "Blue"
    grid.container[4][3] = "Purple"
    grid.container[7][7] = "Red"
    grid.container[10][7] = "Yellow"
    grid.container[12][7] = "Blue"
    while run:
        clock.tick(60)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
        # Draws the game grid
        frames += 1
        if frames == 60:
            grid.gravity()
            frames = 0

        grid.drawGrid()  
          
        # Updates the screen
        pygame.display.flip()
                  
    # Limit to 60 frames per second
    
main()