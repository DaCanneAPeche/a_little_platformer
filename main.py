import pygame
from sys import platform
from game import Game


def main(screen, clock):
    game = Game(screen, clock)

    run = True

    while run:

        run = game.run(run)

    pygame.quit()


if __name__ == '__main__':

    pygame.init()

    size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

    if platform == 'darwin':  # if the os is apple mac

        size[1] -= 105  # doing a more little height screen because of mac dock bar

    win = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption('A little platform\'s game')
    main(win, pygame.time.Clock())
