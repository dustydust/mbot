from apps.common.requests import Request


class BittrexRequestHandler:

    @staticmethod
    def send_request(url):
        return Request.get(url)

    @staticmethod
    def handle_response(url):
        return Request.get(url)