import random

from pytcod import *
from src.entities.robotguard import RobotGuard
from src.entities import get


class MasterGuard(RobotGuard):
    name = 'masterguard'
    type = 'guard'
    icon = "M"
    uuid = "MASTERGUARD"
    colors = Color.gradient({0:RED, 5:GREEN})
    hp = 5

    def __init__(self, x, y):
        super(MasterGuard, self).__init__(x, y, "MASTERGUARD")

    def _getfg(self):
        return self.colors[self.hp]
    fg = property(_getfg)

    def do_move(self, game, dx, dy):
        if self.coord_in_bounds(game, dx, dy):
            blocker = self.thing_at_dest(game, dx, dy)
            if blocker:
                if blocker.type in ['player', 'invis']:
                    self.x = dx
                    self.y = dy
                    blocker.touched(game, self)
                elif blocker.type == 'guard':
                    game.remove(blocker)
                    game.add(get('scrap')(dx, dy))
                    self.checkfinish(game)
                    self.stun += 2
                elif not blocker.block:
                    self.x = dx
                    self.y = dy
            else:
                self.x = dx
                self.y = dy

    def checkfinish(self, game):
        self.hp -= 1
        if self.hp == 0:
            remove = []
            for ent in game.level.entities:
                if ent.type == 'guard':
                    remove.append(ent)
                    game.add(get('scrap')(ent.x, ent.y))
                elif ent.name in ['electricity', 'guardgenerator']:
                    remove.append(ent)
            for ent in remove:
                game.level.entities.remove(ent)
            remove = []
            for tile in game.level.tiles:
                if tile.type == 'electricity':
                    remove.append(tile)
            for tile in remove:
                game.level.tiles.remove(tile)
            
            game.remove(self)
            game.set_frame(42, 5, "Defeating Screwloose has disabled the Master-Key security!", "Success!")

    def touched(self, game, ent):
        if ent.type == 'guard':
            game.remove(ent)
            game.add(get('scrap')(self.x, self.y))
            self.checkfinish(game)
            self.stun += 2
            


exported_class = MasterGuard
