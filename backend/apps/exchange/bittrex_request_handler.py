from apps.common.requests import Request


class BittrexRequestHandler:

    base = "https://api.bittrex.com/v3/"

    @staticmethod
    def _send_request(url):
        return Request.get(self.base + url)

    @staticmethod
    def _handle_response(url):
        return Request.get(url)