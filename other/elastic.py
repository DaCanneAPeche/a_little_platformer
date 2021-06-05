import pygame


class Elastic:

    def __init__(self, surface, totem_rect, size=400):
        self.surface = surface
        self.totem_pos = pygame.math.Vector2(totem_rect.topleft)
        self.size = size
        self.is_active = False

    def draw(self, start, end):

        if self.is_active:

            pygame.draw.line(self.surface, (200, 200, 200), start, end)

    def move_player(self, player_rect, totem_pos):

        if self.is_active:

            difference = (abs(player_rect.x - totem_pos.x), abs(player_rect.y - totem_pos.y))

            player_pos = pygame.math.Vector2(player_rect.topleft)
            direction = player_pos - self.totem_pos

            if sum(difference) > self.size:

                return list(map(int, (direction.normalize() * (sum(difference) // (self.size // 2))) * -1))
