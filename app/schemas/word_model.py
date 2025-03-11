import json
from typing import Literal, Any

from pydantic import BaseModel, field_validator, ConfigDict
from pydantic.main import IncEx


class WordModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    definitions: list[str]
    url: str

    @field_validator("definitions", mode="before")
    @classmethod
    def parse_definitions(cls, v: list[str] | str) -> list[str]:
        if isinstance(v, str):
            return json.loads(v)
        else:
            return v


    def model_dump(
        self,
        *,
        mode: Literal['json', 'python'] | str = 'python',
        include: IncEx | None = None,
        exclude: IncEx | None = None,
        context: Any | None = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal['none', 'warn', 'error'] = True,
        serialize_as_any: bool = False,
    ) -> dict[str, Any]:
        data = super().model_dump(mode=mode, include=include, exclude=exclude, context=context, by_alias=by_alias,
                                  exclude_unset=exclude_unset, exclude_defaults=exclude_defaults,
                                  exclude_none=exclude_none, round_trip=round_trip, warnings=warnings,
                                  serialize_as_any=serialize_as_any)
        data["definitions"] = json.dumps(self.definitions)
        return data
