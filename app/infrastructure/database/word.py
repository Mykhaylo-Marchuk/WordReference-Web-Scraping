from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.database_model import DatabaseModel


class Word(DatabaseModel):
    __tablename__ = "word"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    name: Mapped[str] = mapped_column(String, nullable = False)
    definitions: Mapped[str] = mapped_column(String, nullable = False)
    url: Mapped[str] = mapped_column(String, nullable = False)