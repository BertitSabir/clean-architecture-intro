import pytest

from rentomatic.requests.room_list import build_room_list_request


def test_build_room_list_request_without_filters():
    request = build_room_list_request()

    assert request.filters is None
    assert request.has_errors() is False
    assert bool(request) is True


def test_build_room_list_request_with_empty_filters():
    request = build_room_list_request({})

    assert request.filters == {}
    assert request.has_errors() is False
    assert bool(request) is True


def test_build_room_list_request_incorrect_filters_parameter():
    filters = 11
    request = build_room_list_request(filters=filters)

    assert bool(request) is False
    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"


@pytest.mark.parametrize(
    "key",
    ["code__eq", "price__gt", "price__lt", "price__eq"]
)
def test_build_room_list_request_accepted_filters_parameter(key):
    filters = {key: 11}
    request = build_room_list_request(filters=filters)

    assert bool(request) is True
    assert request.has_errors() is False
    assert request.filters == filters


@pytest.mark.parametrize(
    "key",
    ["code__lt", "code__gt", "size__lt", "size__gt", "size__eq"]
)
def test_build_room_list_request_rejected_filters(key):
    filters = {key: 11}
    request = build_room_list_request(filters=filters)
    assert bool(request) is False
    assert request.has_errors()
    assert request.errors[0]["parameter"] == key
