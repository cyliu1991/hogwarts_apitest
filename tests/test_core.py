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


def test_httpbin_get():
    ApiHttpbinGet().run() \
        .validate("status_code", 200)\
        .validate("headers.Connection", "keep-alive")\
        .validate("json().url", "https://httpbin.org/get")


def test_httpbin_get_with_params():
    ApiHttpbinGet()\
        .set_params(abc=123, xyz=456)\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.Connection", "keep-alive")\
        .validate("json().url", "https://httpbin.org/get")\
        .validate("json().headers.Accept", "application/json")


def test_httpbin_post():
    ApiHttpbinPost().\
        set_data({"abc": 456})\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.Connection", "keep-alive") \
        .validate("json().url", "https://httpbin.org/post") \
        .validate("json().headers.Accept", "application/json")
