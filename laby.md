import pygame
from pygame.locals import *
from Classes import *
from constants import *
        

pygame.init()
window = pygame.display.set_mode((450, 450))
#WALL = pygame.image.load("images/wall.png").convert()
MG = pygame.image.load("images/macgyver.png").convert_alpha() 
#GOAL = pygame.image.load("images/gardian.png").convert_alpha()
#FLOOR = pygame.image.load("images/floor.png").convert()
ETHER = pygame.image.load("images/ethertest.png").convert_alpha()
NEEDLE = pygame.image.load("images/needletest.png").convert()
PIPE = pygame.image.load("images/pipetest.png").convert_alpha()
#accueil = pygame.image.load("images/title.PNG").convert()
fond = pygame.image.load("images/fond.jpg").convert()
window.blit(fond, (0,0))
x = 1
y = 1

#position_x = 0
#position_y = 0
#structure_maze = load()
#position_object(structure_maze)
#random_position(structure_maze)
#player.position(direction)
object_inventory = []
structure_maze = Maze()

structure_maze.load()
structure_maze.display(window)
player =Player(structure_maze.structure)
item = Items(1, 1, ETHER, structure_maze.structure, True)
ether_obj = Items(5, 5, ETHER, structure_maze, True)
pipe_obj = Items(6, 6, ETHER, structure_maze, True)
item.random_position()
item.position_object(structure_maze)

#window = pygame.display.set_mode((450, 450))
#pygame.display.set_caption(window_title)
#pygame.display.flip()
#continue_game = 1
while True:
    accueil = pygame.image.load("images/title.png").convert()
    window.blit(accueil, (0, 0))
    pygame.display.flip()
    continue_game = 1
    continue_accueil = 1

    pipe_not_collected = True

    
    while continue_accueil:
        for event in pygame.event.get():
            if event.type == QUIT:
                continue_accueil = 0
                continue_game = 1
            if event.type == KEYDOWN:				
               if event.key == K_F1:
                    continue_accueil = 0
                    continue_game = 1
                    
        structure_maze = Maze()
        structure_maze.load()
        structure_maze.display(window)
        

    ETHER = pygame.image.load("images/ethertest.png").convert_alpha()
    NEEDLE = pygame.image.load("images/needletest.png").convert()
    PIPE = pygame.image.load("images/pipetest.png").convert_alpha()
    SYRINGE = pygame.image.load("images/seringue.png").convert_alpha()    
    GAME_WON = pygame.image.load("images/game_won1.png").convert()
    GAME_OVER = pygame.image.load("images/game_over1.png").convert()

    #display(structure_maze)
    #continue_game = 1
    while True:
        #if continue_game == 0
            #continue
        #print(str(player.x) + " " +str(player.y))
        for event in pygame.event.get():
            if event.type == QUIT:
                continue_game = 0
                exit() 
            elif event.type == KEYDOWN:
                print("keydown")
                if event.key == pygame.K_LEFT:
                    print("move")
                    player.position ("q") 
                if event.key == pygame.K_RIGHT:
                    print("move 1")
                    player.position ("d")
                if event.key == pygame.K_UP:
                    print("move 2")
                    player.position ("z")
                if event.key == pygame.K_DOWN:
                    print("move 3")
                    player.position ("s")
                
                #structure_Maze = Maze()
                structure_maze.display(window)
                window.blit(MG, (player.x, player.y))
                window.blit(ETHER, (5, 0))
                #if pipe_not_collected = True:
                window.blit(PIPE, (35, 0))
                window.blit(NEEDLE, (70, 0))
                pygame.display.flip()

        
                
                #structure_maze[y][x] = " "   
                #x, y = position(x, y, direction, structure_maze)
                #print(x, y)
        
                #if structure_maze[y][x] in ["E", "N", "T"]:
                    #object_inventory.append(structure_maze[y][x])
                #print(object_inventory)
                
        """     elif structure_maze[y][x] in ["g"]:
                    if len(object_inventory) == 3:
                        window.blit(GAME_WON,(20, 180))
                        pygame.display.flip()
                        #continue_game = 0
                        print("Game won")
                        
                    else:
                        window.blit(GAME_OVER, (20, 180))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        print("Game over")
                    
                    break
                elif len(object_inventory) == 3:    
                    window.blit(SYRINGE, (0,0))
                    pygame.display.flip()    
                    
                structure_maze[y][x] = "M"
                pygame.display.flip()
                display(structure_maze) 
"""                
        structure_maze.display_status(structure_maze, x, y, object_inventory)                               

#pygame.display.flip()