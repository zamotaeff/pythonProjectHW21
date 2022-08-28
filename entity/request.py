from exceptions import InvalidRequest


class Request:
    def __init__(self, request_string):

        req_list = request_string.lower().split(' ')

        if len(req_list) != 7:
            raise InvalidRequest

        self.quantity = int(req_list[1])
        self.title = req_list[2]
        self.departure = req_list[4]
        self.destination = req_list[6]
