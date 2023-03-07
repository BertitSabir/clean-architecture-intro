from abc import ABC, abstractmethod


class RoomLisRequest(ABC):

    def __init__(self, filters: dict = None):
        self.errors = []
        self.filters = filters

    @abstractmethod
    def __bool__(self):
        ...

    def add_error(self, parameter, message):
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self):
        return len(self.errors) > 0

    @classmethod
    def from_dict(cls, data):
        return cls()


class RoomListInvalidRequest(RoomLisRequest):

    def __bool__(self):
        return False


class RoomListValidRequest(RoomLisRequest):

    def __bool__(self):
        return True


def build_room_list_request(filters: dict = None):
    accepted_filters = [
        "code__eq",
        "price__eq",
        "price__gt",
        "price__lt",
    ]
    invalid_request = RoomListInvalidRequest()
    if filters is not None:
        if not isinstance(filters, dict):
            invalid_request.add_error(parameter="filters", message="filters must be a dict")
            return invalid_request
        for key, val in filters.items():
            if key not in accepted_filters:
                invalid_request.add_error(parameter=key, message=f"{key} is not a valid filter")
        if invalid_request.has_errors():
            return invalid_request
    return RoomListValidRequest(filters=filters)


