from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel


class Movie(BaseModel):
    title: str
    director: str | list
    release_year: int
    genre: list
    description: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/users/{user_id}/")
async def get_user(
    user_id: Annotated[int, Path(title="The ID of the user to get", gt=0)]
):
    return {"name": "John Wick", "age": 43}


@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int) -> dict[str, str | int | list]:
    return {
        "title": "Spider-Man 3",
        "director": "Sam Raimi",
        "release_year": 2017,
        "genre": ["Action & Adventure", "Sci-Fi", "Fantasy"],
        "description": "The seemingly invincible Spider-Man goes up against an all-new crop of villains in the third installment of the blockbuster adventure series.",
    }


@app.post("/movies/create")
async def create_movie(movie: Movie):
    return movie
