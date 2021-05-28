from .block import Block


class WoodPlatform(Block):

    def __init__(self, coordinates):

        super().__init__(coordinates, 3, {'top': True})
