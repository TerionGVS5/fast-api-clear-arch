from typing import List

from fastapi import APIRouter, Depends

from .adapters import MemoryStorage
from .services import AnimeListUseCase, Anime

router = APIRouter(
    prefix="/anime",
    tags=["anime"],
)


def get_use_case() -> AnimeListUseCase:
    return AnimeListUseCase(MemoryStorage())


@router.get("/", response_model=List[Anime])
def anime(use_case=Depends(get_use_case)):
    return use_case.show_anime()
