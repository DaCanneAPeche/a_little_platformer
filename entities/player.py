import pygame
from entities.entity import Entity
from huv.health_bar import HealthBar


class Player(Entity):

    def __init__(self, game, x, y, velocity):

        super().__init__(game, x, y, 0, 1, velocity, player=True, offset=10)

        self.rect.height = 22

        self.max_health = 6
        self.health = self.max_health

        self.health_bar = HealthBar(self, self.max_health, self.health, offset=(4, -5), multiplier=4)

    def update_health_bar(self, scroll):

        self.health_bar.update_bar(self.health, scroll)

    def damage(self, amount):

        self.health -= amount

    def check_movements(self, pressed):

        if pressed[pygame.K_d]:
            self.movement[0] = self.velocity
            self.orientation = 'right'
            self.change_animation(1)

        elif pressed[pygame.K_q]:
            self.movement[0] = -1 * self.velocity
            self.orientation = 'left'
            self.change_animation(1)

        else:
            self.movement[0] = 0
            self.change_animation(0)

        if pressed[pygame.K_z]:

            self.jump()

        if self.rect.y >= self.game.position_marker.y + self.game.position_marker.height * 2:

            self.rect.y = self.game.position_marker.y - 50
            self.movement[1] = 0

            self.damage(3)

    def little_jump(self, minimum, pressed):

        if self.air_timer >= minimum and not pressed[pygame.K_z] and self.movement[1] < 0:

            self.y_momentum += 0.05
