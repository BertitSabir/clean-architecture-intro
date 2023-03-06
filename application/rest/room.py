from typing import Any

from fastapi import APIRouter, Depends, Response
import orjson

from application.config import Settings, get_settings
from rentomatic.domain import entities
from rentomatic.repositories.memrepo import MemRepo
from rentomatic.use_cases.room_list import room_list_use_case


rooms = [
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "size": 215,
        "price": 39,
        "longitude": -0.09998975,
        "latitude": 51.75436293,
    },
    {
        "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
        "size": 405,
        "price": 66,
        "longitude": 0.18228006,
        "latitude": 51.74640997,
    },
    {
        "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
        "size": 93,
        "price": 48,
        "longitude": 0.33894476,
        "latitude": 51.39916678,
    },
]

room_router = APIRouter(
    prefix="/rooms", tags=["rooms"]
)


class CustomResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)


@room_router.get("/", response_class=CustomResponse, response_model=list[entities.room.Room])
async def info(settings: Settings = Depends(get_settings)):
    repo = MemRepo(rooms)
    result = room_list_use_case(repo)

    return result

