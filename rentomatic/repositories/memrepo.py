from typing import List

from rentomatic.domain.entities.room import Room


class MemRepo:
    def __init__(self, data: List) -> None:
        self.data = data

    def list(self) -> List:
        return [Room.from_dict(room) for room in self.data]

