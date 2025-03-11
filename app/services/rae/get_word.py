from fastapi import HTTPException

import requests
from bs4 import BeautifulSoup
from starlette import status
from loguru import logger
from starlette.responses import Response

from app.schemas.word_model import WordModel

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "es-ES,es;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0"
}



def _fetch_from_web(name: str) -> tuple[Response, str]:
    base_url = "https://www.wordreference.com/definicion/"
    final_url = base_url + name
    return requests.get(final_url, headers=headers), final_url


def parse_response_into_word(response: Response, name: str, url: str) -> WordModel:
    status_code = response.status_code

    logger.info(f"The response status code of the word {name} was {status_code}.")

    def get_definitions(s: BeautifulSoup) -> list[str]:
        return soup.find_all("ol")

    if status_code == status.HTTP_200_OK:
        soup = BeautifulSoup(response.text, features='html.parser')
        if (header := soup.find("h1")) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The word '{name}' does not exist in this dictionary. Try a different word.")

        full_name = header.text
        definitions = get_definitions(s=soup)

        return WordModel(name=full_name,
                         definitions=[d.text for d in definitions],
                         url=url)


    elif status_code == status.HTTP_400_BAD_REQUEST:
        logger.error(f"Error for word {name}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"There was an error in your request. The word '{name}' may not exist.")
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"There was an unexpected error.")


def get_word(name: str) -> WordModel:
    response, url = _fetch_from_web(name)
    return parse_response_into_word(response=response, name=name, url=url)
