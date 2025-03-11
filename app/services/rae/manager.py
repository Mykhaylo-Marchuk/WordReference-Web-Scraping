from app.infrastructure.database.word import Word
from app.schemas.word_model import WordModel
from app.services.rae.get_word import get_word
from app.shared.unit_of_work import UnitOfWork


def fetch_word(name: str) -> WordModel:
    with UnitOfWork() as uow:
        orm = uow.session.query(Word).filter_by(name=name).first()
        if orm is None:
            word: WordModel = get_word(name=name)
            orm = Word(name=name, **word.model_dump(exclude={"name"}))
            uow.session.add(orm)
            return word

        else:
            return WordModel.model_validate(orm)