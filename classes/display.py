import pygame
from config import FONT, BIG_FONT, BOT_RIGHT, BOT_LEFT, TILE_SIZE, FLOOR, WALL

class Display:
    #Display the maze structure
    def __init__(self, width, height, title):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

    def game_over(self, message):
        #Set the final message
        self.window.fill((0, 0, 0))
        text = BIG_FONT.render(message, True, (255, 0, 0))
        rect = text.get_rect()
        rect.center = 300, 300
        self.window.blit(text, rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def _loot_item(self, gyver, items):
        for item in items: #If MacGyver move to the items position, his bag is incremented 
            #and messages are displayed
            if(gyver.x_pos == item.x_pos and gyver.y_pos == item.y_pos and
               item.looted is False):
                gyver.bag += 1
                item.looted = True
                self.show_message('You collected the {}'.format(item.name), BOT_LEFT)
                self.window.blit(FLOOR, (TILE_SIZE*item.x_pos, TILE_SIZE*item.y_pos))
                bag_message = "You collected {}/3 items".format(gyver.bag)
                self.show_message(bag_message, BOT_RIGHT)
                return item
        return None

    def set_map(self, mapping):
        for y_pos, line in enumerate(mapping.map):
            for x_pos, tile in enumerate(line):
                if tile == '#':
                    self.window.blit(WALL, (x_pos*TILE_SIZE, y_pos*TILE_SIZE))
                else:
                    self.window.blit(FLOOR, (x_pos*TILE_SIZE, y_pos*TILE_SIZE))

    def show_looted_items(self, items):
        for x_pos, item in enumerate(items):
            if item.looted:
                self.window.blit(item.pygame_img, (300+TILE_SIZE*x_pos, 605))
        pygame.display.flip()

    def set_characters(self, gyver, bad_guy):
        gyver_position = (gyver.x_pos * TILE_SIZE, gyver.y_pos * TILE_SIZE)

        bad_guy_position = (bad_guy.x_pos * TILE_SIZE, bad_guy.y_pos * TILE_SIZE)

        self.window.blit(gyver.pygame_img, gyver_position)
        self.window.blit(bad_guy.pygame_img, bad_guy_position)

    def set_items(self, items):
        for item in items:
            image = item.pygame_img
            self.window.blit(image, (item.x_pos * TILE_SIZE, item.y_pos * TILE_SIZE))

    def show_message(self, message, rect):
        #Set the game's messages in bottom strip
        self.window.fill((0, 0, 0), rect)
        text = message
        text_render = FONT.render(text, True, (0, 255, 0))
        self.window.blit(text_render, rect)
        pygame.display.update(rect)

    def move_character(self, mapping, gyver, items, old_pos):
        self.window.fill((0, 0, 0), BOT_LEFT)
        pygame.display.update(BOT_LEFT)
        #If the path is free, MacGyver can move and pick up the objects
        if (mapping.is_path_available(gyver.y_pos, gyver.x_pos) and
                (old_pos["y_pos"] != gyver.y_pos or old_pos["x_pos"] != gyver.x_pos)):
            mapping.move_character(old_pos["y_pos"], old_pos["x_pos"],
                                   gyver.y_pos, gyver.x_pos)
            self._loot_item(gyver, items)
            self.show_looted_items(items)
            self.window.blit(gyver.pygame_img,
                             (gyver.x_pos * TILE_SIZE, gyver.y_pos * TILE_SIZE))
            self.window.blit(FLOOR, (old_pos["x_pos"] * TILE_SIZE, old_pos["y_pos"] * TILE_SIZE))
            pygame.display.update()
        else:
            gyver.y_pos = old_pos["y_pos"]
            gyver.x_pos = old_pos["x_pos"]
            message = 'Invalid Destination'
            self.show_message(message, BOT_LEFT)
