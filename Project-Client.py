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
# Make game grid, game grid needs to hold puyos, thinking 8x15 (120) tiles on grid 
# 
#
#
import pygame
import random
#We Initialize the window handle, window name, and constants before Class and Function delcarations for readablity

# Width and height for game window to be drawn 
width = 409
height = 700

# Displays the game window on the users screen
win = pygame.display.set_mode((width, height)) 

# Sets the Window name
pygame.display.set_caption("Puyo Puyo Client")
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

# Defining sprites for Puyos
greyPuyo = pygame.image.load("GreyPuyo.png").convert()
redPuyo = pygame.image.load("RedPuyo.png").convert()
bluePuyo = pygame.image.load("BluePuyo.png").convert()
purplePuyo = pygame.image.load("PurplePuyo.png").convert()
greenPuyo = pygame.image.load("GreenPuyo.png").convert()
yellowPuyo = pygame.image.load("YellowPuyo.png").convert()
# Sizes for the game grid draw function
gridWidth = 50
gridHeight = 50
gridMargin = 1



class Puyo():
    # Constructor for the Puyo Object
    def __init__(self, color, isMoving, masterSlave):
        # The color of the Puyo
        self.color = color
        # This object variable determines the behavior of the Puyo pairs when they are spawned
        # at the top of the game grid
        self.masterSlave = masterSlave
        # If the Puyo is controllable, True, else False
        self.isMoving = isMoving
        
