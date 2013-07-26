import pygame
import sys
from time import sleep
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SILVER = (192, 192, 192)
GOLD = (255, 215, 0)

#INFORMATION
"""
Important Info!!!!
grid is 50x50
each grid is 10x10 pixels
start player at [3][3] and [46][46]
player vehicle is 1x1 box
blue is 1
red is 2
neither is 0
"""
def main():
    global FPSCLOCK, DISPLAYSURFACE
    FPS = 30
    FPSCLOCK = pygame.time.Clock()
    #initialization of game
    pygame.init()
    #size of game screen
    size = 551
    pygame.display.set_caption("Tron Game")
    DISPLAYSURFACE = pygame.display.set_mode((size, size))

    #initialization variables
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    
    grid = [[0 for i in range(50)] for j in range(50)]
    player1Direction = "UP"
    player2Direction = "DOWN"

    player1Life = True
    player2Life = True

    #Player start locations
    player1X = 45
    player1Y = 45
    player2X = 4
    player2Y = 4

    #Check if players are ready
    DISPLAYSURFACE.fill(SILVER)
    FONT = pygame.font.Font('freesansbold.ttf', 18)
    keySurface = FONT.render("Press any key to start!", True, BLACK)
    keyRect = keySurface.get_rect()
    keyRect.topleft = (551/2-95, 551/2-50)
    DISPLAYSURFACE.blit(keySurface, keyRect)
    pygame.display.update()
    pygame.event.clear()
    pressAnyKey()
    for x in range(3, 0, -1):
        DISPLAYSURFACE.fill(SILVER)
        keySurface = FONT.render(str(x), True, BLACK)
        keyRect = keySurface.get_rect()
        keyRect.topleft = (551/2, 551/2 - 25)
        DISPLAYSURFACE.blit(keySurface, keyRect)
        pygame.display.update()
        sleep(1)
    pygame.event.clear()
    while True:
        display(grid)
        displayPlayer(player1X, player1Y, player2X, player2Y)
        #Check for gameovers/draws
        #Check for out of bounds collision
        if player1X < 0 or player1Y < 0 or player1X > 49 or player1Y > 49:
            player1Life = False
        if player2X < 0 or player2Y < 0 or player2X > 49 or player2Y > 49:
            player2Life = False
        if not player1Life and not player2Life:
            gameDraw(grid)
        if not player1Life:
            gameOver(1, grid)
        elif not player2Life:
            gameOver(2, grid)
        #Test for collisions with enemy trail/self
        if grid[player1X][player1Y] != 0:
            player1Life = False
        if grid[player2X][player2Y] != 0:
            player2Life = False
        if not player1Life and not player2Life:
            gameDraw(grid)
        if not player1Life:
            gameOver(1, grid)
        elif not player2Life:
            gameOver(2, grid)
        #event getter
        for event in pygame.event.get():
            if event.type == QUIT:
                quitGame()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and player1Direction != RIGHT:
                    player1Direction = LEFT
                elif event.key == K_RIGHT and player1Direction != LEFT:
                    player1Direction = RIGHT
                elif event.key == K_UP and player1Direction != DOWN:
                    player1Direction = UP
                elif event.key == K_DOWN and player1Direction != UP:
                    player1Direction = DOWN
                elif event.key == K_a and player2Direction != RIGHT:
                    player2Direction = LEFT
                elif event.key == K_d and player2Direction != LEFT:
                    player2Direction = RIGHT
                elif event.key == K_s and player2Direction != UP:
                    player2Direction = DOWN
                elif event.key == K_w and player2Direction != DOWN:
                    player2Direction = UP
        grid[player1X][player1Y] = 1
        grid[player2X][player2Y] = 2
        if player1Direction == LEFT:
            player1X -= 1
        elif player1Direction == RIGHT:
            player1X += 1
        elif player1Direction == DOWN:
            player1Y += 1
        elif player1Direction == UP:
            player1Y -= 1
        if player2Direction == LEFT:
            player2X -= 1
        elif player2Direction == RIGHT:
            player2X += 1
        elif player2Direction == DOWN:
            player2Y += 1
        elif player2Direction == UP:
            player2Y -= 1
        pygame.display.update()
        FPSCLOCK.tick(FPS)
#Displays graphics
def display(grid):
    DISPLAYSURFACE.fill(SILVER)
    for x in range(0, 51):
        location = (x * 10 + x)
        pygame.draw.line(DISPLAYSURFACE, WHITE, (0, location), (549, location))
        pygame.draw.line(DISPLAYSURFACE, WHITE, (location, 0), (location, 549))
    #Color each grid that has already been occupied
    for x in range(0, 50):
        for y in range(0, 50):
            colorSquare(x, y, grid)
