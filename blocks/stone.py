from .block import Block


class Stone(Block):

    def __init__(self, coordinates):

        super().__init__(coordinates, 2)
