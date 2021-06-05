import pygame


class TileSheet:

    def __init__(self, file, tile_w, tile_h, columns_number, rows_number):
        self.file = pygame.image.load(file)
        self.width, self.height = tile_w * columns_number, tile_h * rows_number
        self.columns_number, self.rows_number = columns_number, rows_number

        self.tile_width, self.tile_height = tile_w, tile_h

    def get_a_tile(self, row, column):
        tile = pygame.surface.Surface((self.tile_width, self.tile_height))

        tile.set_colorkey((0, 0, 0))

        tile.blit(self.file, (0, 0),
                  (column * self.tile_width, row * self.tile_height, self.tile_width, self.tile_height))

        return tile


class SpriteSheet(TileSheet):

    def __init__(self, file, tile_w, tile_h, columns_number, rows_number):
        super().__init__(file, tile_w, tile_h, columns_number, rows_number)

    def load_animation(self, row, frames_number):
        animation = []

        for i in range(frames_number - 1):
            frame = self.get_a_tile(row, i)
            animation.append(frame)

        return animation


textures = []


def init_textures():
    tile_sheet = TileSheet('assets/tile_sheet.png', 32, 32, 3, 2)
    player_sheet = SpriteSheet('assets/sprites_sheets/player.png', 32, 32, 8, 9)
    fire_monster_sheet = SpriteSheet('assets/sprites_sheets/fire_monster.png', 32, 32, 8, 5)

    player_idle_animation = player_sheet.load_animation(0, 5)
    player_run_animation = player_sheet.load_animation(1, 9)
    player_animations = [player_idle_animation, player_run_animation]

    fire_idle_animation = fire_monster_sheet.load_animation(0, 8)
    fire_move_animation = fire_monster_sheet.load_animation(1, 6)
    fire_monster_animations = [fire_idle_animation, fire_move_animation]

    stone = tile_sheet.get_a_tile(0, 0)
    wood = tile_sheet.get_a_tile(0, 1)
    can_broken_wood = tile_sheet.get_a_tile(1, 0)
    broken_wood = tile_sheet.get_a_tile(1, 1)
    totem = tile_sheet.get_a_tile(2, 0)

    textures.append(player_animations)
    textures.append(fire_monster_animations)
    textures.append(stone)
    textures.append(wood)
    textures.append(can_broken_wood)
    textures.append(broken_wood)
    textures.append(totem)


def get_a_texture(texture_number):
    return textures[texture_number]
