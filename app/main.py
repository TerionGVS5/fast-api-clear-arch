from fastapi import FastAPI

from app.anime.rest import router as anime_router

app = FastAPI()

app.include_router(anime_router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications! Updated"}
