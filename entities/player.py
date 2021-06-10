import pygame
from entities.entity import Entity


class Player(Entity):

    def __init__(self, game, x, y, velocity):

        super().__init__(game, x, y, 0, 1, velocity, player=True, offset=10, health=6, health_offset=(4, -5))

        self.rect.height = 22

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
