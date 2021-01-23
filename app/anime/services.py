from typing import List
from pydantic import BaseModel


class Anime(BaseModel):
    title: str
    year: int


class AnimeStorage:
    def get_anime(self) -> List[Anime]: ...


class AnimeListUseCase:
    def __init__(self, repo: AnimeStorage):
        self.repo = repo

    def show_anime(self) -> List[Anime]:
        rooms = self.repo.get_anime()
        return rooms
