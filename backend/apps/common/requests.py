import requests


class Request(object):

    @staticmethod
    def get(url, **kwargs):
        return requests.get(url, kwargs)

    @staticmethod
    def post(url, **kwargs):
        return requests.post(url, kwargs)
