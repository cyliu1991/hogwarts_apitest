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
        set_json({"abc": 456})\
        .run()\
        .validate("status_code", 200)\
        .validate("headers.Connection", "keep-alive") \
        .validate("json.url", "https://httpbin.org/post") \
        .validate("json.headers.Accept", "application/json")


def test_httpbin_get_cookies():
    ApiHttpbinGetCookies().run()


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
    httpbin_run = ApiHttpbinGet().run()
    status_code = httpbin_run.extract("status_code")
    assert status_code == 200

    connection = httpbin_run.extract("headers.Connection")
    assert connection == "keep-alive"


def test_httpbin_parameters_extract():
    cookies = ApiHttpbinSetCookies().run().extract("json.cookies.key")
    assert cookies == "123456"

    ApiHttpbinPost()\
        .set_json({"cookies": cookies})\
        .run()\
        .validate("json.json.cookies", cookies)


def test_httpbin_login_status():
    # step1 login and get cookie
    ApiHttpbinSetCookies().set_params(key="test").run()

    # step2
    resp = ApiHttpbinPost().set_json({"abc": "123"})\
        .run()

    request_headers = resp.response.request.headers
    print("=========", request_headers)

    assert "key=test" in request_headers["Cookie"]
