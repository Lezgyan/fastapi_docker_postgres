from typing import Final


class EntityNotFound(BaseException):
    _EXCEPTION_MESSAGE: Final[str] = "{entity} с id {_id} не найден(о)"

    def __init__(self, entity: str, _id: int) -> None:
        self.message = self._EXCEPTION_MESSAGE.format(entity=entity, _id=_id)

        super().__init__(self.message)