# The grid where the Puyos will live. The grid is 8x15 for 120 tiles to hold Puyos. Each tile can hold one Puyo.
class GameGrid():
    #Constructor for GameGrid Object (Only takes self)
    def __init__(self):
        # List Comprehension ????
        self.container = [[Puyo("Empty", False, None) for x in range(8)] for y in range(13)]
        
        self.chains = []
        self.finalCoords = []

    #Draws the screen based on the contents of self.container()
    def drawGrid(self):
        # Traverse the 2D array (Top left to bottom right)
        for row in range(len(self.container)):
            for col in range(len(self.container[row])):
                # Put correct color object based on data in self.container
                if self.container[row][col].color == "Empty":
                    pygame.draw.rect(win, BLACK, [(gridMargin + gridWidth) * col + gridMargin, (gridMargin + gridHeight) * row + gridMargin, gridWidth, gridHeight])
                if self.container[row][col].color == "Green":
                    win.blit(greenPuyo, (((gridMargin + gridWidth) * col + gridMargin), ((gridMargin + gridHeight) * row + gridMargin)))
                if self.container[row][col].color == "Red":
                    win.blit(redPuyo, (((gridMargin + gridWidth) * col + gridMargin), ((gridMargin + gridHeight) * row + gridMargin)))
                if self.container[row][col].color == "Blue":   
                    win.blit(bluePuyo, (((gridMargin + gridWidth) * col + gridMargin), ((gridMargin + gridHeight) * row + gridMargin)))
                if self.container[row][col].color == "Purple":
                    win.blit(purplePuyo, (((gridMargin + gridWidth) * col + gridMargin), ((gridMargin + gridHeight) * row + gridMargin)))
                if self.container[row][col].color == "Yellow":
                    win.blit(yellowPuyo, (((gridMargin + gridWidth) * col + gridMargin), ((gridMargin + gridHeight) * row + gridMargin)))  
    # Moves the Puyos contained in self.container
    def gravity(self):
        # Records if a Puyo was moved
        moved = False
        # Traverse the 2D array (Bottom right to top left)
        for row in range(len(self.container)):
            for col in range(len(self.container[row])):
                # Ensures the space we are checking is not empty
                if self.container[12-row][7-col].color == "Green" or self.container[12-row][7-col].color == "Red" or self.container[12-row][7-col].color == "Blue" or self.container[12-row][7-col].color == "Purple" or self.container[12-row][7-col].color == "Yellow" or self.container[12-row][7-col].color == "Grey":
                    # Gaurds against index errors
                    if (12-row+1) <= 12:
                        # Check if the space below the Puyo is empty, if it is, move the Puyo down a space
                        # and note that a Puyo was moved
                        if self.container[12-row+1][7-col].color == "Empty":
                            self.container[12-row+1][7-col] = self.container[12-row][7-col]
                            self.container[12-row][7-col] = Puyo("Empty", False, None)
                            moved = True
                        elif self.container[12-row][7-col].isMoving == True:
                            #If one of the Puyos in the Puyo pair stop moving, we need to take away control
                            #of the moving Puyo pair completely
                            
                            for row2 in range(len(self.container)):
                                for col2 in range(len(self.container[row2])):
                                    self.container[row2][col2].isMoving = False
                    elif self.container[12-row][7-col].isMoving == True:
                        #If one of the Puyos in the Puyo pair stop moving, we need to take away control
                        #of the moving Puyo pair completely
                        for row3 in range(len(self.container)):
                                for col3 in range(len(self.container[row3])):
                                    self.container[row3][col3].isMoving = False
                        
                              
        return moved

    def checkChains(self):
        # Keeps track of if this function removed a chain when called
        didRemoveChain = False
        # Traverse the 2D array (Top left to Bottom right)
        for row in range(len(self.container)):
            for col in range(len(self.container[row])):
                # Tails is the current set of coords we are checking
                # A tail is when a Puyo finds another Puyo of its same color adjacent to it,
                # We have to check the tails of all Puyos the Puyo finds for more Puyos of the same color
                tails = []
                # Temp variable for storing tails, this is required so we don't have to append tails to the
                # list of tails as the function is itterating through the list of tails
                tempTails = []
                # Combo contains all verified spaces that are connected, this is also helpful so that
                # the same tail doesn't backtrack while searching
                combo = [(row,col)]
                #print("Starting tail:", row, col)
                # Check all adjacent squares for puyos of the same color and record their position
                if row-1>=0 and self.container[row-1][col].color == self.container[row][col].color and not(self.container[row][col].color == "Empty"):
                    #print("Search started.")
                    #print("Found new tail at: ", row-1,col)
                    tails.append((row-1,col))
                if row+1<=12 and self.container[row+1][col].color == self.container[row][col].color and not(self.container[row][col].color == "Empty"):
                    #print("Search started.")
                    #print("Found new tail at: ", row+1,col)
                    tails.append((row+1,col))
                if col-1>=0 and self.container[row][col-1].color == self.container[row][col].color and not(self.container[row][col].color == "Empty"):
                    #print("Search started.")
                    #print("Found new tail at: ", row,col-1)
                    tails.append((row,col-1))
                if col+1<=7 and self.container[row][col+1].color == self.container[row][col].color and not(self.container[row][col].color == "Empty"):
                    #print("Search started.")
                    #print("Found new tail at: ", row,col+1)
                    tails.append((row,col+1))
                # If no adjacent Puyos were found, stop
                while not(tails == []):
                    
                    # Each tail will be appended to the list as a Tuple, therfore we can access each coord by
                    # tail[0] for row and tail[1] for col, once the tail is checked, append it to the list of
                    # checked Puyos (combo), then we know which puyos to not count twice
                    tempTails = []
                    # Do this for each tail found on intial checking
                    for tail in tails:
                        #print("Checking", tail, "for tails")
                        combo.append(tail)
                        #print("Current Combo: ", combo)
                        # Check if they are the same color 
                        if tail[0]-1>=0 and self.container[tail[0]-1][tail[1]].color == self.container[tail[0]][tail[1]].color:
                            # Gaurding condition against checking a coord twice
                            if (tail[0]-1,tail[1]) not in combo:
                                #print("Found new tail at: ", tail[0]-1, tail[1])
                                tempTails.append((tail[0]-1,tail[1]))
                        # Check if they are the same color         
                        if tail[0]+1<=12 and self.container[tail[0]+1][tail[1]].color == self.container[tail[0]][tail[1]].color:
                            # Gaurding condition against checking a coord twice
                            if (tail[0]+1,tail[1]) not in combo:
                                #print("Found new tail at: ", tail[0]+1, tail[1])
                                tempTails.append((tail[0]+1,tail[1]))
                        # Check if they are the same color       
                        if tail[1]-1>=0 and self.container[tail[0]][tail[1]-1].color == self.container[tail[0]][tail[1]].color:
                            # Gaurding condition against checking a coord twice
                            if (tail[0],tail[1]-1) not in combo:
                                #print("Found new tail at: ", tail[0], tail[1]-1)    
                                tempTails.append((tail[0],tail[1]-1))
                        # Check if they are the same color        
                        if tail[1]+1<=7 and self.container[tail[0]][tail[1]+1].color == self.container[tail[0]][tail[1]].color:
                            # Gaurding condition against checking a coord twice
                            if (tail[0]+1,tail[1]) not in combo:    
                                tempTails.append((tail[0],tail[1]+1))
                        
                    # After looping through the list of tails, we have a new set of tails, so,
                    # get rid of the original set and loop through the new ones.   
                    #print( tempTails)
                    tails = tempTails
                    #print("Tails List after for loop: ", tails)
                # If chain is valid length, remove the Puyos in combo
                #THIS IS WHERE SCORE WOULD BE COUNTED
                if len(list(set(combo))) >= 4:
                    #print("Combo: ", combo)
                    #Remove duplicates
                    combo = list(set(combo))
                    
                    #Notes that a chain was removed
                    didRemoveChain = True
                    #Loop through all combo coords and remove them
                    for coord in combo:
                        
                        self.container[coord[0]][coord[1]] = Puyo("Empty", False, None)     
        return didRemoveChain            
        
    def spawnPuyos(self):
        # If these squares are not empty, then there is a Puyo there, which means you lose because 
        # your board is full
        if self.container[0][3].color != "Empty" or self.container[0][4].color != "Empty":
            return False
        #Pick a random number and place a Puyo at its spawn point based on that number
        # the [0][3] Puyo is the "Master" Puyo, which means the "Slave" Puyo will rotate around
        # the "Master" Puyo when the player rotates the Puyo pair
        rand = random.random()
        if rand < .2:
            self.container[0][3] = Puyo("Red", True, "Master")
        if rand > .2 and rand < .4:
            self.container[0][3] = Puyo("Blue", True, "Master")
        if rand > .4 and rand < .6:
            self.container[0][3] = Puyo("Green", True, "Master")
        if rand > .6 and rand < .8:
            self.container[0][3] = Puyo("Purple", True, "Master")
        if rand > .8 and rand < 1:
            self.container[0][3] = Puyo("Yellow", True, "Master")
        #Pick a random number and place a Puyo at its spawn point based on that number
        rand = random.random()
        if rand < .2:
            self.container[0][4] = Puyo("Red", True, "Slave")
        if rand > .2 and rand < .4:
            self.container[0][4] = Puyo("Blue", True, "Slave")
        if rand > .4 and rand < .6:
            self.container[0][4] = Puyo("Green", True, "Slave")
        if rand > .6 and rand < .8:
            self.container[0][4] = Puyo("Purple", True, "Slave")
        if rand > .8 and rand < 1:
            self.container[0][4] = Puyo("Yellow", True, "Slave")
        
    def movePuyos(self, event):
        if event == "Left":
            for row in range(len(self.container)):
                for col in range(len(self.container[row])):
                    if self.container[row][col].isMoving == True:
                        if col-1 >= 0:
                            if self.container[row][col-1].color == "Empty":
                                self.container[row][col-1] = self.container[row][col]
                                self.container[row][col] = Puyo("Empty", False, None)
        if event == "Right":
            for row in range(len(self.container)):
                for col in range(len(self.container[row])):
                    if self.container[12-row][7-col].isMoving == True:
                        if 7-col+1 <= 7:
                            if self.container[12-row][7-col+1].color == "Empty":
                                self.container[12-row][7-col+1] = self.container[12-row][7-col]
                                self.container[12-row][7-col] = Puyo("Empty", False, None)
        if event == "CounterClockwise":
            moved = False
            for row in range(len(self.container)):
                for col in range(len(self.container[row])):
                    if self.container[row][col].isMoving == True:
                        if self.container[row][col].masterSlave == "Slave":
                            if col+1 <= 7:
                                if self.container[row][col+1].masterSlave == "Master":
                                    #We know the master Puyo is to the right of the slave Puyo
                                    if row+1 <= 12:
                                        if moved == False:
                                            if self.container[row+1][col+1].color == "Empty":
                                                print("right")
                                                # Move it right and down
                                                self.container[row+1][col+1] = self.container[row][col]
                                                self.container[row][col] = Puyo("Empty", False, None)
                                                moved = True
                                       
                            if col-1 >= 0:
                                if self.container[row][col-1].masterSlave == "Master":
                                    #We know the master Puyo is to the left of the slave Puyo
                                    if row-1 >= 0:
                                        if moved == False:
                                            if self.container[row-1][col-1].color == "Empty":
                                                print("left")
                                                #Move it up and left
                                                self.container[row-1][col-1] = self.container[row][col]
                                                self.container[row][col] = Puyo("Empty", False, None)
                                                moved = True
                            if row+1 <= 12:
                                if self.container[row+1][col].masterSlave == "Master":
                                    #We know the master Puyo is below the slave Puyo
                                    if col-1 >= 0:
                                        if moved == False:
                                            if self.container[row+1][col-1].color == "Empty":
                                                print("below")
                                                #Move it left and down
                                                self.container[row+1][col-1] = self.container[row][col]
                                                self.container[row][col] = Puyo("Empty", False, None)
                                                moved = True
                            if row-1 >= 0:
                                if self.container[row-1][col].masterSlave == "Master":
                                    #We know the master Puyo is above the slave Puyo
                                    if col+1 <= 7:
                                        if moved ==  False:
                                            print("above")
                                            #Move it right and up
                                            if self.container[row-1][col+1].color == "Empty":
                                                self.container[row-1][col+1] = self.container[row][col]
                                                self.container[row][col] = Puyo("Empty", False, None)
                                                moved = True
                                        
                                
                                
        
