import random

from pytcod import *
from src.entities import Entity


class Door(Entity):
    name = 'door'
    icon = "+"
    fg = GRAY
    bg = YELLOW
    block = True
    transparent = False
    uuid = None

    def __init__(self, x, y, uuid):
        self.uuid = uuid
        super(Door, self).__init__(x, y)

    def update(self, game):
        p = game.player
        xdif = abs(p.x - self.x)
        ydif = abs(p.y - self.y)
        if xdif == 1 and ydif == 0 or xdif == 0 and ydif == 1:
            game.opendoor(self.uuid)
        
exported_class = Door
