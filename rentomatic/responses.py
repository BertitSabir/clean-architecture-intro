

class ResponseSuccess:

    def __init__(self, value=None):
        self.value = value
        self.type = 'success'

    def __bool__(self):
        return True


class ResponseFailure:
    def __init__(self, message=None):
        self.message = message
        self.type = 'failure'

    def __bool__(self):
        return False
