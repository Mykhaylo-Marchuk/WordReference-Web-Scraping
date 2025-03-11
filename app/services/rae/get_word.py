import urllib.request

from fastapi import HTTPException

from bs4 import BeautifulSoup
from loguru import logger
from starlette import status
from starlette.responses import Response

from app.schemas.word_model import WordModel



def _fetch_from_web(name: str) -> tuple[Response, str]:
    base_url = "https://dle.rae.es/"
    final_url = base_url + name
    req = urllib.request.Request(final_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0')

    return req, final_url


def parse_response_into_word(req: urllib.request.Request, name: str, url: str) -> WordModel:
    status_code: status = 500
    try:
        response = urllib.request.urlopen(req)
        status_code = response.getcode()

    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"There was an unexpected error.")

    logger.info(f"The response status code of the word {name} was {status_code}.")

    def get_definitions(s: BeautifulSoup) -> list[str]:
        all_defs = soup.find_all("ol")
        spaced_defs = []
        for defin in all_defs:
            for a in defin.find_all("li"):
                spaced_defs.append(a)
        return spaced_defs

    if status_code == status.HTTP_200_OK:
        soup = BeautifulSoup(response, features='html.parser')
        if (header := soup.find("h1")) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The word '{name}' does not exist in this dictionary. Try a different word.")

        full_name = header.text
        definitions = get_definitions(s=soup)

        return WordModel(name=full_name,
                         definitions=[d.text for d in definitions],
                         url=url)



def get_word(name: str) -> WordModel:
    request, url = _fetch_from_web(name)
    return parse_response_into_word(req=request, name=name, url=url)
