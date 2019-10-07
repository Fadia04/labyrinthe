from classes.characters import Character

class MacGyver(Character):

    def __init__(self, y, x, img, mapping):
        Character.__init__(self, y, x, img, mapping)
        self.bag = 0

    def set_onmap(self, mapping):
        mapping.set_macgyver(self.y_pos, self.x_pos)

    def moving(self, direction):
        #MacGyver moves from tile to tile depending on the direction chosen by the player
        if direction == 'left':
            self.x_pos -= 1
        elif direction == 'right':
            self.x_pos += 1
        elif direction == 'bottom':
            self.y_pos += 1
        elif direction == 'top':
            self.y_pos -= 1
