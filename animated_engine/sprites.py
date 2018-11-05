import pygame.sprite

__all__ = [
    "Object",
    "tangible"
]

tangible = set()

class Object(pygame.sprite.DirtySprite):
    __slots__ = "_tangible", "hp", "fragments"
    def __init__(self,
                 tangible=True,
                 hp=100, fragments=False):
        super().__init__(self)

        self.tangible = tangible
        self.hp = hp
        self.fragments = fragments

    @property
    def tangible(self):
        return self._tangible

    @tangible.setter
    def tangible(self, tangible):
        self._tangible = tangible
        if tangible:
            tangible.add(self)
        else:
            tangible.discard(self)
        
