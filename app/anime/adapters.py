from typing import List

from .services import AnimeStorage, Anime


class MemoryStorage(AnimeStorage):

    def __init__(self):
        self._storage: List[Anime] = [
            Anime(title='Бездарная Нана', year=2020)
        ]

    def get_anime(self) -> List[Anime]:
        return self._storage
