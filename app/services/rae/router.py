from fastapi import APIRouter

from app.schemas.word_model import WordModel
from app.services.rae.manager import fetch_word

rae_router: APIRouter = APIRouter(prefix="/rae", tags=["RAE"])



@rae_router.get("/word/")
def router_get_word(name: str) -> WordModel:
    """
    Returns word, meanings and link.
    :return: word and definitions
    :rtype: WordModel
    """
    return fetch_word(name=name)