
from rentomatic.responses import ResponseSuccess, ResponseFailure


def test_response_success_is_true():
    assert bool(ResponseSuccess()) is True


def test_response_failure_is_false():
    assert bool(ResponseFailure()) is False


def test_response_success_has_type_and_value():
    response = ResponseSuccess()
    assert response.type == "success"


def test_response_failure_has_type_and_message():
    message = "This is an error"
    response = ResponseFailure(message=message)
    assert response.type == "failure"
    assert response.message == message


