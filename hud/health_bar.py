import pygame


class HealthBar:

    def __init__(self, sprite, max_health, health, offset=None, multiplier=1):

        self.sprite = sprite

        self.multiplier = multiplier

        if offset is None:
            offset = (0, 0)

        self.offset = offset

        print(offset)

        x, y = sprite.rect.x + self.offset[0], sprite.rect.y + offset[1]

        self.background_color = (14, 48, 12)
        self.color = (31, 237, 16)

        self.background_bar = pygame.Rect(x, y, max_health * multiplier, 1)
        self.bar = pygame.Rect(x, y, health * multiplier, 1)

        self.x, self.y = x, y

    def update_bar(self, health, scroll):

        self.background_bar.x = self.sprite.rect.x + self.offset[0] - scroll[0]
        self.background_bar.y = self.sprite.rect.y + self.offset[1] - scroll[1]

        self.bar.x = self.sprite.rect.x + self.offset[0] - scroll[0]
        self.bar.y = self.sprite.rect.y + self.offset[1] - scroll[1]
        self.bar.width = health * self.multiplier

    def draw(self):
        pygame.draw.rect(self.sprite.game.surface, self.background_color, self.background_bar)
        pygame.draw.rect(self.sprite.game.surface, self.color, self.bar)
