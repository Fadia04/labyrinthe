from random import randint
import pygame
from pygame.locals import *

from constants import *


pygame.init()

class Maze:
    
    def __init__(self):
        self.file = "Maze.txt"
        self.player = Player
    def load(self):
        structure_maze = []
        with open(self.file, "r") as filename:
            for line in filename:
                line_maze = []
                for letter in line:
                    if letter != "\n":
                        line_maze.append(letter)
                structure_maze.append(line_maze)
                self.structure = structure_maze
            #return structure_maze
        
    def display(self, window):
        window = pygame.display.set_mode((450, 450))
        pygame.display.set_caption(window_title)
        WALL = pygame.image.load("images/wall.png").convert()
        MG = pygame.image.load("images/macgyver.png").convert_alpha() 
        GOAL = pygame.image.load("images/gardian.png").convert_alpha()
        FLOOR = pygame.image.load("images/floor.png").convert()
        ETHER = pygame.image.load("images/ethertest.png").convert()
        ETHER.set_colorkey(BLACK)
        NEEDLE = pygame.image.load("images/needletest.png").convert()
        NEEDLE.set_colorkey(BLACK)
        PIPE = pygame.image.load("images/pipetest.png").convert()
        PIPE.set_colorkey(WHITE)
        accueil = pygame.image.load("images/title.PNG").convert()
        SYRINGE = pygame.image.load("images/seringue.png").convert_alpha()
        SYRINGE.set_colorkey(WHITE)

        num_line = 0
        for line in self.structure:
            num_col = 0
            for letter in line:     
                x = num_col * letter_size
                y = num_line * letter_size
                if letter == '#':
                    window.blit(WALL, (x,y))
                elif letter == 'p'or letter == "M":
                    window.blit(MG, (x,y))
                elif letter == 'g':
                    window.blit(GOAL, (x,y))
                elif letter == " ":
                    window.blit(FLOOR, (x,y))
                elif letter == "E":
                    window.blit(ETHER, (x,y))
                elif letter == "N":
                    window.blit(NEEDLE, (x,y))  
                elif letter == "T":
                    window.blit(PIPE, (x,y))      
                num_col += 1
            num_line += 1   
               
  
    def display_status(self, structure_maze, x, y, object_inventory):       
        if len(object_inventory) == 3:
            window.blit(SYRINGE, (0,0))
        if "E" in object_inventory:
            window.blit(ETHER,(35, 0))
        if "N" in object_inventory:
            window.blit(NEEDLE,(70, 0))
        if "T" in object_inventory:
            window.blit(PIPE,(105, 0))
    
        #pygame.display.flip()          

class Player:
    def __init__(self, structure_maze):
        self.structure_maze = structure_maze 
        for x in self.structure_maze:
            print(x)          
        self.position_x = 1
        self.position_y = 1
        self.x = 1
        self.y = 1
        
    def position(self, direction):
        if direction == "q":
            print("haut")
            if self.position_x > 0:
                print("condition 1")
                if self.structure_maze[self.position_y][self.position_x-1] != "#":
                    print("condition 2")
                    self.position_x -= 1
                    self.x = self.position_x*30
        elif direction == "d":
            if self.position_x < (len(self.structure_maze) - 1):
                if self.structure_maze[self.position_y][self.position_x+1] != "#":
                    self.position_x += 1 
                    self.x = self.position_x*30 
        elif direction == "z":
            if self.position_y > 0:
                if self.structure_maze[self.position_y-1][self.position_x] != "#":
                    self.position_y -= 1
                    self.y = self.position_y*30
        elif direction == "s":
            print("bas")
            if self.position_y < (len(self.structure_maze) - 1):
                print("condition 1")
                if self.structure_maze[self.position_y+1][self.position_x] != "#":
                    print("condition 2")
                    self.position_y += 1 
                    self.y = self.position_y*30
        return (self.position_x, self.position_y)           

  
class Items:
    
    def __init__(self, pos_x, pos_y, image, structure_maze, collected):
        self.structure_maze = structure_maze    
        self.pos_x = pos_x
        self.pos_y = pos_y 
        self.x = pos_x
        self.y = pos_y
        self.image = image
        self.collected = True

        #ether = pygame.image.load("ethertest.png").convert_alpha()
        #needle = pygame.image.load("needletest.png").convert_alpha()
        #pipe = pygame.image.load("pipetest.png").convert_alpha()
    
    def random_position(self):
        while True:
            self.pos_y = randint(0, 14)
            self.pos_x = randint(0, 14)
            if self.structure_maze[self.pos_y][self.pos_x] == " ":
                self.x = self.pos_x 
                self.y = self.pos_y 
                return (self.y, self.x)
         
    def position_object(self, structure_maze):
        for object in ["E", "N", "T"]:
            self.object_y, self.object_x = self.random_position()
            self.structure_maze[self.object_y][self.object_x] = object
    
        
                    
