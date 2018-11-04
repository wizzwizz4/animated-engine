import pygame
import pygame.sprite
try:
    from .utils import SignedList
except SystemError:
    from utils import SignedList

__all__ = ['Renderer']

class Renderer:
    def __init__(self, *, size=(640, 480), fullscreen=True):
        width, height = size

        if pygame.init()[1]:
            raise RuntimeError("pygame initalisation failed.")

        if fullscreen:
            winflags = 0
        colour_depth = pygame.display.mode_ok(size, winflags, 32)

        self._screen = pygame.display.set_mode(size, winflags, colour_depth)
        self._pg_sprites = {}

    def __del__(self):
        pygame.quit()

    def render(self, *, layers):
        old_ids = set(self._pg_sprites)
        new_ids = set()
        for layer in layers:
            for obj in layer:
                if id(obj) not in self._pg_sprites:
                    self._pg_sprites[id(obj)] = pygame.sprite.Sprite()
                # TODO: UPDATE STUFFZ
                new_ids.add(id(obj))

        for obj in old_ids - new_ids:
            # TODO: DELETE STUFFZ
            pass