def displayPlayer(player1X, player1Y, player2X, player2Y):
    #Color the player
    colorPlayer(player1X, player1Y, BLUE)
    colorPlayer(player2X, player2Y, RED)
    #Color the grid around the player to distinguish
    colorGridAroundPlayer(player1X, player1Y)
    colorGridAroundPlayer(player2X, player2Y)
def gameOverDisplay(grid):
    DISPLAYSURFACE.fill(SILVER)
    for x in range(0, 51):
        location = (x * 10 + x)
        pygame.draw.line(DISPLAYSURFACE, WHITE, (0, location), (549, location))
        pygame.draw.line(DISPLAYSURFACE, WHITE, (location, 0), (location, 549))
    #Color each grid that has already been occupied
    for x in range(0, 50):
        for y in range(0, 50):
            colorSquare(x, y, grid)
    pygame.display.update()
    sleep(1.5)
    pressAnyKey()
    main()
#Function that waits for a key to be pressed
def pressAnyKey():
    pygame.event.clear()
    start = True
    while start:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key == K_ESCAPE:
                    quitGame()
                start = False    
#function to color each grid in the game
def colorSquare(x, y ,tempGrid):
    if tempGrid[x][y] == 0:
        return
    elif tempGrid[x][y] == 1:
        color = BLUE
    elif tempGrid[x][y] == 2:
        color = RED
    elif tempGrid[x][y] == 3:
        color = GOLD
    elif tempGrid[x][y] == 4:
        color = BLACK
    elif tempGrid[x][y] == 5:
        color = WHITE
    locationX = (x * 10 + x) + 1
    locationY = (y * 10 + y) + 1
    pygame.draw.rect(DISPLAYSURFACE, color, (locationX, locationY, 10, 10))
    return
#color player
def colorPlayer(x, y, color):
    locationX = (x * 10 + x) + 1
    locationY = (y * 10 + y) + 1
    pygame.draw.rect(DISPLAYSURFACE, color, (locationX, locationY, 10, 10))
    return
#Color the lines around the player
def colorGridAroundPlayer(x, y):
    locationX = (x * 10 + x)
    locationY = (y * 10 + y)
    pygame.draw.line(DISPLAYSURFACE, BLACK, (locationX, locationY), (locationX, locationY + 11))
    pygame.draw.line(DISPLAYSURFACE, BLACK, (locationX, locationY), (locationX + 11, locationY))
    pygame.draw.line(DISPLAYSURFACE, BLACK, (locationX + 11, locationY), (locationX + 11, locationY + 11))
    pygame.draw.line(DISPLAYSURFACE, BLACK, (locationX, locationY + 11), (locationX + 11, locationY + 11))
#Function for gameover
def gameOver(player, grid):
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
    grid[0][0] = player
    for x in range(0, 50):
        for y in range(0, x):
            grid[x][y] = player
            grid[y][x] = player
            grid[x][x] = player
        display(grid)
        pygame.display.update()
    for x in range(3, 47):
        grid[x][8] = 3
        grid[x][41] = 3
        #print gold box
        grid[x][24] = 3
        grid[x][25] = 3
    #print gold box
    for x in range(4, 46):
        grid[x][9] = 3
        grid[x][40] = 3
    for y in range(8, 42):
        grid[3][y] = 3
        grid[4][y] = 3
    for y in range(8, 42):
        grid[46][y] = 3
        grid [45][y] = 3
    gameOverDisplay(grid)
#Function for game draws
def gameDraw(grid):
    for x in range(0, 50):
        for y in range(0, 50):
            grid[x][y] = 1
            grid[y][x] = 2
            grid[x][x] = 4
        display(grid)
        pygame.display.update()
    #printing gold box
    for x in range(3, 47):
        grid[x][13] = 3
        grid[x][36] = 3
    for x in range(4, 46):
        grid[x][14] = 3
        grid[x][35] = 3
    for y in range(13, 36):
        grid[3][y] = 3
        grid[4][y] = 3
    for y in range(13, 37):
        grid[46][y] = 3
        grid [45][y] = 3
    gameOverDisplay(grid)
#function to quit the game
def quitGame():
    pygame.quit()
    sys.exit()

#initiate the game
if __name__ == "__main__":
    main()
