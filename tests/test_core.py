from tests.api.httpbin import *


def test_httpbin_get():
    ApiHttpbinGet().run() \
        .validate("status_code", 200)\
        .validate("headers.Connection", "keep-alive")\
        .validate("json.url", "https://httpbin.org/get")


def test_httpbin_get_with_params():
    ApiHttpbinGet()\
        .set_params(abc=123, xyz=456)\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.Connection", "keep-alive")\
        .validate("json.url", "https://httpbin.org/get?abc=123&xyz=456")\
        .validate("json.headers.Accept", "application/json")


def test_httpbin_post():
    ApiHttpbinPost().\
        set_data({"abc": 456})\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.Connection", "keep-alive") \
        .validate("json.url", "https://httpbin.org/post") \
        .validate("json.headers.Accept", "application/json")


def test_httpbin_parameters_share():
    user_id = "adk129"
    ApiHttpbinGet() \
        .set_params(user_id=user_id) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.Connection", "keep-alive") \
        .validate("json.url", "https://httpbin.org/get?user_id={}".format(user_id)) \
        .validate("json.headers.Accept", "application/json")

    ApiHttpbinPost(). \
        set_data({"user_id": user_id}) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.Connection", "keep-alive") \
        .validate("json.url", "https://httpbin.org/post") \
        .validate("json.headers.Accept", "application/json")\
        .validate("json.form.user_id", "adk129")


def test_httpbin_extract():
    status_code = ApiHttpbinGetCookies()\
        .run()\
        .extract("status_code")
    assert status_code == 200


def test_httpbin_parameters_extract():
    ApiHttpbinGetCookies()\
        .run()\
        .extract("status_code")
    user_id = 'adk129'
    ApiHttpbinPost(). \
        set_data({"user_id": user_id}) \
        .run() \
        .validate("status_code", 200) \
        .validate("headers.Connection", "keep-alive") \
        .validate("json.url", "https://httpbin.org/post") \
        .validate("json.headers.Accept", "application/json") \
        .validate("json.form.user_id", "adk129")
