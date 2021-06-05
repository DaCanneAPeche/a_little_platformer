from .block import Block
from other.elastic import Elastic


class Totem(Block):

    def __init__(self, x, y, surface, elastic_size=400):
        super().__init__((x, y), 6, {})

        self.elastic = Elastic(surface, self.rect, elastic_size)

    def draw_elastic(self, player_rect, scroll):
        self.elastic.draw((self.rect.x - scroll[0] + 15, self.rect.y - scroll[1] + 7),
                          (player_rect.x - scroll[0] + 16, player_rect.y - scroll[1] + 16))

    def move_player(self, player_rect):

        return self.elastic.move_player(player_rect, self.rect)
