import requests, json
from util.api.response import Response


class BaseCrud(object):
    def __init__(self, base_url, header):
        super().__init__()
        self.base_url = base_url
        self.header = header
        self.crud = {
            "get": self.get,
            "post": self.post,
            "put": self.put,
            "delete": self.delete,
        }

    def _fix_body(self, body):
        if type(body) == dict:
            for key in body.keys():
                if type(body[key]) == str:
                    body[key] = body[key].strip("\"")

    def _construct_url(self, url=None, **kwargs):
        new_url = self.base_url if not url else url
        for key in kwargs.keys():
            if type(kwargs[key]) == str:
                new_url = new_url.replace("{" + key + "}", kwargs[key].strip("\"") )
            else:
                new_url = new_url.replace("{" + key + "}", f"{kwargs[key]}")
        return new_url

    def get(self, body=None,url=None, **kwargs):
        new_url = self._construct_url(url=url, **kwargs)
        if body:
            self._fix_body(body)
            return Response(
                requests.get(new_url, json=body, headers=self.header)
            )
        else:
            return Response(requests.get(new_url, headers=self.header))

    def put(self, body=None,url=None, **kwargs):
        new_url = self._construct_url(url=url, **kwargs)
        if body:
            self._fix_body(body)
            return Response(
                requests.put(new_url, json=body, headers=self.header)
            )
        else:
            return Response(requests.put(new_url, headers=self.header))

    def post(self, body=None,url=None, **kwargs):
        new_url = self._construct_url(url=url, **kwargs)

        if body:
            self._fix_body(body)
            return Response(
                requests.post(new_url, json=body, headers=self.header)
            )
        else:
            return Response(requests.post(new_url, headers=self.header))

    def delete(self, body=None,url=None, **kwargs):
        new_url = self._construct_url(url=url,**kwargs)
        if body:
            self._fix_body(body)
            return Response(
                requests.delete(new_url, json=body, headers=self.header)
            )
        else:
            return Response(requests.delete(new_url, headers=self.header))
