from .block import Block
from time import time
from textures import get_a_texture


class CanBrokenWoodPlatform(Block):

    def __init__(self, coordinates):

        super().__init__(coordinates, 4, {'top': True})

        self.start = 0
        self.is_map_loaded = False
        self.broken = False

    def start_timer(self):

        if not self.broken:

            if self.start == 0 and self.is_map_loaded:
                self.start = time()

            elif not self.is_map_loaded:
                self.is_map_loaded = True

    def check_timer(self):

        if time() - self.start > 2.0 and self.start > 0 and not self.broken:
            self.stopping_sides['top'] = False
            self.broken = True
            self.image = get_a_texture(5)