# MAIN GAME LOOP
def main():
    run = True
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Instanciates the GameGrid Object
    grid = GameGrid()
    # Frame counter
    frames = 0
    # Bool for losing
    youLose = False
    # Manually populate the grid
    #grid.container[1][1] = Puyo("Blue", False, None)
    #grid.container[2][1] = Puyo("Blue", False, None)
    #grid.container[5][1] = Puyo("Blue", False, None)
    #grid.container[12][1] = Puyo("Blue", False, None)
    #grid.container[8][1] = Puyo("Blue", False, None)
    
    #Key press buffer
    keyBuffer = None
    while run:
        # Forces the game logic to run 60 times per second
        clock.tick(60)  
        #increment the frame counter
        frames += 1
        
        
        # Loops through the pygame event stack and checks if the program was closed, key events, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    keyBuffer = "Right"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keyBuffer = "Left"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    keyBuffer = "CounterClockwise"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keyBuffer = "Clockwise"
                    
        # Calling movePuyos every 5 frames give the play some more control
        if frames % 2 == 0:
            #Calls movePuyos to move Puyos based on key presses, then resets the keybuffer
            grid.movePuyos(keyBuffer)  
            keyBuffer = None 
            
        if frames == 30:
            #Calls movePuyos to move Puyos based on key presses, then resets the keybuffer
            
            
            # Need to check chains when grid.gravity() returns False
            if grid.gravity() == False:
                # If checkChains returns false, there were no chains, so we need to send more Puyos
                if grid.checkChains() == False:
                    # If we can't send more Puyos, you have lost the game
                    if grid.spawnPuyos() == False:
                        #You Lose
                        youLose = True
                        
            
        if frames == 60:
            
            # grid.gravity() moves the Puyos on the screen if they need to be moved
            # When grid.gravity() returns False, we need to check for chains
            if grid.gravity() == False:
                # If checkChains returns false, there were no chains, so we need to send more Puyos
                if grid.checkChains() == False:
                    # If we can't send more Puyos, you have lost the game
                    if grid.spawnPuyos() == False:
                        #You Lose
                        youLose = True
            # If we are on the 60th frame, reset the frame counter to 0   
            frames = 0
        # Draws the game grid
        if youLose != True:
            grid.drawGrid()  
        else:
            #Put a lose screen here or somethin
            print("YOU LOSE")
            pygame.quit()
          
        # Updates the screen
        pygame.display.flip()
                  
    
# Calls the main game loop
main()