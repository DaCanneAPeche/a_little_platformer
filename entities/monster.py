from .entity import Entity


class Monster(Entity):

    def __init__(self, game, x, y, animation_number, orientation, attack, default_animation, speed=1):

        super().__init__(game, x, y, animation_number, attack, orientation, default_animation=default_animation,
                         health_multipier=12, health_offset=(3, 0))

        self.has_touch_the_floor = False
        self.speed = speed

    def hunt_player(self, player_pos):

        if player_pos.x < self.rect.x:

            self.movement[0] = self.speed * -1
            self.orientation = 'left'
            self.change_animation(1)

        elif player_pos.x > self.rect.x:
            self.movement[0] = self.speed
            self.orientation = 'right'
            self.change_animation(1)

        else:
            self.movement[0] = 0
            self.change_animation(0)

        self.jump()

class FireMonster(Monster):

    def __init__(self, game, x, y, orientation='right', speed=1):

        super().__init__(game, x, y, 1, orientation, 1, 1, speed=speed)

        self.rect.height = 16
