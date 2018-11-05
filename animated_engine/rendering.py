import pygame.display

__all__ = ['Renderer']

class Renderer:
    __slots__ = "_should_quit", "_screen"

    def __init__(self, *, size=(640, 480), fullscreen=True):
        width, height = size

        self._should_quit = not pygame.display.get_init()
        pygame.display.init()

        if fullscreen:
            winflags = 0

        self._screen = pygame.display.set_mode(size, winflags)

    def __enter__(self):
        pass

    def __exit__(self, *a):
        if self._should_quit:
            pygame.quit()

    def __del__(self):
        if self._should_quit:
            pygame.quit()
