from textures import get_a_texture


class Block:

    def __init__(self, coordinates, texture_nb, stopping_sides=None):

        if stopping_sides is None:
            stopping_sides = {"top": True,
                              "bottom": True,
                              "right": True,
                              "left": True
                              }
        self.image = get_a_texture(texture_nb)

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = coordinates

        self.stopping_sides = stopping_sides
