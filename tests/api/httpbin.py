from hogwarts_apitest.api import BaseApi


class ApiHttpbinGet(BaseApi):
    url = "http://httpbin.org/get"
    method = "GET"
    params = {}
    headers = {"Accept": "application/json"}


class ApiHttpbinPost(BaseApi):
    url = "http://httpbin.org/post"
    method = "POST"
    headers = {"Accept": "application/json"}
    json = {"abc": 123}


class ApiHttpbinGetCookies(BaseApi):
    url = 'http://httpbin.org/cookies'
    method = "GET"
    params = {}
    headers = {"Accept": "application/json"}