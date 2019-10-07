##!/usr/bin/env python3
# coding: utf-8
import pygame
from classes.characters import Character
from classes.display import Display
from classes.map import Map
from classes.items import Item
from classes.gyver import MacGyver
from config import BOT_LEFT, BOT_RIGHT

#pylint: disable=E1101
class Main():

    def __init__(self):
        #setting the pygame window
        title = "MacGyver's Maze"
        display = Display(600, 650, title)

        #Setting the map
        mapping = Map("mapping.txt")
        display.set_map(mapping)

        #Setting the characters
        bad_guy = Character(1, 14, "guardian.png", mapping)
        gyver = MacGyver(14, 0, "macgyver.png", mapping)
        display.set_characters(gyver, bad_guy)

        pygame.display.flip()

        self._start_game(mapping, gyver, bad_guy, display)

    @staticmethod
    def check_encounter(gyver, bad_guy, display):
        #When MacGyver moves to bad_guy position and picks up 3 objects, 
        # the victory message is displayed and the game is over
        if(gyver.x_pos == bad_guy.x_pos and gyver.y_pos == bad_guy.y_pos):
            if gyver.bag == 3:
                end = "Congratulations, you won !"
            #When MacGyver moves to bad_guy position and picks up less than 3 objects,
            # the defeat message is displayed and the game is over
            else:
                end = "You lost !"
            display.game_over(end)
            return True
        return None

    @staticmethod
    def set_items(mapping, display):  #pylint: disable=W0613
        tube = Item('tube', 'tube.png', mapping)
        ether = Item('ether', 'ether.png', mapping)
        needle = Item('needle', 'needle.png', mapping)
        items = [tube, ether, needle]
        display.set_items(items)
        pygame.display.flip()
        return items

    def _start_game(self, mapping, gyver, bad_guy, display):
        #Define the starting messages 
        items = self.set_items(mapping, display)
        message = 'You collected 0/3 items'
        display.show_message(message, BOT_RIGHT)
        message = 'Collect all items to defeat the guardian'
        display.show_message(message, BOT_LEFT)
        
        #Main game loop
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                old_position = {"y_pos": gyver.y_pos, "x_pos": gyver.x_pos}
                if event.type == pygame.QUIT: #If the gamer uses the quit key, the game is over
                    game_over = True
                #Using directional keys to move MacGyver
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        gyver.moving('top')
                    elif event.key == pygame.K_DOWN:
                        gyver.moving('bottom')
                    elif event.key == pygame.K_RIGHT:
                        gyver.moving('right')
                    elif event.key == pygame.K_LEFT:
                        gyver.moving('left')

                    display.move_character(mapping, gyver, items, old_position)
                    game_over = self.check_encounter(gyver, bad_guy, display)


if __name__ == "__main__":
    MAIN = Main()
