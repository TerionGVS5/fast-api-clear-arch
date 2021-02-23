from typing import List

from sqlalchemy.orm import Session

from . import models
from .services import AnimeStorage, Anime


class MemoryStorage(AnimeStorage):

    def __init__(self):
        self._storage: List[Anime] = [
            Anime(title='Бездарная Нана', year=2020)
        ]

    def get_anime_list(self) -> List[Anime]:
        return self._storage


class SQLStorage(AnimeStorage):

    def __init__(self, db: Session):
        self.db = db

    def get_anime_list(self) -> List[Anime]:
        return self.db.query(models.Anime).all()
